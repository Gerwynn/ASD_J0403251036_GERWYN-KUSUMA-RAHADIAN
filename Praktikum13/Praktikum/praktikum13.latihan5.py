#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
# Praktikum 13 - Graph III: Spanning Tree
#=======================================================================================

# ==========================================================
# Latihan 5: Tugas Mandiri: Buat Program MST dengan Kasus Baru
# Kasus Pilihan: Kasus 2 (Jaringan Komputer)
# Algoritma: Kruskal
# ==========================================================

# 1. Representasi weighted graph dalam bentuk list of edges 
# Format: (bobot, 'Router 1', 'Router 2')
edges = [
    (3, 'Router A', 'Router B'),
    (2, 'Router A', 'Router C'),
    (5, 'Router B', 'Router D'),
    (1, 'Router C', 'Router D'),
    (4, 'Router B', 'Router C')
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
print("Minimum Spanning Tree (Jaringan Komputer Terpilih):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} (Bobot: {edge[2]})")

# 4. Output total bobot minimum
print("\nTotal bobot minimum =", total_bobot)

# ==========================================
# 5. Komentar penjelasan program (Jawaban Analisis):
# 1. Kasus apa yang dipilih?
#    Kasus 2. Jaringan Komputer.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal. Algoritma ini digunakan karena list koneksi jaringan router sangat mudah direpresentasikan dalam bentuk edge list dan diurutkan bobotnya.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    Edge yang dipilih adalah:
#    - Router C - Router D (Bobot: 1)
#    - Router A - Router C (Bobot: 2)
#    - Router A - Router B (Bobot: 3)
#
# 4. Berapa total bobot MST?
#    Total bobot MST adalah 6.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Edge Router B - Router C (bobot 4) dan Router B - Router D (bobot 5) tidak dipilih karena keempat router (A, B, C, D) tersebut sudah saling terhubung melalui jalur yang lebih murah. Jika edge tersebut ditambahkan, maka akan membentuk putaran (cycle) dan mengakibatkan pemborosan resource.