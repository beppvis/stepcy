import networkx as nx                                   #node, cost between nodes
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
ply.show()