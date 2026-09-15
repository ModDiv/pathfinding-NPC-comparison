"""
main.py
Menjalankan BFS, DFS, UCS, dan A* pada kasus NPC Pathfinding,
lalu menjalankan 3 eksperimen sesuai ketentuan tugas:
    Eksperimen 1 - Kondisi normal
    Eksperimen 2 - Perubahan path cost
    Eksperimen 3 - Perubahan heuristic
"""

from graph_data import GRAPH, START, GOAL, copy_graph_with_modified_costs
from search_algorithms import bfs, dfs, ucs, a_star
import heuristic as H


def print_result(name, result, show_node_values=False):
    print(f"--- {name} ---")
    print(f"Initial State   : {START}")
    print(f"Goal State      : {GOAL}")
    print(f"Expansion Order : {' -> '.join(result['expansion_order'])}")
    if result["path"]:
        print(f"Solution Path   : {' -> '.join(result['path'])}")
    else:
        print("Solution Path   : TIDAK DITEMUKAN")
    print(f"Number of Steps : {result['steps']}")
    print(f"Path Cost       : {result['cost']}")
    print(f"Expanded Nodes  : {result['expanded_nodes']}")

    if show_node_values and "node_values" in result:
        print("Nilai g(n), h(n), f(n) untuk tiap node yang ditemukan:")
        for node, (g, h, f) in result["node_values"].items():
            print(f"   {node:16s} g={g:.2f}  h={h:.2f}  f={f:.2f}")
    print()


def run_all(graph, heuristic_fn, label):
    print(f"\n============================")
    print(f" {label}")
    print(f"============================\n")

    print_result("BFS", bfs(graph, START, GOAL))
    print_result("DFS", dfs(graph, START, GOAL))
    print_result("UCS", ucs(graph, START, GOAL))
    print_result("A*", a_star(graph, START, GOAL, heuristic_fn), show_node_values=True)


if __name__ == "__main__":
    # ============================================================
    # Eksperimen 1 - Kondisi Normal
    # ============================================================
    run_all(GRAPH, H.heuristic, "EKSPERIMEN 1: Kondisi Normal (Euclidean heuristic)")

    # ============================================================
    # Eksperimen 2 - Perubahan Path Cost
    # Ubah minimal 3 edge cost, lalu jalankan ulang semua algoritma.
    # ============================================================
    modified_graph = copy_graph_with_modified_costs([
        ("AulaUtama", "JembatanGantung", 9),      # semula 2 -> 9
        ("LorongSelatan", "GudangSenjata", 1),    # semula 4 -> 1
        ("MenaraPengawas", "RuangBos", 2),        # semula 8 -> 2
    ])
    run_all(modified_graph, H.heuristic, "EKSPERIMEN 2: Perubahan Path Cost (Euclidean heuristic)")

    # ============================================================
    # Eksperimen 3 - Perubahan Heuristic
    # Bandingkan Euclidean (default) vs Manhattan vs heuristic 0 (=UCS) vs inflated (tidak admissible)
    # Graph yang dipakai: graph ASLI (bukan modified_graph) agar efek heuristic murni terlihat.
    # ============================================================
    print(f"\n============================")
    print(f" EKSPERIMEN 3: Perubahan Heuristic (graph asli)")
    print(f"============================\n")

    print_result("A* dengan heuristic Euclidean (default)",
                 a_star(GRAPH, START, GOAL, H.heuristic), show_node_values=True)

    print_result("A* dengan heuristic Manhattan",
                 a_star(GRAPH, START, GOAL, H.heuristic_manhattan), show_node_values=True)

    print_result("A* dengan heuristic = 0 (setara UCS)",
                 a_star(GRAPH, START, GOAL, H.heuristic_zero), show_node_values=True)

    print_result("A* dengan heuristic inflated (x3, tidak admissible)",
                 a_star(GRAPH, START, GOAL, H.heuristic_inflated), show_node_values=True)
