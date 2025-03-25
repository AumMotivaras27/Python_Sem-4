import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(range(4,7))
G.add_edge(1,1)
G.add_edges_from([(2,3),(3,2),(3,6),(4,6),(5,6)])
# nx.draw_networkx(G,node_size=850,node_color='red',width=5,edge_color='blue')
nx.draw_networkx(G)
plt.show()