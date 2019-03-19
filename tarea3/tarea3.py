import networkx as nx
import matplotlib.pyplot as plt
import time as tm
import numpy as np
from scipy import stats

G=nx.Graph()
G.add_nodes_from(['1','2','3'], bipartite=0)
G.add_nodes_from(['4','5'], bipartite=1)
G.add_edges_from([('1','5',)])
G.add_edges_from([('2','4',)])
G.add_edges_from([('2','5',)])
G.add_edges_from([('3','5',)])
G.add_edges_from([('3','4',)])
G.add_edges_from([('1','4',)])

tiempos = []
for i in range(30):
    start = tm.time()
    for x in range(8000000):
        nx.all_shortest_paths(G, source='1', target='3')
    end = tm.time()
    tiempos.append(end - start)

plt.hist(tiempos, bins='auto', alpha = 0.9, rwidth=0.85, color= '#FA0000')
plt.grid(axis='y', alpha=1)
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo (seg)')
plt.text(7.6,6.7, r'$\mu=7.29, \sigma=0.339$')
plt.text(7.7,6.2, r'$p=0.489$')


#########################2
G=nx.Graph()
G.add_nodes_from([1,5])
G.add_edges_from([(1,2),(1,3),(2,3),(3,4),(4,5),(5,5)])

tiempo2 = []
for i in range(30):
    start = tm.time()
    for x in range(8000000):
        nx.betweenness_centrality(G, normalized=True)
    end = tm.time()
    tiempo2.append(end - start)

print(tiempos)

plt.hist(tiempo2, bins='auto', alpha = 0.9, rwidth=0.85, color= 'gray')
plt.grid(axis='y', alpha=1)
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo(seg)')
plt.text(2200,5.7, r'$\mu=2082.23, \sigma=116.38$')
plt.text(2275,5.2, r'$p=0.59$')

################3

G=nx.DiGraph()

G.add_nodes_from(["1","2","3","4","5"])
G.add_edges_from([("1","2"),("2","3"),("3","4"),("4","5")])

tiempo3 = []
for i in range(30):
    start = tm.time()
    for x in range(8000000):
        nx.dfs_edges(G, source=0)
    end = tm.time()
    tiempo3.append(end - start)

plt.hist(tiempo3, bins='auto', alpha = 0.9, rwidth=0.85, color= 'black')
plt.grid(axis='y', alpha=1)
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo(seg)')
plt.text(6.8,5.7, r'$\mu=7.705, \sigma=0.397$')
plt.text(7,5.2, r'$p=0.182$')

######################################4
G=nx.DiGraph()
G.add_nodes_from([1,5])
G.add_edges_from([(1,2),(1,3),(2,3),(3,4),(4,5),(5,5)])

tiempo4 = []
for i in range(30):
    start = tm.time()
    for x in range(8000000):
        nx.greedy_color(G, strategy='largest_first')
    end = tm.time()
    tiempo4.append(end - start)

plt.hist(tiempo4, bins='auto', alpha = 0.9, rwidth=0.85, color= 'green')
plt.grid(axis='y', alpha=1)
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo(seg)')
plt.text(370, 7.7, r'$\mu=363.34, \sigma=6.816$')
plt.text(373, 7.2, r'$p=0.260$')

#################################5
G=nx.Graph()
G.add_nodes_from([1,5])
G.add_edges_from([(1,2),(1,3),(2,3),(3,4),(4,5),(5,5)])
tiempo5 = []
for i in range(30):
    start = tm.time()
    for x in range(20000):
        nx.max_weight_matching(G)
    end = tm.time()
    tiempo5.append(end - start)

plt.hist(tiempo5, bins='auto', alpha = 0.9, rwidth=0.85, color= 'gray')
plt.grid(axis='y', alpha=1)
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo(seg)')
plt.text(2700, 8.8, r'$\mu=2945.70, \sigma=113.52$')
plt.text(2750, 8.2, r'$p=0.962$')

colors = ['b', 'c', 'y', 'm', 'r']

a = plt.errorbar(np.mean(tiempo1), 6, xerr = np.std(tiempo1), c=colors[0], ecolor=colors[0], marker='o')
b = plt.errorbar(np.mean(tiempo2), 6, xerr = np.std(tiempo2), c=colors[1], ecolor=colors[1], marker='h')
c = plt.errorbar(np.mean(tiempo3), 6, xerr = np.std(tiempo3), c=colors[2], ecolor=colors[2], marker='*')
d = plt.errorbar(np.mean(tiempo4), 6, xerr = np.std(tiempo4), c=colors[3], ecolor=colors[3], marker='^')
e = plt.errorbar(np.mean(tiempo5), 6, xerr = np.std(tiempo5), c=colors[4], ecolor=colors[4], marker='<')

plt.legend((a, b, c, d, e),
           ('All shortest paths', 'Betweenness centrality', 'DFS tree', 'Greedy color','Max weight matching'),
           scatterpoints=1,
           loc='best',
           ncol=1,
           fontsize=8)

plt.xlabel("Tiempo promedio de ejecución (seg)")
plt.ylabel("Cantidad de aristas")

plt.show()