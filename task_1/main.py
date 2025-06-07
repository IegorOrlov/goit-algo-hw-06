import json
import networkx as nx
import matplotlib.pyplot as plt

# Завантаження даних з JSON-файлу
with open("kyiv_subway.json", "r", encoding="utf-8") as f:
    metro_data = json.load(f)

# Створення графа
G = nx.Graph()
G.add_weighted_edges_from(metro_data, weight="time")

print(f"Кількість станцій київського метро: {G.number_of_nodes()}")
print(f"Кількість сполучень київського метро: {G.number_of_edges()}")

centrality = nx.closeness_centrality(G)

sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
print("Ступінь блискості для станцій київського метро:")
for station, score in sorted_centrality:
    print(f"{station}: {score:.4f}")

nx.draw(G, with_labels=True)
plt.show()
