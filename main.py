
class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Node:
    def __init__(self,pos:Pos,g:int,h:float,parent:Node):
        self.parent = parent
        self.f = g+h
        self.g = g
        self.h = h
        self.pos = pos


class Map:
    def __init__(self,Open:[Node],Closed:[Node]):
        self.open = Open
        self.closed = Closed








