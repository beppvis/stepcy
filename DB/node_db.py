import sqlite3
import json
from classes_node import Node 
from classes_node import Neighbour

database = "../map.db"
table_name = "floor1"


# Assumes table created
def add_node(node: Node):
    try:
        cnt = sqlite3.connect(database)
        cur = cnt.cursor()

        # Prepare the data structure for neighbors with classroom information
        node_data = {}
        for (neighbour_id, cost) in node.neighbours:
            # Classroom information between this node and its neighbor
            classroom_info = node.classroom_info.get(neighbour_id, {})
            node_data[neighbour_id] = {
                "cost": cost,
                "classroom_info": classroom_info
            }

        # Convert the entire structure to a JSON string
        node_data_str = json.dumps(node_data)
        print(node_data_str)  # Debug print to verify JSON structure

        # Corrected SQL query to insert node data into the table
        query = '''INSERT INTO {} (node_id, node_data) VALUES (?, ?)'''.format(table_name)

        print(query)  # Debug print to verify query
        cur.execute(query, (node.id, node_data_str))  # Use parameterized query to avoid SQL injection

    except sqlite3.Error as error:
        print("SQLite error:", error)

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
>>>>>>> de0959bf1affb6b3184a02655d7af3829b2a3167

def get_data_all():
    try :
        cnt = sqlite3.connect(database)
        cur = cnt.cursor()     
        cur = cur.execute("select * from floor1;")
        vals = cur.fetchall()
        return vals

    except sqlite3.Error as error:
        print("sqlite error : ",error)

    finally:
        if cnt:
            cnt.close()
