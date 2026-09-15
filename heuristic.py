"""
heuristic.py
Fungsi heuristic untuk A* pada kasus NPC Pathfinding.

Heuristic default: Euclidean distance antara koordinat node saat ini dan koordinat goal.
Heuristic ini admissible selama tidak ada jalur yang lebih pendek dari garis lurus
antara dua titik (berlaku di sini karena cost edge >= jarak Euclidean-nya).
"""

import math
from graph_data import COORDS


def heuristic(node, goal):
    """Euclidean distance dari `node` ke `goal` berdasarkan koordinat pada COORDS."""
    x1, y1 = COORDS[node]
    x2, y2 = COORDS[goal]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def heuristic_manhattan(node, goal):
    """Alternatif heuristic: Manhattan distance. Dipakai pada Eksperimen 3."""
    x1, y1 = COORDS[node]
    x2, y2 = COORDS[goal]
    return abs(x1 - x2) + abs(y1 - y2)


def heuristic_zero(node, goal):
    """Heuristic h(n) = 0 untuk semua node -> A* akan berperilaku seperti UCS.
    Berguna sebagai pembanding pada Eksperimen 3."""
    return 0


def heuristic_inflated(node, goal, factor=3):
    """Heuristic tidak admissible (dikalikan faktor tertentu) untuk menunjukkan
    dampak heuristic yang melebih-lebihkan (overestimate) pada Eksperimen 3."""
    return heuristic(node, goal) * factor
