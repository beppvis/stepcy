import sqlite3
import json
from classes_node import Node 
from classes_node import Neighbour

database = "../map.db"
table_name = "floor1"


# Assumes table created
def add_node(node:Node):
    try :
        cnt = sqlite3.connect(database)
        cur = cnt.cursor()     
        node_neighbour= {}
        for (neighbour_id,cost) in node.neighbours:
            node_neighbour[neighbour_id]=cost
        node_neighbour_str = json.dumps(node_neighbour)
        print(node_neighbour_str)
        query = '''insert into {} values('{}','{}')'''.format(table_name,node.id,node_neighbour_str)        
        print(query)
        cur.execute(query)

    except sqlite3.Error as error:
        print("Sqlite error : ",error)

    finally:
        if cnt:
            cnt.commit()
            cnt.close()

N = int(input("Enter no of nodes : "))
nodes = []

for i in range(1,N+1):
    nodeID = "node"+str(i)
    node = Node(nodeID)     
    nodes.append(node)

for node in nodes:
    print(node.id +" connectections : ")
    neighour_nums = int(input("Enter num of neighbour connections : "))

    for i in range(1,neighour_nums + 1):
        neighbour_num = int(input("Enter neighbour num  : "))
        cost = int(input("Enter cost to neighbour {} to {}: ".format(node.id,neighbour_num)))
        neighbour_id = "node"+str(neighbour_num)
        = 
        node.neighbours.append((neighbour_id,cost))
    add_node(node)
