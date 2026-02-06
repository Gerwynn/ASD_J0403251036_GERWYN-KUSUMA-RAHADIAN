"""
Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
Latihan Dasar 1 : Membuat Fungsi Load Data
"""

Nama_file = "data_mahasiswa2.txt"

def baca_data(Nama_file):
    data_dict = {}
    with open(Nama_file,"r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(',')
            data_dict[nim] = {"nama": nama,"nilai": int(nilai)}
    return data_dict

# buka_data = baca_data(Nama_file)
# print(len(buka_data))


"""
Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
Latihan Dasar 2 : Membuat Funamangsi Menampilkan Data
"""

def tampilkan_data(data_dict):
    print("\n===Daftar Mahasiswa===")
    print(f"{'NIM':<10} | {'NAMA':<50} | {'NILAI': <5}")
    print("-" * 40)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<50} | {int(nilai) : >5}")

# tampilkan_data(buka_data)

"""
Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
Latihan Dasar 3 : Membuat Fungsi Mencari Data
"""

def cari_data(data_dict):
    nim_cari = input("Masukkan NIM Mahasiswa Yang Ingin Dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("=== Data Mahasiswa Ditemukan ===")
        print(f"NIM       : {nim_cari}")
        print(f"NAMA      : {nama}")
        print(f"NILAI     : {nilai}")
    else:
        print("Data Tidak Ditemukan")

# cari_data(buka_data)   

"""
Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
Latihan Dasar 4 : Membuat Fungsi Update Data
"""

#Membuat fungsi update data
def ubah_data(data_dict):

    #awali dulu dengan mencari nim / data mahasiswa yang ingin di update
    nim = input("Masukkan NIM Mahasiswa yang Ingin Diubah Datanya: ").strip()

    if nim not in data_dict:
        print("NIM Tidak Ditemukan. Update Dibatalkan")
        return
    
    try:
        nilai_baru = nilai_baru = int(input("Masukkan Nilai Baru 0-100: ").strip())
    except ValueError:
        print("Nilai Harus Berupa Angka. Update Dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#Memanggil Fungsi Update Data

# ubah_data(buka_data)

"""
Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
Latihan Dasar 5 : Membuat Fungsi Simpan Data
"""

def simpan_data(Nama_file, data_dict):

    with open(Nama_file,"w",encoding="utf-8") as f:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"] 
            nilai = data_dict[nim]["nilai"]
            f.write(f"{nim},{nama},{nilai}\n")
    print("\nData Berhasil Disimpan ke File", Nama_file)
    #Memanggil fungsi dan simpan data
# simpan_data(Nama_file,buka_data)


"""
Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
Latihan Dasar 6 : Membuat Menu Interaktif 
"""

def main():
    # Load data otomatis saat program dimulai
    buka_data = baca_data(Nama_file) # fs. 1 fungsi load data

    while True:
        print("\n === Menu Data Mahasiswa ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")
    
        pilihan = int(input("Masukkan Fitur Berapa: ").strip())

        if pilihan == 1:
            tampilkan_data(buka_data)
        if pilihan == 2:
            cari_data(buka_data)
        if pilihan == 3:
            ubah_data(buka_data)
        if pilihan == 4:
            simpan_data(Nama_file,buka_data)
        if pilihan == 0:
            break

main()

