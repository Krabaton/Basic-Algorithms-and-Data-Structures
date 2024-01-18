import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()
G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edge("A", "E")
G.add_edges_from([("B", "D"), ("B", "E"), ("C", "F")])
G.add_edge('B', 'F')

# G.remove_node("D")
DG = nx.DiGraph(G)
DG.remove_edge("B", "A")
DG.remove_edge("F", "C")

DG.add_node("Dima")
DG.add_edge("Dima", "A", weight=3)
DG.nodes["Dima"]["color"] = "red"
print(DG.nodes["Dima"]["color"])

print(nx.shortest_path(DG, source="Dima", target="D"))

print(DG.nodes())
print(DG.edges())
print(list(DG.neighbors("B")))
print(DG.number_of_nodes())
print(DG.number_of_edges())

print(nx.degree_centrality(DG))
print(nx.betweenness_centrality(DG))
print(nx.closeness_centrality(DG))


if __name__ == '__main__':

    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(DG, seed=42)
    nx.draw_networkx(DG, pos, with_labels=True, node_size=800, node_color="lightblue", width=1.2,  font_size=16, font_weight="light")
    plt.show()
