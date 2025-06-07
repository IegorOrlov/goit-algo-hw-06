import json
import networkx as nx
from dfs import dfs_recursive
from bfs import bfs_iterative

# Завантаження даних з JSON-файлу
with open("kyiv_subway.json", "r", encoding="utf-8") as f:
    metro_data = json.load(f)

# Створення графа
G = nx.Graph()
G.add_weighted_edges_from(metro_data, weight="time")
garf_dict= {node: list(neighbors) for node, neighbors in G.adj.items()}

print(f"DFS обхід графа станцій київських метро: {dfs_recursive(garf_dict,"Майдан Незалежності")}")
print(f"BFS обхід графа станцій київських метро: {bfs_iterative(garf_dict,"Майдан Незалежності")}")