#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
# Praktikum 13 - Graph III: Spanning Tree
#=======================================================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    
    # Masukkan edge dari node awal ke dalam priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan belum dikunjungi, tambahkan ke MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Masukkan edge tetangga dari node yang baru dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# ==========================================
# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan pada implementasi ini adalah node 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge yang dipilih pertama kali adalah ('A', 'C') dengan bobot 2.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Algoritma Prim mencari edge dengan bobot paling kecil dari kumpulan edge yang terhubung dengan node-node yang sudah dikunjungi (berada di dalam MST), yang mengarah ke node yang belum dikunjungi.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST yang dihasilkan adalah 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Kruskal berfokus secara global, yaitu memilih edge dengan bobot terkecil dari seluruh graph selama tidak membentuk cycle. Sedangkan Prim berfokus pada node, yaitu membangun tree secara bertahap dan terus melebar dari satu node awal ke node-node tetangganya.