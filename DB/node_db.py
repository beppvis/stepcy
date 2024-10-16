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

# N = int(input("Enter no of nodes : "))
# nodes = []

# for i in range(1,N+1):
#     nodeID = "node"+str(i)
#     node = Node(nodeID)     
#     nodes.append(node)

# for node in nodes:
#     print(node.id +" connectections : ")
#     neighour_nums = int(input("Enter num of neighbour connections : "))

#     for i in range(1,neighour_nums + 1):
#         neighbour_num = int(input("Enter neighbour num  : "))
#         cost = int(input("Enter cost to neighbour {} to {}: ".format(node.id,neighbour_num)))
#         neighbour_id = "node"+str(neighbour_num)
#         node.neighbours.append((neighbour_id,cost))
#     add_node(node)

def get_data_all():
    try :
        cnt = sqlite3.connect(database)
        cur = cnt.cursor()     
        cur = cur.execute("select * from floor1;")
        vals = cur.fetchall()
        data = []
        for row in vals:
            node_id = row[0]
            neighbour_data = json.loads(row[1])
            neighbours = []
            # TODO :vals are not used currenlty need to be implemented
            for (key,val) in neighbour_data.items():
                n_data = {}
                n_data[key] = val
                neighbours.append(n_data)
            # print(neighbours)
            data.append((node_id,neighbours))
        return data

    except sqlite3.Error as error:
        print("sqlite error : ",error)

    finally:
        if cnt:
            cnt.close()

# To create a base template for easy addition
def gen_json_file():
    f = open("floor1.json","w")
    N = int(input("Num of nodes : "))
    floor_dict = {}
    i = 1

    while i <= N:
        node_id = "node" + str(i)
        floor_dict[node_id]={}
        floor_dict[node_id]["neighbours"]={}
        n = int(input("Enter no of neighbours : "))
        for x in range(1,1+n):
            y = int(input("Enter neighbour : "))
            neighbour_id = "node"+ str(y)
            floor_dict[node_id]["neighbours"][neighbour_id] ={}
            floor_dict[node_id]["neighbours"][neighbour_id]["cost"] = 0
            floor_dict[node_id]["neighbours"][neighbour_id]["classes"] = []
            floor_dict[node_id]["neighbours"][neighbour_id]["angle"] = 90 
        i+=1
    
    json.dump(floor_dict,f)
    
# json_ to sql        

def json_to_sql(file_path:str):
    file = open(file_path)
    data = json.load(file)
    for (key,val) in data.items():
        try :
            cnt = sqlite3.connect(database)
            cur = cnt.cursor()     
            neighbours = val["neighbours"]
            node_neighbour_str = json.dumps(neighbours)
            print(node_neighbour_str)
            query = '''insert into {} values('{}','{}')'''.format(table_name,key,node_neighbour_str)        
            print(query)
            cur.execute(query)

        except sqlite3.Error as error:
            print("Sqlite error : ",error)

        finally:
            if cnt:
                cnt.commit()
                cnt.close()
    
def create_table(table_name : str,database_path:str):
    try: 
        cnt = sqlite3.connect(database_path)
        cur = cnt.cursor()
        query = "create table "+table_name + "(node_id string,neighbour_data string);"
        cur.execute(query)
    except sqlite3.Error as error:
        print("Sqlite error : ",error)
    finally:
        if cnt:
            cur.close()
            cnt.commit()
            cnt.close()

if __name__ =="__main__":
    gen_json_file()
