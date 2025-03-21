import networkx as nx
import pickle
import plotly.graph_objects as go
import random
from plotly.graph_objs import *
from plotly.offline import init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

class Map:
	def __init__(self, G):
		self._graph = G
		self.intersections = nx.get_node_attributes(G, "pos")
		self.roads = [list(G[node]) for node in G.nodes()]

	def save(self, filename):
		with open(filename, 'wb') as f:
			pickle.dump(self._graph, f)

def load_map(name):
	with open(name, 'rb') as f:
		G = pickle.load(f)
	return Map(G)

def create_map_from_data(roads_list, intersections_dict):
    """
    Create a Map object from a list of road connections and a dictionary of node positions.
    
    Args:
        roads_list: List of lists where each inner list contains the neighbors of a node
        intersections_dict: Dictionary mapping node IDs to their (x, y) positions
        
    Returns:
        A Map object with the provided data
    """
    # Create an empty graph
    G = nx.Graph()
    
    # Add nodes with their positions
    for node_id, pos in intersections_dict.items():
        G.add_node(node_id, pos=pos)
    
    # Add edges (connections between nodes)
    for node_id, neighbors in enumerate(roads_list):
        for neighbor in neighbors:
            G.add_edge(node_id, neighbor)
    
    # Create and return a Map object
    return Map(G)

def show_map(M, start=None, goal=None, path=None):
    G = M._graph
    pos = nx.get_node_attributes(G, 'pos')
    edge_trace = Scatter(
    x=[],
    y=[],
    line=Line(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

    for edge in G.edges():
        x0, y0 = G.node[edge[0]]['pos']
        x1, y1 = G.node[edge[1]]['pos']
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=Marker(
            showscale=False,
            # colorscale options
            # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
            # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
            colorscale='Hot',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))
    for node in G.nodes():
        x, y = G.node[node]['pos']
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    for node, adjacencies in enumerate(G.adjacency_list()):
        color = 0
        if path and node in path:
            color = 2
        if node == start:
            color = 3
        elif node == goal:
            color = 1
        # node_trace['marker']['color'].append(len(adjacencies))
        node_trace['marker']['color'].append(color)
        node_info = "Intersection " + str(node)
        node_trace['text'].append(node_info)

    fig = Figure(data=Data([edge_trace, node_trace]),
                 layout=Layout(
                    title='<br>Network graph made with Python',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                   
                    xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

    iplot(fig)

# Example usage of create_map_from_data
if __name__ == "__main__":
    # Road connections (each list represents connections for a node)
    roads_list = [
        [36, 34, 31, 28, 17],
        [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
        [39, 36, 21, 19, 9, 7, 4],
        [35, 20, 15, 11, 6],
        [39, 36, 21, 19, 9, 7, 2],
        [32, 16, 14],
        [35, 20, 15, 11, 1, 3],
        [39, 36, 22, 21, 19, 9, 2, 4],
        [33, 30, 14],
        [36, 21, 19, 2, 4, 7],
        [31, 27, 26, 25, 24, 18, 17, 13],
        [35, 20, 15, 3, 6],
        [37, 34, 31, 28, 22, 17],
        [27, 24, 18, 10],
        [33, 30, 16, 5, 8],
        [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
        [37, 30, 5, 14],
        [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
        [31, 27, 26, 25, 24, 1, 10, 13, 17],
        [21, 2, 4, 7, 9],
        [35, 26, 1, 3, 6, 11, 15],
        [2, 4, 7, 9, 19],
        [39, 37, 29, 7, 12],
        [38, 32, 29],
        [27, 10, 13, 18],
        [34, 31, 27, 26, 1, 10, 15, 17, 18],
        [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
        [31, 1, 10, 13, 18, 24, 25, 26],
        [39, 36, 34, 31, 0, 12, 17],
        [38, 37, 32, 22, 23],
        [33, 8, 14, 16],
        [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
        [38, 5, 23, 29],
        [8, 14, 30],
        [0, 12, 17, 25, 26, 28, 31],
        [1, 3, 6, 11, 15, 20],
        [39, 0, 2, 4, 7, 9, 28],
        [12, 16, 22, 29],
        [23, 29, 32],
        [2, 4, 7, 22, 28, 36]
    ]
    
    # Node positions
    intersections_dict = {
        0: [0.7801603911549438, 0.49474860768712914],
        1: [0.5249831588690298, 0.14953665513987202],
        2: [0.8085335344099086, 0.7696330846542071],
        3: [0.2599134798656856, 0.14485659826020547],
        4: [0.7353838928272886, 0.8089961609345658],
        5: [0.09088671576431506, 0.7222846879290787],
        6: [0.313999018186756, 0.01876171413125327],
        7: [0.6824813442515916, 0.8016111783687677],
        8: [0.20128789391122526, 0.43196344222361227],
        9: [0.8551947714242674, 0.9011339078096633],
        10: [0.7581736589784409, 0.24026772497187532],
        11: [0.25311953895059136, 0.10321622277398101],
        12: [0.4813859169876731, 0.5006237737207431],
        13: [0.9112422509614865, 0.1839028760606296],
        14: [0.04580558670435442, 0.5886703168399895],
        15: [0.4582523173083307, 0.1735506267461867],
        16: [0.12939557977525573, 0.690016328140396],
        17: [0.607698913404794, 0.362322730884702],
        18: [0.719569201584275, 0.13985272363426526],
        19: [0.8860336256842246, 0.891868301175821],
        20: [0.4238357358399233, 0.026771817842421997],
        21: [0.8252497121120052, 0.9532681441921305],
        22: [0.47415009287034726, 0.7353428557575755],
        23: [0.26253385360950576, 0.9768234503830939],
        24: [0.9363713903322148, 0.13022993020357043],
        25: [0.6243437191127235, 0.21665962402659544],
        26: [0.5572917679006295, 0.2083567880838434],
        27: [0.7482655725962591, 0.12631654071213483],
        28: [0.6435799740880603, 0.5488515965193208],
        29: [0.34509802713919313, 0.8800306496459869],
        30: [0.021423673670808885, 0.4666482714834408],
        31: [0.640952694324525, 0.3232711412508066],
        32: [0.17440205342790494, 0.9528527425842739],
        33: [0.1332965908314021, 0.3996510641743197],
        34: [0.583993110207876, 0.42704536740474663],
        35: [0.3073865727705063, 0.09186645974288632],
        36: [0.740625863119245, 0.68128520136847],
        37: [0.3345284735051981, 0.6569436279895382],
        38: [0.17972981733780147, 0.999395685828547],
        39: [0.6315322816286787, 0.7311657634689946]
    }
    
    # Create the map
    map_40 = create_map_from_data(roads_list, intersections_dict)
    
    # Print some information about the map
    print(f"Map created with {len(map_40.roads)} nodes")
    print(f"First 5 road connections: {map_40.roads[:5]}")
    print(f"First 5 intersections: {list(map_40.intersections.items())[:5]}")
    
    # Save the map to a file
    map_40.save("/Users/ric/code/DataStr/4-Advanced Algorithms/project/map-40-custom.pickle")
    print("Map saved to map-40-custom.pickle")
