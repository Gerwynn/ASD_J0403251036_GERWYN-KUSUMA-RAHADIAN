#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ==================================================================================================================
# Latihan 1: Rekursi Pangkat
# Diskusi dan jelaskan alur program serta base case dan recursive call.
# ==================================================================================================================
def pangkat(a, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16

# Penjelasan:
# Alur program:
# 1. Fungsi pangkat dipanggil dengan a=2 dan n=4
# 2. Karena n tidak sama dengan 0, fungsi akan memanggil dirinya sendiri dengan n dikurangi 1 (n=3)
# 3. Proses ini berlanjut hingga n mencapai 0, di mana fungsi akan mengembalikan 1 (base case)
# 4. Setelah mencapai base case, fungsi akan kembali ke panggilan sebelumnya dan mengalikan hasil perkalian a dengan hasil dari pangkat(a, n-1) untuk setiap langkah
# 5. Akhirnya, hasil akhir dari pangkat(2, 4) akan dihitung sebagai 2 * 2 * 2 * 2 = 16