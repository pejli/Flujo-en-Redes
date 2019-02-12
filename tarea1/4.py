import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()
G.add_nodes_from(["1","2","3","4","5"])

G.add_edges_from([("1","2"),("2","3"),("3","4"),("4","5")])
nx.draw(G,with_labels=True)
plt.savefig("Graph2.eps", format="EPS")
plt.show()

