

# BY KELOMPOK 3
# Anggota Kelompok :
Diva Rajestiadi			    `(11221015)`
Muhammad Haikal Ar Ridwan	 `(11221088)`
Muhammad Adzikril			    `(11251073)`
Pradifta Alfariz			    `(11251035)`
Vivian Marsyanda			    `(11231091)`

###############################################

# Source Code — Solving Problems by Searching
## Kasus: Pathfinding NPC pada Permainan

Implementasi BFS, DFS, UCS, dan A* untuk mencari rute NPC dari `Spawn` menuju `RuangBos`
di dalam peta dungeon yang dimodelkan sebagai graph (10 node, 14 edge berbobot).

###############################################

## Struktur File

| `graph_data.py` | = Menyimpan seluruh data mentah tentang masalah — graph (node & edge beserta cost), koordinat tiap node, serta titik Start dan Goal.

| Data state space (`GRAPH`, `COORDS`), `START`, `GOAL`, dan helper untuk mengubah cost edge (dipakai Eksperimen 2). |

| `heuristic.py`  = Menyediakan fungsi h(n) yang dipakai khusus oleh A* untuk menebak seberapa dekat suatu node dengan goal.

Fungsi heuristic untuk A*: `heuristic` (Euclidean, default), `heuristic_manhattan`, `heuristic_zero`, `heuristic_inflated` (dipakai Eksperimen 3). |

| `search_algorithms.py` | = Berisi implementasi keempat algoritma yang diwajibkan tugas: bfs(), dfs(), ucs(), a_star(). Ini adalah jantung dari tugas — tempat logika FIFO, LIFO, priority queue, dan f(n)=g(n)+h(n) diterapkan.

Implementasi `bfs()`, `dfs()`, `ucs()`, `a_star()`. |

| `main.py` | = Menghubungkan semua file di atas dan menjalankan seluruh skenario yang diminta tugas — ini file yang kamu jalankan (python main.py).

Menjalankan seluruh algoritma + 3 eksperimen (kondisi normal, perubahan path cost, perubahan heuristic) dan mencetak hasilnya ke terminal. |

| `visualize_graph.py` | = Membuat gambar graph dan solution path memakai matplotlib + networkx, supaya laporan punya ilustrasi visual, bukan cuma tabel angka.

Membuat visualisasi graph (`graph_overview.png`) dan perbandingan solution path tiap algoritma (`solution_paths.png`) menggunakan networkx & matplotlib. |

###############################################

## Kebutuhan Library

Untuk `main.py` (wajib): hanya modul bawaan Python — `heapq`, `collections.deque`, `math`.

Untuk `visualize_graph.py` (opsional, untuk gambar graph):
```bash
pip install matplotlib networkx
```

Membutuhkan **Python 3.8+**.

###############################################

## Cara Menjalankan

```bash
python main.py
```

Program akan mencetak ke terminal:
1. **Eksperimen 1** — hasil BFS, DFS, UCS, A* pada graph asli (Euclidean heuristic).
2. **Eksperimen 2** — hasil keempat algoritma setelah 3 edge cost diubah
   (`AulaUtama–JembatanGantung`, `LorongSelatan–GudangSenjata`, `MenaraPengawas–RuangBos`).
3. **Eksperimen 3** — hasil A* dengan 4 variasi heuristic (Euclidean, Manhattan, nol/setara UCS,
   dan heuristic "inflated" ×3 yang tidak admissible), pada graph asli.

Setiap hasil menampilkan: Initial State, Goal State, Expansion Order, Solution Path,
Number of Steps, Path Cost, Expanded Nodes — dan khusus A*, nilai g(n), h(n), f(n) tiap node.

Untuk membuat visualisasi graph & solution path:
```bash
python visualize_graph.py
```
Menghasilkan dua file gambar di folder yang sama:
- `graph_overview.png` — peta graph lengkap dengan cost tiap edge, Start (hijau) & Goal (merah).
- `solution_paths.png` — 4 subplot solution path BFS/DFS/UCS/A* (disorot kuning/merah) untuk dibandingkan visual.

###############################################


