import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання міст і доріг
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=2)
G.add_edge('C', 'B', weight=4)
G.add_edge('D', 'E', weight=4)

short_paths = nx.single_source_dijkstra_path(G, 'A')
print(short_paths)
length_path = nx.single_source_dijkstra_path_length(G, 'A')
print(length_path)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()