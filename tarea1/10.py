import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
Vertices={1:(0,0),2:(-1,-1),3:(1,-1),4:(2,-1),5:(2,0),6:(4,-1),7:(5,-1)}
Aristas=[(3,1),(2,1),(3,2),(3,4),(2,4),(4,5),(7,5),(6,5)]

nx.draw_networkx_nodes(G, Vertices,nodelist = [1,2,3,4,5,6,7], node_color = 'b')
nx.draw_networkx_edges(G,Vertices,width=1, edgelist=Aristas,alpha=1)

plt.axis('off')