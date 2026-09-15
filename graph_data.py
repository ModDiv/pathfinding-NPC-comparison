"""
graph_data.py
Representasi state space untuk kasus: NPC Pathfinding pada Permainan.

GRAPH   : adjacency list {node: {tetangga: cost, ...}, ...} -> graph tak berarah
COORDS  : koordinat (x, y) tiap node, dipakai untuk menghitung heuristic pada A*
START   : initial state
GOAL    : goal state
"""

GRAPH = {
    "Spawn":           {"LorongUtara": 4, "LorongSelatan": 3},
    "LorongUtara":     {"Spawn": 4, "Perpustakaan": 5, "AulaUtama": 6},
    "LorongSelatan":   {"Spawn": 3, "GudangSenjata": 4, "AulaUtama": 7},
    "Perpustakaan":    {"LorongUtara": 5, "JembatanGantung": 3},
    "AulaUtama":       {"LorongUtara": 6, "LorongSelatan": 7, "JembatanGantung": 2, "MenaraPengawas": 5},
    "GudangSenjata":   {"LorongSelatan": 4, "MenaraPengawas": 6},
    "JembatanGantung": {"Perpustakaan": 3, "AulaUtama": 2, "RuangRahasia": 4},
    "MenaraPengawas":  {"AulaUtama": 5, "GudangSenjata": 6, "RuangRahasia": 3, "RuangBos": 8},
    "RuangRahasia":    {"JembatanGantung": 4, "MenaraPengawas": 3, "RuangBos": 5},
    "RuangBos":        {"RuangRahasia": 5, "MenaraPengawas": 8},
}

COORDS = {
    "Spawn": (0, 0),
    "LorongUtara": (1, 2),
    "LorongSelatan": (1, -2),
    "Perpustakaan": (3, 3),
    "AulaUtama": (3, 1),
    "GudangSenjata": (3, -3),
    "JembatanGantung": (5, 2),
    "MenaraPengawas": (5, -1),
    "RuangRahasia": (7, 1),
    "RuangBos": (9, 0),
}

START = "Spawn"
GOAL = "RuangBos"


def copy_graph_with_modified_costs(modifications):
    """
    Membuat salinan GRAPH dengan beberapa cost edge diubah.
    modifications: list of (node_a, node_b, new_cost)
    Dipakai untuk Eksperimen 2 (Perubahan Path Cost).
    """
    import copy
    new_graph = copy.deepcopy(GRAPH)
    for a, b, new_cost in modifications:
        new_graph[a][b] = new_cost
        new_graph[b][a] = new_cost
    return new_graph
