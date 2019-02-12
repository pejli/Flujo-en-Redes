import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_nodes_from(['1','2','3', '4','5']) 
G.add_edges_from([('1','2'),('1','3',)])   
G.add_edges_from([('2','4')])
G.add_edges_from([('3','5')])


nx.draw(G,with_labels=True)                            
plt.show() 