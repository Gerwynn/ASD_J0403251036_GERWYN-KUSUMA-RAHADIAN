# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 2: Buat Kode Implementasikan Pencarian pada Node Tertentu Single Circular Linked List.
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        # Jika list kosong
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            # Cari node terakhir (yang next-nya menunjuk ke head)
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("(Tidak ada elemen)")
            return

        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("... (back to head)")

    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")


# ================================
# Contoh Penggunaan
# ================================

print("\n=== Contoh Tampilan #1 ===")
cll = CircularSingleLinkedList()
data1 = [3, 7, 12, 19, 25]
print("Masukkan elemen ke dalam Circular Linked List:", data1)

for item in data1:
    cll.insert_at_end(item)

cll.display()

cari1 = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(cari1)


print("\n=== Contoh Tampilan #2 ===")
cll = CircularSingleLinkedList()   # RESET LIST
data2 = [5, 10, 15, 20, 30]
print("Masukkan elemen ke dalam Circular Linked List:", data2)

for item in data2:
    cll.insert_at_end(item)

cll.display()

cari2 = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(cari2)


print("\n=== Contoh Tampilan #3 ===")
cll = CircularSingleLinkedList()   # RESET LIST
data3 = []
print("Masukkan elemen ke dalam Circular Linked List:", data3)

for item in data3:
    cll.insert_at_end(item)

cll.display()

cari3 = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(cari3)