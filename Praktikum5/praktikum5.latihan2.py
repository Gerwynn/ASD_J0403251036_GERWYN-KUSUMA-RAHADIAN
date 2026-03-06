#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ==================================================================================================================
# Latihan 2: Tracing Rekursi
# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
# ==================================================================================================================
def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

"""
Penjelasan:
Output 'Keluar' muncul terbalik karena fungsi countdown memanggil dirinya sendiri sebelum mencetak 'Keluar'. 
Ketika countdown(3) dipanggil, ia mencetak 'Masuk: 3', lalu memanggil countdown(2), dan seterusnya hingga countdown(0). 
Saat countdown(0) dipanggil, ia mencetak 'Selesai' dan kembali ke panggilan sebelumnya. Ketika kembali ke countdown(1), 
ia mencetak 'Keluar: 1', lalu kembali ke countdown(2) dan mencetak 'Keluar: 2', dan seterusnya hingga mencetak 'Keluar: 3'.
"""