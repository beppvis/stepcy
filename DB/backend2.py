'''import networkx as nx                                   #node, cost between nodes
import matplotlib.pyplot as ply
import node_db
import json
nodea=input("enter starting node:")
nodeb=input("enter end node:")
nodea = "node"+nodea
nodeb = "node"+nodeb
G = nx.Graph()
L=[]
edge=[]
distances={}
data = node_db.get_data_all()
print(data)
for record in data:
    node_id = record[0]
    print(node_id)
    L.append(node_id)
    x=json.loads(record[1])
    for key,values in x.items():
        print(f"neighbour_node: {key}, cost: {values}")
        edge.append((record[0],key))
        distances[(record[0],key)]=values
print(edge)
print(distances)
G.add_edges_from(edge)
nx.set_edge_attributes(G,distances,'weight')
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size= 1000, node_color='red',node_shape='o')
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
print(nx.shortest_path(G,nodea,nodeb,'weight'))
ply.show()'''
import networkx as nx
import matplotlib.pyplot as ply
import node_db
import json

# Input nodes
nodea = input("Enter starting node: ")
nodeb = input("Enter end node: ")
nodea = "node" + nodea
nodeb = "node" + nodeb

# Create a directed graph to show arrows for direction
G = nx.DiGraph()
L = []
edges = []
distances = {}

# Get data from node_db
data = node_db.get_data_all()   
print(data)

for record in data:
    node_id = record[0]
    print(node_id)
    L.append(node_id)
    x = json.loads(record[1])
    for key, values in x.items():
        print(f"Neighbour node: {key}, cost: {values}")
        edges.append((record[0], key))
        distances[(record[0], key)] = values

print(edges)
print(distances)

# Add edges to the graph and set their weights
G.add_edges_from(edges)
nx.set_edge_attributes(G, distances, 'weight')

# Find the shortest path
shortest_path = nx.shortest_path(G, nodea, nodeb, 'weight')
print("Shortest path: ", shortest_path)

for i in range(len(shortest_path) - 1):
    current_node = shortest_path[i]
    next_node = shortest_path[i + 1]
    if current_node < next_node:
        direction = "right"
    else:
        direction = "left"
    print(f"Move from {current_node} to {next_node}: Go {direction}")


pos=nx.spring_layout(G)

# Draw the graph nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='red', node_shape='o')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20)
nx.draw_networkx_labels(G, pos)

# Highlight the shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', arrows=True, arrowsize=25)

# Display the graph
ply.show()

