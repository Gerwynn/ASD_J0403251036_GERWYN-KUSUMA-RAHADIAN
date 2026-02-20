#===============================================================
# Nama  : Gerwyn Kusuma Rahadian
# NIM   : J0403251036
# Kelas : A1
#===============================================================

#===============================================================
# Implementasi Dasar : Queue (First In First Out)
#===============================================================

#Enqueue = Menambahkan data dari belakang dari data (rear)
#Dequeue = Menghapus/mengambil data dari depan (front)

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjuk ke Node berikutnya
    
class Queue:
    #buat konstruktor untuk inisialisasi variabel front and rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None

    #membuat fungsi untuk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data)
        
        #Jika queue kosong, front and rear menunjuk ke Node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru

        #Jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jalankan data baru sebagai rear
        self.rear.next = nodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai user

    def dequeue(self):
        #Menghapus data dari depan/front
        hapus_data = self.front.data #lihat data paling depan
        self.front = self.front.next

        #Jika setelah geser front menjadi None, maka queue kosong
        #rear juga harus jadi None
        if self.front is None:
            self.rear = None

        return hapus_data

    def tampilkan(self):
        current = self.front
        print("Front ->", end="")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")

#Instantiasi class queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()

        
