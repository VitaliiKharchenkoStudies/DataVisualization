# Лабораторна робота №5 з предмету Data Visualization
**Виконав**: Харченко Віталій Андрійович,  
**Група**: ІКМ-М223б

---

У цій лабораторній роботі ми вивчаємо візуалізацію бінарних дерев та створюємо граф за допомогою бібліотеки `networkx`. Розглянемо код з поясненням кожної частини.

---

### Імпорт бібліотек
```
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
```

### Бінарне дерево
- **Клас `TreeNode`**:
  ```
  class TreeNode:
      def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None
  ```
  - Визначаємо бінарне дерево з коренем, який може мати лівого та правого дітей.
- **Додавання вузла**:
  ```
  def add_node(root, value):
      if value < root.value:
          if root.left is None:
              root.left = TreeNode(value)
          else:
              add_node(root.left, value)
      else:
          if root.right is None:
              root.right = TreeNode(value)
          else:
              add_node(root.right, value)
  ```
  - Додаємо новий вузол до бінарного дерева.
  - Якщо значення менше кореневого, додаємо в ліве піддерево, якщо більше або рівне — в праве.

---

### Побудова графа з бінарного дерева
- **Функція `build_graph`**:
  ```
  def build_graph(root):
      graph = nx.DiGraph()
      positions = {}

      def recurse(node, x=0, y=0, level=0):
          if node:
              graph.add_node(node)
              positions[node] = (x, y)

              if node.left:
                  graph.add_edge(node, node.left)
                  recurse(node.left, x - 1 / 2 ** (level + 1), y - 1, level + 1)

              if node.right:
                  graph.add_edge(node, node.right)
                  recurse(node.right, x + 1 / 2 ** (level + 1), y - 1, level + 1)

      recurse(root)
      return graph, positions
  ```
  - Створює граф та позиції вузлів на основі бінарного дерева.
  - Рекурсивно додає вузли та встановлює позиції.
  - Якщо є лівий підвузол, додаємо ребро до нього, рухаємося ліворуч. Якщо правий — рухаємося праворуч.

---

### Створення дерева та його візуалізація
- **Корінь дерева**:
  ```
  root = TreeNode(np.random.uniform(-1, 1))
  ```
  - Створюємо корінь із випадковим значенням.
- **Додавання кількох вузлів**:
  ```
  for _ in range(15):
      value = np.random.uniform(-1, 1)
      add_node(root, value)
  ```
  - Додаємо 15 випадкових вузлів до дерева.
- **Побудова графа та позицій**:
  ```
  G, pos = build_graph(root)
  ```
  - Створюємо граф та позиції на основі бінарного дерева.
- **Візуалізація бінарного дерева**:
  ```
  plt.figure(figsize=(10, 8))
  nx.draw(G, pos, with_labels=True, labels={node: f"{node.value:.2f}" for node in G.nodes}, node_size=700, node_color='lightblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray')
  plt.title("Візуалізація бінарного дерева")
  plt.show()
  ```
  - Візуалізуємо граф із використанням `networkx`.
  - Відображаємо значення вузлів, встановлюємо розмір і колір вузлів, а також кольори ребер.
  - Показуємо граф із підписаними вузлами та заголовком.

---

![alt graph](https://media.discordapp.net/attachments/917547349864230912/1233887493305401474/image.png?ex=662ebac6&is=662d6946&hm=deaf1a30203b4566a38d8c4a63ae22acdf88dd64eafc8082fa56ec81ab62d4eb&=&format=webp&quality=lossless&width=438&height=350)