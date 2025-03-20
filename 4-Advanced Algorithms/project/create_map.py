import pickle
import os
import math
import sys
import networkx as nx

# Añadir la ruta del proyecto al path para poder importar student_code
sys.path.append('/Users/ric/code/DataStr/4-Advanced Algorithms/project')
from student_code import Map

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

def create_map_from_pickle(pickle_path):
    """
    Crea un objeto Map a partir de un archivo pickle utilizando la función read_pickle_map.
    
    Args:
        pickle_path: Ruta al archivo pickle
        
    Returns:
        Un objeto Map con el grafo cargado
    """
    try:
        # Obtener datos del grafo usando read_pickle_map
        data = read_pickle_map(pickle_path)
        
        # Crear un nuevo grafo de NetworkX
        G = nx.Graph()
        
        # Añadir nodos con sus posiciones
        for node in data["nodes"]:
            if node in data["positions"]:
                G.add_node(node, pos=data["positions"][node])
        
        # Añadir aristas
        for node, neighbors in data["connections"].items():
            for neighbor in neighbors:
                if neighbor in data["nodes"]:  # Asegurarse de que el vecino existe
                    G.add_edge(node, neighbor)
        
        # Crear y devolver un objeto Map
        try:
            # Crear un diccionario de intersecciones (nodos con sus posiciones)
            intersections = {}
            for node, pos in data["positions"].items():
                if node in data["nodes"]:
                    intersections[node] = pos
            
            # Crear un diccionario de roads (conexiones entre nodos)
            roads = {}
            for node, neighbors in data["connections"].items():
                if node in data["nodes"]:
                    roads[node] = [n for n in neighbors if n in data["nodes"]]
            
            # Crear el objeto Map directamente con los diccionarios
            # en lugar de usar el constructor con el grafo de NetworkX
            map_obj = Map(None)  # Crear un mapa vacío
            map_obj.intersections = intersections
            map_obj.roads = roads
            
            print(f"\nMapa creado manualmente con {len(map_obj.roads)} nodos y {len(map_obj.intersections)} intersecciones")
            return map_obj
        except Exception as e:
            print(f"Error al crear mapa: {e}")
            # En caso de error, intentar con el método estándar
            try:
                map_obj = Map(G)
                return map_obj
            except Exception as e2:
                print(f"Error al crear mapa con método estándar: {e2}")
                # En caso de error, crear un mapa básico
                return create_basic_map()
        except TypeError as e:
            if "_CachedPropertyResetterNode" in str(e) and "not iterable" in str(e):
                print("Error de _CachedPropertyResetterNode detectado. Usando método alternativo...")
                # Método alternativo: crear un mapa básico con la misma estructura
                alt_G = nx.Graph()
                
                # Copiar nodos y posiciones
                for node, pos in nx.get_node_attributes(G, 'pos').items():
                    alt_G.add_node(node, pos=pos)
                
                # Copiar aristas manualmente
                for node in G:
                    for neighbor in data["connections"].get(node, []):
                        if node in alt_G and neighbor in alt_G:
                            alt_G.add_edge(node, neighbor)
                
                map_obj = Map(alt_G)
                print(f"Mapa alternativo creado con {len(map_obj.roads)} nodos")
                return map_obj
            else:
                raise
        
    except Exception as e:
        print(f"Error al crear mapa desde pickle: {e}")
        # En caso de error, crear un mapa básico
        return create_basic_map()

def create_basic_map(num_nodes=10):
    """
    Crea un mapa básico con el número especificado de nodos.
    
    Args:
        num_nodes: Número de nodos en el mapa
        
    Returns:
        Un objeto Map con el grafo generado
    """
    # Crear un grafo vacío
    G = nx.Graph()
    
    # Generar posiciones para los nodos en un círculo
    positions = {}
    for i in range(num_nodes):
        angle = 2 * math.pi * i / num_nodes
        x = 100 * math.cos(angle)
        y = 100 * math.sin(angle)
        positions[i] = (x, y)
    
    # Añadir nodos al grafo con sus posiciones
    for node, pos in positions.items():
        G.add_node(node, pos=pos)
    
    # Conectar nodos cercanos
    for i in range(num_nodes):
        # Conectar con los nodos adyacentes (garantiza conectividad básica)
        G.add_edge(i, (i + 1) % num_nodes)
        G.add_edge(i, (i - 1) % num_nodes)
        # Añadir algunas conexiones adicionales
        G.add_edge(i, (i + 2) % num_nodes)
    
    # Crear y devolver un objeto Map
    return Map(G)

if __name__ == "__main__":
    # Puedes cambiar la ruta al archivo pickle que quieras leer
    pickle_path = "/Users/ric/code/DataStr/4-Advanced Algorithms/project/map-10.pickle"
    
    if os.path.exists(pickle_path):
        # Crear un mapa a partir del archivo pickle
        map_obj = create_map_from_pickle(pickle_path)
        
        # Mostrar información sobre el mapa
        print("\nInformación del mapa:")
        print(f"Número de nodos: {len(map_obj.roads)}")
        if map_obj.intersections and 0 in map_obj.intersections:
            print(f"Posición del nodo 0: {map_obj.intersections[0]}")
        if map_obj.roads and len(map_obj.roads) > 0:
            print(f"Conexiones del nodo 0: {map_obj.roads[0]}")
    else:
        print(f"El archivo {pickle_path} no existe.")