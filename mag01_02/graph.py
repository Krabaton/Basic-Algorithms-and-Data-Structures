import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Додаємо вершини
G.add_node("Yaroslav")
G.add_node("Anatoliy")
G.add_node("Oleksandr")
G.add_node("Roman")
G.add_node("Eugene")
G.add_node("Oleksandra")
G.add_node("Miko")
G.add_node("Oleksii")
G.add_node("Sergiy")
G.add_node("Yulia")

# Додаємо з'єднання
G.add_edge("Yaroslav", "Anatoliy")
G.add_edge("Yaroslav", "Oleksandr")
G.add_edge("Yaroslav", "Sergiy")
G.add_edge("Yaroslav", "Oleksii")
G.add_edge("Yaroslav", "Eugene")
G.add_edge("Oleksandr", "Roman")
G.add_edge("Roman", "Oleksandra")
G.add_edge("Miko", "Sergiy")
G.add_edge("Sergiy", "Yulia")


# Малюємо граф
plt.figure(figsize=(6, 6))
nx.draw_networkx(G, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray')
plt.axis("off")
plt.show()
