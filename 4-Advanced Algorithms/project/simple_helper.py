import pickle
import networkx as nx
import matplotlib.pyplot as plt

def load_simple_map(filename):
    """Load map from pickle file and return basic components"""
    with open(filename, 'rb') as f:
        G = pickle.load(f)
    
    # Extract intersections (positions)
    intersections = {}
    for node in G.nodes():
        try:
            # Try different ways to access position data
            if hasattr(G, 'nodes') and callable(getattr(G, 'nodes')):
                if 'pos' in G.nodes[node]:
                    intersections[node] = G.nodes[node]['pos']
            elif hasattr(G, 'node'):
                if 'pos' in G.node[node]:
                    intersections[node] = G.node[node]['pos']
        except:
            # Default position if we can't find it
            intersections[node] = (0, 0)
    
    # Extract roads (connections)
    roads = []
    for node in G.nodes():
        try:
            roads.append(list(G.neighbors(node)))
        except:
            try:
                roads.append(list(G[node]))
            except:
                roads.append([])
    
    return {'graph': G, 'intersections': intersections, 'roads': roads}

def show_simple_map(map_data, start=None, goal=None, path=None):
    """Display map using matplotlib instead of plotly"""
    plt.figure(figsize=(10, 10))
    
    # Draw edges
    for i, neighbors in enumerate(map_data['roads']):
        for j in neighbors:
            x0, y0 = map_data['intersections'][i]
            x1, y1 = map_data['intersections'][j]
            plt.plot([x0, x1], [y0, y1], 'k-', alpha=0.3)
    
    # Draw nodes
    for i, pos in map_data['intersections'].items():
        color = 'blue'
        if path and i in path:
            color = 'green'
        if i == start:
            color = 'red'
        elif i == goal:
            color = 'purple'
        plt.plot(pos[0], pos[1], 'o', markersize=10, color=color)
        plt.text(pos[0], pos[1], str(i), fontsize=12)
    
    plt.title('Map Visualization')
    plt.axis('equal')
    plt.grid(True)
    plt.show()