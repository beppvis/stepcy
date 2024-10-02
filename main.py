import math
class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Node:
    def __init__(self,pos:Pos,g:int,h:float,parent:Node=self):
        self.parent = parent
        self.f = g+h
        self.g = g
        self.h = h
        self.pos = pos


class Map:
    def __init__(self,Open:[Node],Closed:[Node]):
        self.open_nodes = Open
        self.closed_nodes = Closed


i = 0
open_nodes = []
x = 0 
y = 0
while (i<10):
    pos = Pos(x,y)
    node = Node(pos,0,0,None)
    open_nodes.append(node)
    x += 1
    y += 1
    
    i += 1




