import sqlite3
import json

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours = []  # To store tuples of (neighbour_id, cost)
        self.classroom_info = {}  # Initialize classroom_info as an empty dictionary


database = "../map.db"
query = "create table"
table_name = "AB1floor1"
query = "create table "+table_name+";"


cnt = sqlite3.connect(database)
cur = cnt.cursor()
cur.execute("create table AB1floor1")
cur.close()
cnt.commit()
cnt.close()

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
        cost = int(input(f"Enter cost to neighbour {node.id} to node{neighbour_num}: "))
        neighbour_id = "node" + str(neighbour_num)
        node.neighbours.append((neighbour_id, cost))

        # Ask for classroom information between this node and its neighbor
        classroom_info = json.loads(input(f"Enter classroom information (as JSON) between {node.id} and {neighbour_id}: "))

        # Store classroom information for this specific neighbor
        node.classroom_info[neighbour_id] = classroom_info

    # Add node to the database
    add_node(node)
