# from src.TradePost import TradePost
from src.Tree import Tree
from src.Agent import Agent, Player
import json

# TODO: Turns, player, tradeposts (different ones) i mplcursors, loading from json

p = Tree(3)
p.show()

# with open('./saves/map.json', 'w') as file:
#     json.dump(p.dict(), file)


# creation of agent and player
# pa = Player(2, 0)
#
# pa.show()
#
# currentp = p.map[pa.position]
# possibleposition = currentp.connections
# dir = int(input())
# pa.updateposition(pa.nextposition(connections=possibleposition, direction=dir))
#
# pa.show()

# basic movement of agent
# for i in range(10):
#     a.show()
#     currentp = p.map[a.position]
#     possibleposition = currentp.connections
#     a.updateposition(a.nextposition(possibleposition))


