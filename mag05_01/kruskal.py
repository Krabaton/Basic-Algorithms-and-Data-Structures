import networkx as nx
import matplotlib.pyplot as plt


# Функція для побудови Мінімального Остовного Дерева за алгоритмом Краскала
def kruskal_mst(graph):
    # Створюємо ліс, кожне дерево якого є окремою вершиною графа
    forest = nx.Graph()
    for node in graph.nodes():
        forest.add_node(node)

    # Сортування ребер графа за вагою в порядку зростання
    sorted_edges = sorted(graph.edges(data=True), key=lambda t: t[2].get('weight', 1))

    # Мінімальне остовне дерево
    mst = nx.Graph()

    # Додаємо ребра до МОД з урахуванням того, що додавання ребра не формує циклу
    for edge in sorted_edges:
        u, v, weight = edge
        # Якщо u та v знаходяться в різних компонентах зв'язності, додаємо ребро
        if not nx.has_path(forest, u, v):
            forest.add_edge(u, v)
            mst.add_edge(u, v, weight=weight['weight'])

    return mst


if __name__ == '__main__':
    # Створення зваженого графа
    G = nx.Graph()
    G.add_edge('A', 'B', weight=7)
    G.add_edge('A', 'D', weight=5)
    G.add_edge('B', 'C', weight=8)
    G.add_edge('B', 'D', weight=9)
    G.add_edge('B', 'E', weight=7)
    G.add_edge('C', 'E', weight=5)
    G.add_edge('D', 'E', weight=15)
    G.add_edge('D', 'F', weight=6)
    G.add_edge('E', 'F', weight=8)
    G.add_edge('E', 'G', weight=9)
    G.add_edge('F', 'G', weight=11)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    # Побудова мінімального остовного дерева за допомогою алгоритму Краскала
    mst = kruskal_mst(G)

    # Вивід ребер МОД
    print("Edges in the MST:")
    for edge in mst.edges(data=True):
        print(edge)

    # Візуалізація
    # pos = nx.spring_layout(mst, seed=42)
    nx.draw(mst, pos, with_labels=True)
    labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    plt.show()
