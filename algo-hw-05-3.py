import networkx as nx
import matplotlib.pyplot as plt

# Створення графа для моделювання топології Інтернету
# Граф зі 100 вершинами, побудований за моделлю Барбаші-Альберт
G = nx.scale_free_graph(100)

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Розташування вершин
nx.draw(G, pos, node_size=50, node_color="skyblue",
        edge_color="gray", with_labels=False)
plt.title("Топологія Інтернету (Scale-Free Graph)", fontsize=14)
plt.show()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = [deg for _, deg in G.degree()]

{
    "Кількість вершин": num_nodes,
    "Кількість ребер": num_edges,
    "Середній ступінь вершини": sum(degrees) / len(degrees),
    "Максимальний ступінь вершини": max(degrees),
    "Мінімальний ступінь вершини": min(degrees),
}
