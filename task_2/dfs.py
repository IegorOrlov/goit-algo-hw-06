def dfs_recursive(graph: dict[str, list[str]], vertex: str, visited=None) -> list:
    if visited is None:
        visited = list()
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited
