import random


class Agent:

    def __init__(self, position, id, speed):
        self.position = position
        self.destination = None
        self.destination_weight = None
        self.id = id
        self.speed = speed
        self.moving = False

    @staticmethod
    def create(position, id, speed):
        return Agent(position, id, speed)

    def nextposition(self, connections):
        if not self.moving:
            t = random.randrange(0, len(connections.connections))
            self.destination = connections.connections[t]
            self.destination_weight = connections.weights[t]
        else:
            pass
        return self.destination

    def updateposition(self, newposition):
        #self.position = newposition
        pass
    def show(self):
        print("id:", self.id, "position:", self.position)


class Player(Agent):
    def nextposition(self, connections, direction):
        if direction == self.position:
            print("not moving")
            return direction
        elif direction in connections:
            return direction
        else:
            print("no connection")
