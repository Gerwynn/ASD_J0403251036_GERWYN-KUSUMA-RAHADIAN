#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
# Praktikum 13 - Graph III: Spanning Tree
#=======================================================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki banyak kemungkinan jalur yang saling terhubung dan sering kali mengandung cycle. Sedangkan spanning tree adalah subgraph dari graph tersebut yang menghubungkan seluruh node tetapi sama sekali tidak memiliki cycle.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Dalam spanning tree, cycle dihindari karena akan menyebabkan penggunaan edge berlebih. Hal ini membuat koneksi menjadi tidak efisien dan pada akhirnya akan meningkatkan biaya total secara keseluruhan.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree membatasi jumlah edge pada titik paling minimum yang dibutuhkan untuk menghubungkan semua node tanpa membentuk cycle. Tepatnya, jumlah edge pada spanning tree selalu sebanyak jumlah node dikurangi satu.