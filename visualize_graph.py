"""
visualize_graph.py
Visualisasi state space (graph) dan solution path tiap algoritma
untuk kasus NPC Pathfinding, menggunakan networkx + matplotlib.

Menghasilkan 2 gambar:
    1. graph_overview.png   -> graph lengkap dengan cost tiap edge, Start & Goal ditandai
    2. solution_paths.png   -> 4 subplot: jalur solusi BFS, DFS, UCS, A* disorot warna merah
"""

import matplotlib
matplotlib.use("Agg")  # render tanpa display (headless)
import matplotlib.pyplot as plt
import networkx as nx

from graph_data import GRAPH, COORDS, START, GOAL
from search_algorithms import bfs, dfs, ucs, a_star
from heuristic import heuristic


def build_networkx_graph():
    G = nx.Graph()
    for node, neighbors in GRAPH.items():
        G.add_node(node)
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)
    return G


def node_colors(G, highlight_start_goal=True):
    colors = []
    for node in G.nodes():
        if highlight_start_goal and node == START:
            colors.append("#4CAF50")   # hijau untuk Start
        elif highlight_start_goal and node == GOAL:
            colors.append("#F44336")   # merah untuk Goal
        else:
            colors.append("#90CAF9")   # biru muda untuk node lain
    return colors


def draw_graph_overview():
    G = build_networkx_graph()
    pos = COORDS

    plt.figure(figsize=(10, 7))
    nx.draw_networkx_nodes(G, pos, node_color=node_colors(G), node_size=1600, edgecolors="black")
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")
    nx.draw_networkx_edges(G, pos, width=1.5, edge_color="gray")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color="darkred")

    plt.title("State Space — NPC Pathfinding (Spawn -> RuangBos)", fontsize=13, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("graph_overview.png", dpi=150)
    plt.close()
    print("Tersimpan: graph_overview.png")


def draw_solution_paths():
    G = build_networkx_graph()
    pos = COORDS

    results = {
        "BFS": bfs(GRAPH, START, GOAL),
        "DFS": dfs(GRAPH, START, GOAL),
        "UCS": ucs(GRAPH, START, GOAL),
        "A*": a_star(GRAPH, START, GOAL, heuristic),
    }

    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    axes = axes.flatten()

    for ax, (name, result) in zip(axes, results.items()):
        path = result["path"]
        path_edges = list(zip(path, path[1:])) if path else []

        # gambar semua node & edge dengan warna netral
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors(G, highlight_start_goal=False),
                                node_size=1000, edgecolors="black")
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=7)
        nx.draw_networkx_edges(G, pos, ax=ax, width=1, edge_color="lightgray")

        # sorot node & edge yang termasuk solution path
        nx.draw_networkx_nodes(G, pos, nodelist=path, ax=ax, node_color="#FFD54F",
                                node_size=1000, edgecolors="black")
        nx.draw_networkx_nodes(G, pos, nodelist=[START], ax=ax, node_color="#4CAF50", node_size=1000, edgecolors="black")
        nx.draw_networkx_nodes(G, pos, nodelist=[GOAL], ax=ax, node_color="#F44336", node_size=1000, edgecolors="black")
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, ax=ax, width=3, edge_color="#E53935")

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_size=6, font_color="dimgray")

        ax.set_title(f"{name}  (cost={result['cost']}, steps={result['steps']}, expanded={result['expanded_nodes']})",
                     fontsize=11, fontweight="bold")
        ax.axis("off")

    plt.suptitle("Perbandingan Solution Path: BFS vs DFS vs UCS vs A*", fontsize=15, fontweight="bold")
    plt.tight_layout()
    plt.savefig("solution_paths.png", dpi=150)
    plt.close()
    print("Tersimpan: solution_paths.png")


if __name__ == "__main__":
    draw_graph_overview()
    draw_solution_paths()
