# from src.TradePost import TradePost
from src.Tree import Tree
from src.Agent import Agent, Player
from src.Map import Map
import json

# TODO: Turns, player, tradeposts (different ones) i mplcursors, loading from json


if __name__ == '__main__':

    tree = Tree(10)
    a = Agent.create(0,0)
    viewer = Map(tree)
    viewer.add_agent(a)
    viewer.run()

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


