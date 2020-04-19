import networkx as nx
from random import randrange
import math


class Tsp:
    def __init__(self, number_of_cities):
        self.g = nx.complete_graph(number_of_cities)
        self.tour = []
        self.tour_length = 0
        self.tour_lengths = []

    # verteile weights fuer jede Kante
    def set_weights(self, t):
        if t == 'constant':
            for e in self.g.edges():
                self.g.add_edge(e[0], e[1], weight=int(math.sqrt((e[1] - e[0]) ** 2)))  # weights konstant zu nodenamen-differenz
        elif t == 'random':
            for e in self.g.edges():
                self.g.add_edge(e[0], e[1], weight=randrange(100))
        else:
            print("'constant' or 'random' expected")

    # random tsp-tour simulieren
    def random_tour(self):
        node_list = list(self.g.nodes)
        start = node_list[randrange(len(node_list))]
        self.tour = [start]
        self.tour_length = 0    # vielleicht unnötig
        for node in range(0, self.g.number_of_nodes() - 1):
            target = node_list[randrange(len(node_list))]
            while start == target:
                target = node_list[randrange(len(node_list))]
            self.tour_length += self.g.edges[start, target]['weight']
            node_list.remove(start)
            self.tour.append(target)
            start = target
        # rueckweg hinzufügen
        self.tour_length += self.g.edges[self.tour[0], target]['weight']
        self.tour_lengths.append(self.tour_length)

    def transposition(self):
        start = randrange(len(self.tour))
        target = randrange(len(self.tour))
        while start == target:
            target = randrange(len(self.tour))
        temp = self.tour[start]
        self.tour[start] = self.tour[target]
        self.tour[target] = temp

    def reversal(self):
        start = randrange(len(self.tour))
        target = randrange(len(self.tour))
        while start == target:
            target = randrange(len(self.tour))
        if start > target:
            temp = start
            start = target
            target = temp
        self.tour[start:target+1] = reversed(self.tour[start:target+1])

    def reevaluate_tour(self):
        new_tour_length = 0
        for t in range(0, len(self.tour)-1):
            new_tour_length += self.g.edges[self.tour[t], self.tour[t+1]]['weight']
        new_tour_length += self.g.edges[self.tour[0], self.tour[len(self.tour)-1]]['weight']
        self.tour_lengths.append(new_tour_length)
