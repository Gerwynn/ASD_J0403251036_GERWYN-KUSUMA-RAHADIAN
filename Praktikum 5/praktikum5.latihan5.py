#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Studi Kasus: Generator PIN
# Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?
# ======================================================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)
        
buat_pin(3)

"""
Penjelasan:
Fungsi buat_pin menghasilkan semua kombinasi angka '0', '1', dan '2' dengan panjang tertentu. 
Untuk mencegah angka yang sama muncul berulang, kita bisa menambahkan kondisi untuk memeriksa apakah angka
yang akan ditambahkan sudah ada dalam hasil saat ini. Misalnya, kita bisa menggunakan set untuk menyimpan 
angka yang sudah digunakan dan memeriksa sebelum menambahkan angka baru. Namun, dalam kasus ini, 
karena kita ingin menghasilkan semua kombinasi, kita tidak perlu mencegah angka yang sama muncul berulang, 
karena setiap kombinasi yang dihasilkan akan unik berdasarkan urutan angka. Jika kita ingin mencegah kombinasi 
yang sama muncul berulang, kita bisa menggunakan pendekatan yang berbeda, seperti menggunakan itertools.
permutations untuk menghasilkan permutasi unik dari angka yang tersedia.
"""