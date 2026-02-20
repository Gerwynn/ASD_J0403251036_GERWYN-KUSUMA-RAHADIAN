#===============================================================
# Nama  : Gerwyn Kusuma Rahadian
# NIM   : J0403251036
# Kelas : A1
#===============================================================

#===============================================================
# Implementasi Dasar : Stack (Last In First Out)
#===============================================================

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Stack ada operasi push (memasukkan head baru) dan pop (menghapus head)
class stack:
    def __init__(self):
        self.top = None # top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None #Stack kosong jika node = None

    def push(self,data): #memasukkan data baru pada stack
        # 1) Membuat node baru
        nodeBaru = Node(data) # Instansiasi/memanggil konstruktor pada class Node

        # 2) Node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        # 3) Geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #Mengambil/menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack Kosong, Pop Tidak Bisa")
            return None
        hapus_data = self.top.data #Soroti bagian top dan simpan di variabel
        self.top = self.top.next #Geser ke Node berikutnya
        return hapus_data
    
    def peek(self):
        #Melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data
    
    def tampilkan(self):
        current = self.top
        print("Top", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")


# Instantiasi Class Stack
stack = stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.tampilkan()
print("Top saat ini adalah", stack.peek())
stack.pop()
stack.tampilkan()
stack.pop()
stack.tampilkan()
stack.pop()
stack.tampilkan()


        