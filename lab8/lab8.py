import networkx as nx
import matplotlib.pyplot as plt

gml_filename = "netscience.gml"
G = nx.read_gml(gml_filename)

print("Кількість вузлів:", len(G.nodes()))
print("Кількість зв'язків:", len(G.edges()))

plt.figure(figsize=(15, 15))
nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')
plt.title("Граф з файлу GML")
plt.show()
