import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from([0,1,2])
L = [[1,0,0,1],[0,1,1,1],[1,1,1,0]]
for i in range(0,3):
    for j in range(0,3):
        if L[i][j]==1:
            G.add_edge(i,j)
nx.draw_networkx(G,with_labels=True)
plt.show()