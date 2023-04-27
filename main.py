import src.TradePost as tp
from src.Tree import Tree
from src.Agent import Agent

p = Tree()

p.show()

a = Agent(2,0)

a.show()

for i in range(10):
    a.show()
    currentp = p.map[a.position]
    possibleposition = currentp.connections
    a.updateposition(a.nextposition(possibleposition))
    #TODO better display, wagi, logika poruszania sie, implementacja punktów

# wewnatrz klasy przestrzen robiłbym sobie wszystko, drzewo ważone
# LISTA ( DICTIONARY)   , OBIEKT, NEXT POINT I LISTA PUNKTÓW
# FUNKCJA DEFINIUJACA SCIEZKE
# w petli get next agenta, generuje nastepny punkt, przesuwamy go,
# w miejscu get next moge zrobić wszystko