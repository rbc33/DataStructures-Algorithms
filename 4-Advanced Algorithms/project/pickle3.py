import pickle
import os
import math
import sys
import networkx as nx

# Añadir la ruta del proyecto al path para poder importar student_code
sys.path.append('/Users/ric/code/DataStr/4-Advanced Algorithms/project')

def read_pickle_map(file_path):
    """Lee un archivo pickle y extrae información de los nodos"""
    with open(file_path, 'rb') as f:
        graph = pickle.load(f)
    
    print(f"Tipo de objeto cargado: {type(graph)}")
    print(f"Archivo: {os.path.basename(file_path)}")
    
    # Inspeccionar el objeto directamente
    print("\nInspeccionando objeto directamente:")
    for attr_name in dir(graph):
        if not attr_name.startswith('__'):
            try:
                attr_value = getattr(graph, attr_name)
                print(f"  {attr_name}: {type(attr_value)}")
            except:
                print(f"  {attr_name}: <error al acceder>")
    
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
        
        # Intentar extraer nodos directamente del objeto
        try:
            # Verificar si el objeto tiene atributos específicos de Map
            if hasattr(graph, 'intersections') and hasattr(graph, 'roads'):
                print("\nDetectado objeto Map con intersections y roads")
                nodes = list(graph.intersections.keys())
                print(f"Nodos obtenidos de intersections: {nodes}")
                
                # Extraer posiciones y conexiones directamente
                positions = graph.intersections
                connections = graph.roads
                
                print(f"\nPosiciones extraídas directamente: {len(positions)} nodos")
                print(f"Conexiones extraídas directamente: {len(connections)} nodos")
                
                # Calcular distancias entre nodos conectados
                distances = {}
                for node in nodes:
                    distances[node] = {}
                    for neighbor in connections[node]:
                        x1, y1 = positions[node]
                        x2, y2 = positions[neighbor]
                        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        distances[node][neighbor] = distance
                
                return {
                    "graph": graph,
                    "nodes": nodes,
                    "positions": positions,
                    "connections": connections,
                    "distances": distances
                }
        except Exception as e:
            print(f"Error al extraer datos directamente: {e}")
        
        # Si no funcionó el método directo, intentar con métodos de NetworkX
        try:
            # Intentar diferentes métodos para obtener nodos
            methods_to_try = ['nodes', 'nodes_iter', 'get_node_list']
            for method_name in methods_to_try:
                if hasattr(graph, method_name):
                    method = getattr(graph, method_name)
                    if callable(method):
                        try:
                            result = method()
                            # Manejar específicamente el error de _CachedPropertyResetterNode
                            try:
                                nodes_list = list(result)
                                if nodes_list:
                                    nodes = nodes_list
                                    print(f"Nodos obtenidos con {method_name}(): {nodes}")
                                    break
                            except TypeError as e:
                                if "_CachedPropertyResetterNode" in str(e):
                                    print(f"Error de _CachedPropertyResetterNode en {method_name}()")
                                    # Intentar extraer nodos de otra manera
                                    if hasattr(graph, '_node'):
                                        nodes = list(graph._node.keys())
                                        print(f"Nodos obtenidos de _node: {nodes}")
                                        break
                                else:
                                    raise
                        except Exception as e:
                            print(f"Error al llamar {method_name}(): {e}")
        except Exception as e:
            print(f"Error al intentar obtener nodos: {e}")
        
        # Si no se encontraron nodos, crear nodos de prueba
        if not nodes:
            print("No se pudieron extraer nodos reales. Creando nodos de prueba...")
            # Determinar el número de nodos basado en el nombre del archivo
            filename = os.path.basename(file_path)
            if "map-10" in filename:
                num_nodes = 10
            elif "map-40" in filename:
                num_nodes = 40
            else:
                num_nodes = 10  # Valor predeterminado
                
            nodes = list(range(num_nodes))
            print(f"Nodos de prueba creados: {nodes}")
        
        # Intentar extraer posiciones
        positions = {}
        try:
            if hasattr(graph, 'nodes') and callable(getattr(graph, 'nodes')):
                for node in nodes:
                    try:
                        if node in graph.nodes and 'pos' in graph.nodes[node]:
                            positions[node] = graph.nodes[node]['pos']
                    except:
                        pass
        except:
            pass
        
        # Si no se encontraron posiciones, crear posiciones en círculo
        if not positions:
            print("\nCreando posiciones en círculo para los nodos...")
            for i, node in enumerate(nodes):
                angle = 2 * math.pi * i / len(nodes)
                x = 100 * math.cos(angle)
                y = 100 * math.sin(angle)
                positions[node] = (x, y)
        
        print("\nPosiciones para los nodos:")
        for i, (node, pos) in enumerate(positions.items()):
            # if i < 5:  # Mostrar solo los primeros 5 para no saturar la salida
            print(f"  Nodo {node}: {pos}")
        # if len(positions) > 5:
        #     print(f"  ... y {len(positions) - 5} más")
        
        # Intentar extraer conexiones
        connections = {}
        try:
            if hasattr(graph, 'adj'):
                for node in nodes:
                    if node in graph.adj:
                        connections[node] = list(graph.adj[node].keys())
            elif hasattr(graph, '_adj'):
                for node in nodes:
                    if node in graph._adj:
                        connections[node] = list(graph._adj[node].keys())
        except:
            pass
        
        # Si no hay conexiones, crear conexiones básicas
        if not connections or not any(connections.values()):
            print("\nCreando conexiones básicas entre nodos...")
            for node in nodes:
                # Conectar cada nodo con los 2-3 nodos siguientes (circular)
                num_connections = min(3, len(nodes) - 1)
                connections[node] = [(node + i) % len(nodes) for i in range(1, num_connections + 1)]
        
        print("\nConexiones para los nodos:")
        for i, (node, neighbors) in enumerate(connections.items()):
            # if i < 5:  # Mostrar solo los primeros 5 para no saturar la salida
            print(f"  Nodo {node} conectado a: {neighbors}")
        # if len(connections) > 5:
        #     print(f"  ... y {len(connections) - 5} más")
        
        # Calcular distancias entre nodos conectados
        distances = {}
        for node in nodes:
            distances[node] = {}
            for neighbor in connections.get(node, []):
                if node in positions and neighbor in positions:
                    x1, y1 = positions[node]
                    x2, y2 = positions[neighbor]
                    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    distances[node][neighbor] = distance
        
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
    Crea un objeto Map a partir de un archivo pickle.
    
    Args:
        pickle_path: Ruta al archivo pickle
        
    Returns:
        Un diccionario con la información del mapa
    """
    try:
        # Obtener datos del grafo
        data = read_pickle_map(pickle_path)
        return data
    except Exception as e:
        print(f"Error al procesar el archivo pickle: {e}")
        return None

if __name__ == "__main__":
    # Procesar ambos archivos pickle
    pickle_paths = [
        "/Users/ric/code/DataStr/4-Advanced Algorithms/project/map-10.pickle",
        "/Users/ric/code/DataStr/4-Advanced Algorithms/project/map-40.pickle"
    ]
    
    for pickle_path in pickle_paths:
        if os.path.exists(pickle_path):
            print(f"\n{'='*50}")
            print(f"Procesando {os.path.basename(pickle_path)}...")
            print(f"{'='*50}")
            data = create_map_from_pickle(pickle_path)
            if data:
                print(f"\nExtracción completada con éxito!")
                print(f"Nodos: {len(data['nodes'])}")
                print(f"Posiciones: {len(data['positions'])}")
                print(f"Conexiones: {len(data['connections'])}")
        else:
            print(f"El archivo {pickle_path} no existe.")