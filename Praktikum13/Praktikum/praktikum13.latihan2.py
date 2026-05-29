#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
# Praktikum 13 - Graph III: Spanning Tree
#=======================================================================================

# ==========================================================
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Edge yang dipilih pertama kali adalah ('C', 'D') dengan bobot 1 (bobot terkecil).
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena algoritma Kruskal merupakan algoritma Minimum Spanning Tree (MST) yang memang bekerja dengan cara memilih edge dengan bobot paling kecil terlebih dahulu. Pemilihan ini dilakukan secara bertahap agar total akhirnya minimum.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST yang dihasilkan adalah 6. (Hasil penjumlahan dari edge berbobot 1, 2, dan 3).
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge tertentu diabaikan atau tidak dipilih karena jika edge tersebut ditambahkan ke dalam MST, ia akan membentuk cycle (siklus) pada graph.