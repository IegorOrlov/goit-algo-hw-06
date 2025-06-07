from collections import deque


def bfs_iterative(graph: dict[str, list[str]], start: str) -> list:
    visited = list()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(graph[vertex]).difference(visited))
    return visited
