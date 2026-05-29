#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
# Praktikum 13 - Graph III: Spanning Tree
#=======================================================================================

# ==========================================================
# Studi Kasus: Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Kruskal
# ==========================================================

# 1. Representasi weighted graph dalam bentuk list of edges
# Format: (biaya, 'Gedung Asal', 'Gedung Tujuan')
edges = [
    (4, 'Gedung A', 'Gedung B'),
    (2, 'Gedung A', 'Gedung C'),
    (3, 'Gedung B', 'Gedung D'),
    (1, 'Gedung C', 'Gedung D'),
    (5, 'Gedung A', 'Gedung D')
]

# 2. Implementasi Kruskal
# Urutkan edge berdasarkan biaya pemasangan kabel dari yang termurah
edges.sort()

mst = []
total_biaya = 0
terhubung = set()

for biaya, gedung1, gedung2 in edges:
    # Cek apakah penambahan kabel ini akan membentuk cycle/putaran
    if gedung1 not in terhubung or gedung2 not in terhubung:
        mst.append((gedung1, gedung2, biaya))
        total_biaya += biaya
        terhubung.add(gedung1)
        terhubung.add(gedung2)

# 3. Output edge yang dipilih
print("Jalur Pemasangan Kabel yang Dipilih (MST):")
for jalur in mst:
    print(f"{jalur[0]} - {jalur[1]} (Biaya: {jalur[2]})")

# 4. Output total biaya minimum
print("\nTotal Biaya Minimum =", total_biaya)

# ==========================================
# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Pada program ini, digunakan Algoritma Kruskal. Algoritma ini dipilih karena mudah diimplementasikan dengan mengurutkan bobot edge (biaya kabel) dari yang terkecil.
#
# 2. Edge mana saja yang dipilih?
#    Edge yang dipilih adalah:
#    - Gedung C - Gedung D (Biaya: 1)
#    - Gedung A - Gedung C (Biaya: 2)
#    - Gedung B - Gedung D (Biaya: 3)
#
# 3. Berapa total biaya minimum?
#    Total biaya minimumnya adalah 6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    MST sangat cocok karena tujuan utama dari kasus ini adalah menghubungkan seluruh gedung di kampus (agar semua masuk dalam jaringan) dengan total biaya kabel seminimal mungkin. MST memastikan semua gedung terhubung tanpa ada pemborosan kabel akibat jalur yang membentuk siklus/putaran (cycle).