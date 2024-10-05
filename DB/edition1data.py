import sqlite3
import json
from classes_node import Node

database = "../map.db"
table_name = "AB1floor1"


# Assumes table created
def add_node(node: Node):
    try:
        cnt = sqlite3.connect(database)
        cur = cnt.cursor()
        
        # Prepare the data structure for neighbors and classes
        node_data = {}
        for (neighbour_id, cost) in node.neighbours:
            node_data[neighbour_id] = {
                "cost": cost,
                "classleft": node.classleft.get(neighbour_id, {}),
                "classright": node.classright.get(neighbour_id, {}),
                "classback": node.classback.get(neighbour_id, {}),
                "classfront": node.classfront.get(neighbour_id, {})
            }

        # Convert the entire structure to a JSON string
        node_data_str = json.dumps(node_data)
        print(node_data_str)  # Debug print to verify JSON structure
        
        # Insert the data into the table
        query = '''INSERT INTO {} (node_id, node_data) VALUES ('{}', '{}')'''.format(
            table_name, node.id, node_data_str
        )
        
        print(query)  # Debug print to verify query
        cur.execute(query)

    except sqlite3.Error as error:
        print("SQLite error:", error)

    finally:
        if cnt:
            cnt.commit()
            cnt.close()

# Example of creating nodes and adding them to the database
N = int(input("Enter number of nodes: "))
nodes = []

for i in range(1, N + 1):
    nodeID = "node" + str(i)
    node = Node(nodeID)
    nodes.append(node)

    print(node.id + " connections:")
    neighbour_count = int(input("Enter number of neighbour connections: "))

    for j in range(1, neighbour_count + 1):
        neighbour_num = int(input("Enter neighbour number: "))
        cost = int(input("Enter cost to neighbour {} to {}: ".format(node.id, neighbour_num)))
        neighbour_id = "node" + str(neighbour_num)
        node.neighbours.append((neighbour_id, cost))

    # Getting class data for neighbors from the user
    classleft = json.loads(input("Enter classleft information (as JSON for all neighbors): "))
    classright = json.loads(input("Enter classright information (as JSON for all neighbors): "))
    classback = json.loads(input("Enter classback information (as JSON for all neighbors): "))
    classfront = json.loads(input("Enter classfront information (as JSON for all neighbors): "))

    # Set class information for the node
    node.classleft = classleft
    node.classright = classright
    node.classback = classback
    node.classfront = classfront

    # Add node to the database
    add_node(node)
