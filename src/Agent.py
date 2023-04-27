import random


class Agent:

    def __init__(self, position, id):
        self.position = position
        self.id = id

    @staticmethod
    def create(position, id):
        return Agent(position, id)

    def nextposition(self, connections):
        return random.choice(connections)

    def updateposition(self, newposition):
        self.position = newposition

    def show(self):
        print("id:", self.id, "position:", self.position)