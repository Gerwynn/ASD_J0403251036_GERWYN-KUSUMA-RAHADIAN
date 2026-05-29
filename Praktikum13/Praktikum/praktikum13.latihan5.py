#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
# Praktikum 13 - Graph III: Spanning Tree
#=======================================================================================

# ==========================================================
# Latihan 5: Buat Program MST dengan Kasus Baru
# Kasus Pilihan: Kasus 1 (Jaringan Jalan Antar Kota)
# Algoritma: Kruskal
# ==========================================================

# 1. Representasi weighted graph dalam bentuk list of edges 
# Format: (bobot, 'Kota 1', 'Kota 2')
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# 2. Implementasi Kruskal
# Mengurutkan edge berdasarkan bobot jarak dari yang terpendek
edges.sort()

mst = []
total_bobot = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle (siklus)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_bobot += weight
        connected.add(u)
        connected.add(v)

# 3. Output MST
print("Minimum Spanning Tree (Jalur Antar Kota Terpilih):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} (Bobot: {edge[2]})")

# 4. Output total bobot minimum
print("\nTotal bobot minimum =", total_bobot)

# ==========================================
# 5. Komentar penjelasan program (Jawaban Analisis):
# 1. Kasus apa yang dipilih?
#    Kasus 1 (Jaringan Jalan Antar Kota).
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal. Algoritma ini dipilih karena sangat cocok dan ringkas untuk diterapkan pada representasi data edge list.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    Edge yang dipilih adalah:
#    - Bogor - Depok (Bobot: 2)
#    - Depok - Jakarta (Bobot: 3)
#    - Depok - Bandung (Bobot: 4)
#
# 4. Berapa total bobot MST?
#    Total bobot MST adalah 9.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Edge Bogor-Jakarta (bobot 5) dan Jakarta-Bandung (bobot 6) tidak dipilih karena simpul-simpul kota tersebut sudah saling terhubung (melalui kota Depok). Jika edge tersebut ditambahkan, maka akan membentuk putaran (cycle) dan menyebabkan total bobot tidak lagi minimum.