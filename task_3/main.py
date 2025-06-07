import json
import networkx as nx
from dijkstra import dijkstra

__START_STATION__ = "Хрещатик"


def load_graph() -> dict[str, dict[str, float]]:
    with open("kyiv_subway.json", "r", encoding="utf-8") as f:
        metro_data = json.load(f)

    G = nx.Graph()
    G.add_weighted_edges_from(metro_data, weight="time")

    graph = {}
    for u, v, data in G.edges(data=True):
        time = data.get("time")
        graph.setdefault(u, {})[v] = time
        graph.setdefault(v, {})[u] = time
    return graph


graph = load_graph()
distances = dijkstra(graph, __START_STATION__)

sorted_distances = sorted(distances.items(), key=lambda x: x[1], reverse=True)

print(f"Відстань у хвилинах від станції '{__START_STATION__}' у київського метро до:")
for station, distance in sorted_distances:
    print(f"{station}: {distance:.0f} хвилин")
