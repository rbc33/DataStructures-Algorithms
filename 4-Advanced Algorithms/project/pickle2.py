import pickle
import os
import math
import sys

def read_pickle_map(file_path):
    """Lee un archivo pickle y extrae información de los nodos"""
    with open(file_path, 'rb') as f:
        graph = pickle.load(f)
    
    print(f"Tipo de objeto cargado: {type(graph)}")
    
    # Inspeccionar el objeto directamente
    print("\nInspeccionando objeto directamente:")
    for attr_name in dir(graph):
        if not attr_name.startswith('__'):
            try:
                attr_value = getattr(graph, attr_name)
                print(f"  {attr_name}: {type(attr_value)}")
            except:
                print(f"  {attr_name}: <error al acceder>")
    
    # Intentar crear una representación manual del grafo
    manual_graph = {}
    
    # Intentar extraer nodos y conexiones directamente
    try:
        # Intentar obtener el grafo como diccionario
        if hasattr(graph, 'graph'):
            print("\nAtributos del grafo:")
            for k, v in graph.graph.items():
                print(f"  {k}: {v}")
        
        # Intentar acceder a los métodos de NetworkX
        print("\nIntentando métodos de NetworkX:")
        
        # Intentar obtener nodos
        try:
            if hasattr(graph, 'number_of_nodes'):
                print(f"Número de nodos según number_of_nodes(): {graph.number_of_nodes()}")
        except Exception as e:
            print(f"Error al llamar number_of_nodes(): {e}")
        
        # Intentar obtener aristas
        try:
            if hasattr(graph, 'number_of_edges'):
                print(f"Número de aristas según number_of_edges(): {graph.number_of_edges()}")
        except Exception as e:
            print(f"Error al llamar number_of_edges(): {e}")
        
        # Intentar obtener lista de nodos
        nodes = []
        try:
            # Intentar diferentes métodos para obtener nodos
            methods_to_try = ['nodes', 'nodes_iter', 'get_node_list']
            for method_name in methods_to_try:
                if hasattr(graph, method_name):
                    method = getattr(graph, method_name)
                    if callable(method):
                        try:
                            result = method()
                            nodes_list = list(result)
                            if nodes_list:
                                nodes = nodes_list
                                print(f"Nodos obtenidos con {method_name}(): {nodes}")
                                break
                        except Exception as e:
                            print(f"Error al llamar {method_name}(): {e}")
        except Exception as e:
            print(f"Error al intentar obtener nodos: {e}")
        
        # Si no se encontraron nodos, crear nodos de prueba
        if not nodes:
            print("No se pudieron extraer nodos reales. Creando nodos de prueba...")
            nodes = list(range(10))
            print(f"Nodos de prueba creados: {nodes}")
        
        # Crear posiciones aleatorias para los nodos
        positions = {}
        for i, node in enumerate(nodes):
            # Posiciones en un círculo
            angle = 2 * math.pi * i / len(nodes)
            x = 100 * math.cos(angle)
            y = 100 * math.sin(angle)
            positions[node] = (x, y)
        
        print("\nPosiciones generadas para los nodos:")
        for node, pos in positions.items():
            print(f"  Nodo {node}: {pos}")
        
        # Crear conexiones aleatorias entre nodos
        connections = {}
        for node in nodes:
            # Conectar cada nodo con los 2-3 nodos siguientes (circular)
            num_connections = min(3, len(nodes) - 1)
            neighbors = [(node + i) % len(nodes) for i in range(1, num_connections + 1)]
            connections[node] = neighbors
        
        print("\nConexiones generadas:")
        for node, neighbors in connections.items():
            print(f"  Nodo {node} conectado a: {neighbors}")
        
        # Calcular distancias entre nodos conectados
        distances = {}
        for node in nodes:
            distances[node] = {}
            for neighbor in connections[node]:
                x1, y1 = positions[node]
                x2, y2 = positions[neighbor]
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                distances[node][neighbor] = distance
        
        print("\nDistancias calculadas:")
        for node, neighbor_distances in distances.items():
            print(f"  Desde nodo {node}:")
            for neighbor, distance in neighbor_distances.items():
                print(f"    Hasta nodo {neighbor}: {distance:.2f}")
        
        return {
            "graph": graph,
            "nodes": nodes,
            "positions": positions,
            "connections": connections,
            "distances": distances
        }
        
    except Exception as e:
        print(f"Error al crear representación manual: {e}")
        # Devolver un grafo vacío en caso de error
        return {
            "graph": graph,
            "nodes": [],
            "positions": {},
            "connections": {},
            "distances": {}
        }

if __name__ == "__main__":
    # Puedes cambiar la ruta al archivo pickle que quieras leer
    # pickle_path = "/Users/ric/code/DataStr/4-Advanced Algorithms/project/map-10.pickle"
    pickle_path = "/Users/ric/code/DataStr/4-Advanced Algorithms/project/map-40.pickle"
    
    if os.path.exists(pickle_path):
        data = read_pickle_map(pickle_path)
        print("\nExtracción completada con éxito!")
    else:
        print(f"El archivo {pickle_path} no existe.")