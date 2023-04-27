import random

#TODO naprawić wiszące wierzchołki, podgrafy, różne prędkosci na tej samej sciezce,
class Point:
    def __init__(self, id, connections, weights):
        self.id = id
        self.connections = connections
        self.weights = weights
        self.money = 0
        self.goods = None

    @staticmethod
    def create(id, connections, weights):
        return Point(id, connections, weights)

    def trade(self):
        self.money += 5

    def refill(self):
        pass

class Tree:
    def __init__(self):
        self.map = []
        for i in range(5):
            connections = [random.randrange(0, 4) for c in range(3)]
            weights = [random.random() for c in range(3)]
            nPoint = Point.create(i, connections, weights)
            self.map.append(nPoint)

    def show(self):
        for i in self.map:
            print(i.id, i.connections, i.weights)