# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Gerwyn Kusuma Rahadian
# NIM : J0403251036
# Kelas : A1
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "data_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}
    with open(nama_file,'r',encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()
            kode_barang, nama_barang, stok_barang = baris.split(',')
            stok_dict[kode_barang] = {"nama": nama_barang,"stok": int(stok_barang)}
    return stok_dict



# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    print("\n===Daftar Barang===")
    print(f"{'Kode Barang':<10} | {'Nama Barang':<50} | {'Stok':<10}")
    print('-' * 50)

    for kode_barang in sorted(stok_dict.keys()):
        nama_barang = stok_dict[kode_barang]["nama"]
        stok_barang = stok_dict[kode_barang]["stok"]
        print(f"{kode_barang:<10} | {nama_barang:<50} | {int(stok_barang):<10}")

# # -------------------------------
# # Fungsi: Cari barang berdasarkan kode
# # -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    cari_kode = input("Masukkan kode barang: ").strip()

    if cari_kode in stok_dict:
        nama_barang = stok_dict[cari_kode]["nama"]
        stok_barang = stok_dict[cari_kode]["stok"]

        print(f"\n=== Kode Barang Ditemukan! ===")
        print(f"Kode Barang:    {cari_kode}")
        print(f"Nama Barang:    {nama_barang}")
        print(f"Stok Barang:    {stok_barang}")
    else:
        print("=== Kode Barang yang Anda Cari Tidak Ditemukan ===")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode_barang = input("Masukkan kode barang baru: ").strip()
    

    if kode_barang in stok_dict:
        print("=== Kode Barang Telah Terdaftar dalam Data Barang! ===")
        return
    else:
        nama_barang = input("Masukkan nama barang baru: ").strip()
        stok_barang = input("Masukkan jumlah stok barang baru: ").strip()

        stok_dict[kode_barang] = {"nama":nama_barang,"stok":int(stok_barang),}
        print("=== Barang Berhasil Ditambahkan! (Jangan Lupa Simpan!) ===")


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode_barang = input("Masukkan kode barang yang ingin diupdate: ").strip()



    if kode_barang not in stok_dict:
        print("Kode Barang Tidak Ditemukan. Update Dibatalkan")
        return
    else:
        nama_barang = stok_dict[kode_barang]["nama"]
        stok_barang = stok_dict[kode_barang]["stok"]

        print("Pilih Jenis Update:")
        print("1. Tambahi Stok")
        print("2. Kurangi Stok")
        pilih_jenis = int(input("Pilih Jenis Update: "))

        if pilih_jenis == 1:
                try:
                    penambahan = int(input("Berapa Jumlah Stok yang Ingin Ditambahkan: ").strip())
                    stok_baru = stok_barang + penambahan
                    stok_dict[kode_barang]["stok"] = stok_baru
                    print("=== Stok Berhasil Ditambah. Update Berhasil! (Jangan Lupa Simpan!) ===")
                except ValueError:
                    print("=== Stok Harus Berupa Angka. Update Dibatalkan! ===")
                    return
        elif pilih_jenis == 2:
                try:
                    pengurangan = int(input("Berapa Jumlah Stok yang Ingin Dikurangi: ").strip())
                    stok_baru = stok_barang - pengurangan
                    if stok_baru >= 0:
                        stok_dict[kode_barang]["stok"] = stok_baru
                        print("=== Stok Berhasil Dikurangi. Update Berhasil! (Jangan Lupa Simpan!) ===")
                    else:
                        print("=== Stok Kurang dari 0. Update Dibatalkan! ===")
                        return  
                except ValueError:
                    print("=== Stok Harus Berupa Angka. Update Dibatalkan! ===")
                    return
        else:
            print("=== Pilihan Tidak Valid! ===")
            return

# # -------------------------------
# # Fungsi: Menyimpan data ke file
# # -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """

    with open(nama_file,'w',encoding='utf-8') as f:
        for kode_barang in sorted(stok_dict.keys()):
            nama_barang = stok_dict[kode_barang]["nama"]
            stok_barang = stok_dict[kode_barang]["stok"]
            f.write(f"{kode_barang},{nama_barang},{stok_barang}\n")
    print("=== Update Telah Tersimpan! ===")

# -------------------------------
# Program Utama
# -------------------------------
def main():
# Membaca data dari file saat program mulai
    data_barang = baca_stok(nama_file)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_semua(data_barang)
        elif pilihan == "2":
            cari_barang(data_barang)
        elif pilihan == "3":
            tambah_barang(data_barang)
        elif pilihan == "4":
            update_stok(data_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, data_barang)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()