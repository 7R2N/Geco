#from src.TradePost import TradePost
from src.Tree import Tree
from src.Agent import Agent

p = Tree()

p.show()

a = Agent(2, 0)

a.show()

for i in range(10):
    a.show()
    currentp = p.map[a.position]
    possibleposition = currentp.connections
    a.updateposition(a.nextposition(possibleposition))
    #TODO better display, wagi, logika poruszania sie, implementacja punktów, dodanie różnych rodzajów punktów