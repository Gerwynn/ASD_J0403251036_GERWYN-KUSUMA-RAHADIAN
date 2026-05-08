#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

"""
Tugas: Konversi Adjacency Matrix menjadi Adjacency List
Analisis:
1. Matrix input berukuran 4x4, artinya terdapat 4 node (0, 1, 2, 3).
2. Jika matrix[i][j] bernilai 1, maka node i terhubung ke node j.
3. Hasil akhir akan disimpan dalam dictionary agar sesuai dengan format Praktikum 2.
"""

def createGraphFromMatrix(matrix):
    # Menentukan jumlah node berdasarkan panjang baris matrix
    V = len(matrix)
    
    # Inisialisasi dictionary kosong untuk setiap node (0, 1, 2, 3)
    adj = {i: [] for i in range(V)}

    # Melakukan perulangan untuk mengecek setiap sel di dalam matrix
    for i in range(V):         # Baris (Node Asal)
        for j in range(V):     # Kolom (Node Tujuan)
            
            # Jika ditemukan angka 1, masukkan indeks kolom (j) ke list node asal (i)
            if matrix[i][j] == 1:
                adj[i].append(j)
                
    return adj

if __name__ == "__main__":
    # Definisi Adjacency Matrix dari soal
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    # Memproses konversi matrix menjadi adjacency list
    adj = createGraphFromMatrix(matrix)

    print("Adjacency List Representation (Hasil Konversi):")
    # Menggunakan logika perulangan yang sama dengan Praktikum 2
    for i in adj:
        # Mencetak Nama Node
        print(f"{i}:", end=" ")
        
        # Mencetak semua tetangga dalam satu baris (tanpa kurung siku)
        for j in adj[i]:
            print(j, end=" ")
            
        # Pindah ke baris baru setelah semua tetangga node i selesai dicetak
        print()