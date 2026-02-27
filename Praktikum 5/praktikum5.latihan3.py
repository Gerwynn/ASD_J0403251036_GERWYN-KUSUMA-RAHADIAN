#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Latihan 3: Mencari Nilai Maksimum
# Diskusi dan jelaskan alur program serta base case dan recursive call.
# ======================================================================================
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:
        return data[index]
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# penjelasan:
# Alur program:
# 1. Fungsi cari_maks dipanggil dengan data=[3, 7, 2, 9, 5] dan index=0
# 2. Karena index tidak sama dengan len(data) - 1, fungsi akan memanggil dirinya sendiri dengan index ditambah 1 (index=1)
# 3. Proses ini berlanjut hingga index mencapai len(data) - 1, di mana fungsi akan mengembalikan nilai terakhir dalam data (base case)
# 4. Setelah mencapai base case, fungsi akan kembali ke panggilan sebelumnya dan membandingkan nilai saat ini dengan hasil dari panggilan rekursif untuk mencari nilai maksimum di antara keduanya
# 5. Akhirnya, hasil akhir dari cari_maks(angka) akan dihitung sebagai 9, yang merupakan nilai maksimum dalam daftar angka.
