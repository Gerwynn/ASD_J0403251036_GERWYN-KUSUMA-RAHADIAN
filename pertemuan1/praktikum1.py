#Praktikum 1 - Gerwyn Kusuma Rahadian

# Membuka file dalam mode read ("r")
with open("data_mahasiswa.txt","r") as file:
    isi_file = file.read()
print(isi_file)

# Tipe data file
print("Tipe data:",type(isi_file))

# Membuka file per baris
jumlah_baris = 0
with open("data_mahasiswa.txt","r") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris
        print("Baris ke-", jumlah_baris)
        print('Isinya: ', baris)

# Parsing baris menjadi data satuan

with open("data_mahasiswa.txt","r") as file:
    for baris in file:
        baris = baris.strip() #Menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #Pecah menjadi data satuan dan menjadi 3 variabel
        print("NIM: ", nim, "| NAMA: ", nama, "| Nilai: ", nilai)

data_list = []

with open("data_mahasiswa.txt","r") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_list.append([nim,nama,int(nilai)])

print(data_list)
print(data_list[0:4])

data_dict = {}

with open("data_mahasiswa.txt","r") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
            "Nama" : nama,
            "Nilai" : nilai
        }

print (data_dict)