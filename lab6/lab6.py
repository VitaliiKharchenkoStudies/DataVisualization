import os
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque
def build_graph(directory, max_depth=None):
    graph = nx.DiGraph()
    color_map = {}
    stack = deque([(directory, 0)])

    while stack:
        current_path, level = stack.pop()
        if max_depth is not None and level > max_depth:
            continue

        current_name = os.path.basename(current_path)
        graph.add_node(current_path, label=current_name, level=level)

        # Генерація кольору для кожного рівня
        if level not in color_map:
            color_map[level] = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        if os.path.isdir(current_path):
            try:
                for item in os.listdir(current_path):
                    item_path = os.path.join(current_path, item)
                    graph.add_edge(current_path, item_path)
                    stack.append((item_path, level + 1))
            except OSError:  # Handle permission issues
                continue

    return graph, color_map

root_directory = "E:/projects/DeviceTemplateEditor/trunk/src/UI/images/"
max_depth = 5

# Побудова графа
G, color_map = build_graph(root_directory, max_depth)

# Візуалізація графа
pos = nx.spring_layout(G, iterations=200)
colors = [color_map[data['level']] for node, data in G.nodes(data=True)]

plt.figure(figsize=(10, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    labels={node: data['label'] for node, data in G.nodes(data=True)},
    node_size=500,
    node_color=colors,
    edge_color="gray",
    font_size=8,
    font_color="black",
)
plt.title("Граф структури файлів та каталогів")
plt.show()
