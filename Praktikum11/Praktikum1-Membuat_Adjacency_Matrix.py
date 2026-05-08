#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

"""
1. vertex = [0, 1, 2, 3]
2. edge = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 3), (3,2)]
"""
"""
1. Jenis graph tersebut adalah undirected graph, karena tidak terdapat panah yang menunjukkan arah pada edge-nya.
2. Graph tersebut memiliki 4 vertex (0, 1, 2, 3) dan 8 edge yang menghubungkan vertex-vertex tersebut.
3. 0 terhubung dengan 1 dan 2
4. 1 terhubung dengan 0 dan 2
5. 2 terhubung dengan 0, 1, dan 3
6. 3 terhubung dengan 2
"""

def createGraph(V, edges):
    # Membuat matriks 2D berukuran V x V (4x4) yang nilai awalnya diisi 0 (asumsi awal tidak ada koneksi)
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Membaca setiap pasangan sisi (edge) untuk memetakan koneksi ke dalam matriks
    for it in edges:
        u = it[0] # Vertex asal
        v = it[1] # Vertex tujuan
        
        # Menandai adanya koneksi antara vertex u dan v dengan angka 1
        mat[u][v] = 1

        # Memastikan relasi sebaliknya (v ke u) juga bernilai 1 karena graf bersifat undirected
        mat[v][u] = 1
        
    return mat

if __name__ == "__main__":
    V = 4
    
    # Daftar relasi antar vertex. Relasi bolak-balik sudah didefinisikan langsung di dalam list
    edges = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 3), (3, 2)]

    # Memproses pembentukan adjacency matrix
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    
    # Melakukan perulangan untuk menampilkan matriks dalam format grid (baris x kolom)
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        
        print()