import random

#TODO naprawić wiszące wierzchołki, podgrafy, różne prędkosci na tej samej sciezce
class Point:
    def __init__(self, id, connections, weights):
        self.id = id
        self.connections = connections
        self.weights = weights

    @staticmethod
    def create(id, connections, weights):
        return Point(id, connections, weights)

class Tree:
    def __init__(self, size):
        self.map = []
        for i in range(size):
            rand = random.randrange(1, size)
            connections = [random.randrange(0, size) for c in range(rand)]
            weights = [random.random() for c in range(rand)]
            nPoint = Point.create(i, connections, weights)
            self.map.append(nPoint)

    def show(self):
        for i in self.map:
            print(i.id, i.connections, i.weights)