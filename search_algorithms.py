"""
search_algorithms.py
Implementasi BFS, DFS, UCS, dan A* untuk kasus NPC Pathfinding.

Setiap fungsi mengembalikan dict berisi:
    expansion_order : urutan node yang diekspansi (dipilih & diperiksa)
    path            : solution path dari start ke goal (None jika tidak ditemukan)
    steps           : jumlah langkah (jumlah edge pada solution path)
    cost            : total path cost dari solution path
    expanded_nodes  : jumlah node yang diekspansi
"""

from collections import deque
import heapq


def _reconstruct_path(parent, node):
    path = [node]
    while parent[node] is not None:
        node = parent[node]
        path.append(node)
    path.reverse()
    return path


def _path_cost(graph, path):
    if not path or len(path) < 2:
        return 0
    return sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))


def _empty_result():
    return {
        "expansion_order": [],
        "path": None,
        "steps": 0,
        "cost": 0,
        "expanded_nodes": 0,
    }


def bfs(graph, start, goal):
    """Breadth-First Search - ekspansi node paling dangkal terlebih dahulu (FIFO)."""
    frontier = deque([start])
    visited = {start}
    parent = {start: None}
    expansion_order = []

    while frontier:
        node = frontier.popleft()
        expansion_order.append(node)

        if node == goal:
            path = _reconstruct_path(parent, node)
            return {
                "expansion_order": expansion_order,
                "path": path,
                "steps": len(path) - 1,
                "cost": _path_cost(graph, path),
                "expanded_nodes": len(expansion_order),
            }

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                frontier.append(neighbor)

    result = _empty_result()
    result["expansion_order"] = expansion_order
    result["expanded_nodes"] = len(expansion_order)
    return result


def dfs(graph, start, goal):
    """Depth-First Search - ekspansi node terdalam terlebih dahulu (LIFO)."""
    stack = [start]
    visited = set()
    parent = {start: None}
    expansion_order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        expansion_order.append(node)

        if node == goal:
            path = _reconstruct_path(parent, node)
            return {
                "expansion_order": expansion_order,
                "path": path,
                "steps": len(path) - 1,
                "cost": _path_cost(graph, path),
                "expanded_nodes": len(expansion_order),
            }

        # reverse-sorted supaya urutan pop dari stack tetap alfabetis (deterministik)
        for neighbor in sorted(graph[node], reverse=True):
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = node
                stack.append(neighbor)

    result = _empty_result()
    result["expansion_order"] = expansion_order
    result["expanded_nodes"] = len(expansion_order)
    return result


def ucs(graph, start, goal):
    """Uniform-Cost Search - memilih node dengan path cost (g(n)) terkecil, menggunakan priority queue."""
    counter = 0  # tie-breaker agar heapq tidak membandingkan string saat cost sama
    frontier = [(0, counter, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = set()
    expansion_order = []

    while frontier:
        cost, _, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        expansion_order.append(node)

        if node == goal:
            path = _reconstruct_path(came_from, node)
            return {
                "expansion_order": expansion_order,
                "path": path,
                "steps": len(path) - 1,
                "cost": cost_so_far[goal],
                "expanded_nodes": len(expansion_order),
            }

        for neighbor, weight in graph[node].items():
            new_cost = cost_so_far[node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = node
                counter += 1
                heapq.heappush(frontier, (new_cost, counter, neighbor))

    result = _empty_result()
    result["expansion_order"] = expansion_order
    result["expanded_nodes"] = len(expansion_order)
    return result


def a_star(graph, start, goal, heuristic):
    """A* Search - f(n) = g(n) + h(n).
    Mengembalikan juga `node_values`: dict {node: (g, h, f)} untuk node yang ditemukan.
    """
    counter = 0
    h_start = heuristic(start, goal)
    frontier = [(h_start, counter, 0, start)]  # (f, tie-breaker, g, node)
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited = set()
    expansion_order = []
    node_values = {start: (0, h_start, h_start)}  # (g, h, f)

    while frontier:
        f, _, g, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        expansion_order.append(node)

        if node == goal:
            path = _reconstruct_path(came_from, node)
            return {
                "expansion_order": expansion_order,
                "path": path,
                "steps": len(path) - 1,
                "cost": cost_so_far[goal],
                "expanded_nodes": len(expansion_order),
                "node_values": node_values,
            }

        for neighbor, weight in graph[node].items():
            new_g = g + weight
            if neighbor not in cost_so_far or new_g < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_g
                h = heuristic(neighbor, goal)
                f_new = new_g + h
                came_from[neighbor] = node
                node_values[neighbor] = (new_g, h, f_new)
                counter += 1
                heapq.heappush(frontier, (f_new, counter, new_g, neighbor))

    result = _empty_result()
    result["expansion_order"] = expansion_order
    result["expanded_nodes"] = len(expansion_order)
    result["node_values"] = node_values
    return result
