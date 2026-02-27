#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Latihan 4: Kombinasi Huruf
# Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.
# ======================================================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return

    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)

# Penjelasan:
# Fungsi kombinasi menghasilkan semua kombinasi huruf 'A' dan 'B' dengan panjang n. Setiap kali fungsi dipanggil, ia menambahkan 'A' atau 'B' ke hasil saat ini dan memanggil dirinya sendiri hingga panjang hasil mencapai n. Untuk n=2, kombinasi yang dihasilkan adalah:
# 1. AA
# 2. AB
# 3. BA
# 4. BB
# Jadi, total kombinasi yang dihasilkan untuk n=2 adalah 4. Secara umum, untuk n huruf, jumlah kombinasi yang dihasilkan adalah 2^n, karenasetiap posisi dapat diisi dengan 2 pilihan (A atau B).