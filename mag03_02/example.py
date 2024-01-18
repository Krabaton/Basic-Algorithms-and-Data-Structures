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

print(G.nodes())
print(G.edges())
print(list(G.neighbors("B")))
print(G.number_of_nodes())
print(G.number_of_edges())

print(nx.degree_centrality(G))
print(nx.betweenness_centrality(G))
print(nx.closeness_centrality(G))


if __name__ == '__main__':

    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=16, font_weight="bold")
    plt.show()
