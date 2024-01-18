import matplotlib.pyplot as plt
import networkx as nx

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"],
}

G = nx.Graph(graph)

plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=16, font_weight="bold")
plt.show()
