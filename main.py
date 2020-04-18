import networkx as nx
from random import randrange
import math


# g ist vollst. Graph, der Karte mit 100 Staedten darstellen soll
g = nx.complete_graph(100)

# verteile weights fuer jede Kante
for e in g.edges():
    # g.add_edge(e[0], e[1], weight=randrange(100))
    g.add_edge(e[0], e[1], weight=int(math.sqrt((e[1]-e[0])**2))) # weights konstant zu nodenamen-differenz

# random tsp-tour simulieren
node_list = list(g.nodes)
tour_total = 0
start = node_list[randrange(len(node_list))]
tour = [start]
for node in range(0, g.number_of_nodes()-1):
    target = node_list[randrange(len(node_list))]
    while start == target:
        target = node_list[randrange(len(node_list))]
    tour_total += g.edges[start, target]['weight']
    node_list.remove(start)
    tour.append(target)
    start = target
# rueckweg hinzufügen
tour_total += g.edges[tour[0], target]['weight']
tour.append(tour[0])

print(tour_total)
print(tour)
