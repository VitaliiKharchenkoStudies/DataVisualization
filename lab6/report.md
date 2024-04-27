# Лабораторна робота №6 з предмету Data Visualization
**Виконав**: Харченко Віталій Андрійович,  
**Група**: ІКМ-М223б

---

У цій лабораторній роботі ми створюємо граф структури файлів та каталогів з використанням бібліотеки `networkx`. Для візуалізації графа враховуємо різні кольори для різних рівнів, а також обмежуємо глибину для уникнення надмірного навантаження. Нижче наведено опис коду з поясненнями.

---

### Імпорт бібліотек
```
import os
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque
```
- **`os`**: Для роботи з файловою системою.
- **`networkx`**: Для створення графа та його візуалізації.
- **`matplotlib.pyplot`**: Для побудови графіків.
- **`random`**: Для генерації випадкових кольорів.
- **`deque`**: Для ітеративного обходу структури каталогів.

---

### Функція для побудови графа структури файлів та каталогів
```
def build_graph(directory, max_depth=None):
    graph = nx.DiGraph()
    color_map = {}
    stack = deque([(directory, 0)])

    while stack:
        current_path, level = stack.pop()

        # Обмеження на глибину
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
            except OSError:  # Обробка помилок дозволів
                continue

    return graph, color_map
```
- **Ітеративний підхід**: Використовуємо стек для обходу структури каталогів без рекурсії.
- **Обмеження глибини**: Параметр `max_depth` обмежує кількість рівнів для побудови графа.
- **Генерація кольору для кожного рівня**: Створюємо кольорову мапу, щоб різні рівні мали різні кольори.
- **Обробка помилок**: Враховуємо можливі помилки дозволів (permission issues).

---

### Побудова графа та візуалізація
```
root_directory = "E:/projects/DeviceTemplateEditor/trunk/src/UI/images/"  # Вкажіть свій кореневий каталог
max_depth = 5  # Обмеження глибини

G, color_map = build_graph(root_directory, max_depth)

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
```
- **Кореневий каталог**: Вкажіть шлях до свого вихідного каталогу.
- **Обмеження глибини**: Параметр `max_depth` контролює глибину, щоб уникнути надмірного навантаження.
- **Побудова графа**: Створюємо граф на основі структури каталогів.
- **Візуалізація**: Встановлюємо різні кольори для різних рівнів та візуалізуємо граф за допомогою `nx.draw`.
- **Налаштування графіка**: Встановлюємо розмір вузлів, кольори, підписи та інші параметри.

---

### Зображення графів


- Маємо 3 зображення з різними глубинами обходу

![alt graph](https://media.discordapp.net/attachments/917547349864230912/1233892467716264016/image.png?ex=662ebf68&is=662d6de8&hm=9b167b0e0331e09665019f59d0406a4d266bb7f08df6f1e208b9ccb346cfe6d7&=&format=webp&quality=lossless&width=839&height=671)
![alt graph](https://media.discordapp.net/attachments/917547349864230912/1233892468584353987/image.png?ex=662ebf69&is=662d6de9&hm=76835a1c61824049175b715fd79719fdf4daa22958316aa2d9503f1a4b426297&=&format=webp&quality=lossless&width=839&height=671)
![alt graph](https://media.discordapp.net/attachments/917547349864230912/1233892468156661851/image.png?ex=662ebf69&is=662d6de9&hm=3950f157fbe66d1f27dfe3c45c2a4d26f0b44f63ad7549ec18f269ca8abb3d62&=&format=webp&quality=lossless&width=839&height=671)