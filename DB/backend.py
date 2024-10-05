import networkx as nx
import matplotlib.pyplot as ply
G = nx.Graph()
edge=[(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(2,8),(6,9),(3,10),(4,11),(1,7)]
G.add_edges_from(edge)
distances={(1,2):10,(2,3):3,(3,4):9,(4,5):6,(5,6):7,(6,7):4,(2,8):8,(6,9):5,(3,10):11,(4,11):9,(1,7):2}
nx.set_edge_attributes(G,distances,'weight')
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size= 1000, node_color='red',node_shape='o')
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
print(nx.shortest_path(G,1,5,'weight'))
ply.show()


