import networkx as nx
from random import randrange


def random_weights():
    weights = []
    for i in range(0, 100):
        weights[i] = i
    return weights

class Tsp:
    def __init__(self, number_of_cities):
        self.cities = nx.complete_graph(number_of_cities)
        self.rand = []

