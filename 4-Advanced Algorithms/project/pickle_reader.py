import pickle
import os

def read_pickle_map(file_path):
    """Lee un archivo pickle y extrae información de los nodos"""
    with open(file_path, 'rb') as f:
        graph = pickle.load(f)
    
    print(f"Tipo de objeto cargado: {type(graph)}")
    print(f"Atributos disponibles: {dir(graph)}")
    
    # Intentar extraer nodos de manera más robusta
    nodes = []
    try:
        nodes = list(graph.nodes())
        print(f"Número de nodos: {len(nodes)}")
        print(f"Nodos: {nodes}")
    except Exception as e:
        print(f"Error al obtener nodos: {e}")
        try:
            # Intento alternativo
            nodes = list(graph)
            print(f"Número de nodos (método alternativo): {len(nodes)}")
            print(f"Nodos: {nodes}")
        except Exception as e2:
            print(f"También falló el método alternativo: {e2}")
            
            # Intento adicional para NetworkX 1.11
            try:
                if hasattr(graph, 'adj'):
                    nodes = list(graph.adj.keys())
                    print(f"Número de nodos (desde adj): {len(nodes)}")
                    print(f"Nodos: {nodes}")
                elif hasattr(graph, '_adj'):
                    nodes = list(graph._adj.keys())
                    print(f"Número de nodos (desde _adj): {len(nodes)}")
                    print(f"Nodos: {nodes}")
            except Exception as e3:
                print(f"Tercer intento falló: {e3}")
                
                # Último recurso: inspeccionar el objeto directamente
                print("\nInspeccionando objeto directamente:")
                for attr_name in dir(graph):
                    if not attr_name.startswith('_'):
                        try:
                            attr_value = getattr(graph, attr_name)
                            print(f"  {attr_name}: {type(attr_value)}")
                            if attr_name in ['node', 'nodes', 'adj', '_adj', '_node']:
                                print(f"    Contenido: {attr_value}")
                        except:
                            print(f"  {attr_name}: <error al acceder>")
    
    # Intentar extraer posiciones
    positions = {}
    for node in nodes:
        try:
            if hasattr(graph, 'nodes') and callable(getattr(graph, 'nodes')):
                try:
                    if 'pos' in graph.nodes[node]:
                        positions[node] = graph.nodes[node]['pos']
                except:
                    pass
            elif hasattr(graph, 'node'):
                try:
                    if 'pos' in graph.node[node]:
                        positions[node] = graph.node[node]['pos']
                except:
                    pass
        except:
            pass
    
    print(f"Posiciones encontradas para {len(positions)} nodos")
    for node, pos in positions.items():
        print(f"  Nodo {node}: {pos}")
    
    # Intentar extraer conexiones
    connections = {}
    for node in nodes:
        try:
            neighbors = list(graph.neighbors(node))
            connections[node] = neighbors
        except:
            try:
                neighbors = list(graph[node])
                connections[node] = neighbors
            except:
                try:
                    if hasattr(graph, 'adj'):
                        neighbors = list(graph.adj[node].keys())
                        connections[node] = neighbors
                except:
                    connections[node] = []
    
    print("\nConexiones:")
    for node, neighbors in connections.items():
        print(f"  Nodo {node} conectado a: {neighbors}")
    
    return {
        "graph": graph,
        "nodes": nodes,
        "positions": positions,
        "connections": connections
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