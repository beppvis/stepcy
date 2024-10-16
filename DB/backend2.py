import networkx as nx
import matplotlib.pyplot as ply
import node_db
import json

# Input nodes
# nodea = input("Enter starting node: ")
# nodeb = input("Enter end node: ")
# nodea = "node" + nodea
# nodeb = "node" + nodeb

# Create a directed graph to show arrows for direction
def get_shortest_path(nodea,nodeb):
    G = nx.DiGraph()
    L = []
    edges = []
    distances = {}

    # Get data from node_db
    data = node_db.get_data_all()   
    for record in data:
        node_id = record[0]
        try : 
            for neighbour in record[1]:
                for neighbour_id ,neighbour_data in neighbour.items():
                        edges.append((node_id, neighbour_id))
                        distances[(node_id, neighbour_id)] = neighbour_data["cost"]
        except:
            print("DB data parsing error")

    # print(edges)
    # print(distances)

    # Add edges to the graph and set their weights
    G.add_edges_from(edges)
    nx.set_edge_attributes(G, distances, 'weight')

    # Find the shortest path
    shortest_path = nx.shortest_path(G, nodea, nodeb, 'weight')

    print("BACKEND 2 : Shortest path: ", shortest_path)
    # DEBUGING : for debugging purposes 

    # if __name__ == "__main__":
    #     pos=nx.spring_layout(G)

    #     # Draw the graph nodes and edges
    #     nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='red', node_shape='o')
    #     nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20)
    #     nx.draw_networkx_labels(G, pos)

    #     # Highlight the shortest path
    #     path_edges = list(zip(shortest_path, shortest_path[1:]))
    #     nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', arrows=True, arrowsize=25)

    #     # Display the graph
    #     ply.show()

    return shortest_path

# if __name__=="__main__":
#     get_shortest_path("node1","node2")
