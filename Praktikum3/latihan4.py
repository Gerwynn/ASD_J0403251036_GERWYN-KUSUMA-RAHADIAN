# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 4: Buat Metode untuk Menggabungkan Dua Single Linked List Menjadi Satu Single Linked List Baru.
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, other_list):
        # Jika list pertama kosong
        if not self.head:
            return other_list

        # Jika list kedua kosong
        if not other_list.head:
            return self

        # Sambungkan tail list pertama ke head list kedua
        self.tail.next = other_list.head
        self.tail = other_list.tail

        return self


# ================================
# Contoh Tampilan #1
# ================================

print("=== Contoh Tampilan #1 ===")

ll1 = SingleLinkedList()
ll2 = SingleLinkedList()

data1 = [1, 3, 5, 7]
data2 = [2, 4, 6, 8]

print("Masukkan elemen untuk Linked List 1:", data1)
print("Masukkan elemen untuk Linked List 2:", data2)

for item in data1:
    ll1.insert_at_end(item)

for item in data2:
    ll2.insert_at_end(item)

print("Linked List 1:", end=" ")
ll1.display()

print("Linked List 2:", end=" ")
ll2.display()

merged = ll1.merge(ll2)

print("Linked List setelah digabungkan:", end=" ")
merged.display()


# ================================
# Contoh Tampilan #2
# ================================

print("\n=== Contoh Tampilan #2 ===")

ll3 = SingleLinkedList()
ll4 = SingleLinkedList()

data3 = [5, 15, 25]
data4 = []

print("Masukkan elemen untuk Linked List 1:", data3)
print("Masukkan elemen untuk Linked List 2:", "(Tidak ada elemen)")

for item in data3:
    ll3.insert_at_end(item)

for item in data4:
    ll4.insert_at_end(item)

print("Linked List 1:", end=" ")
ll3.display()

print("Linked List 2:", end=" ")
ll4.display()

merged2 = ll3.merge(ll4)

print("Linked List setelah digabungkan:", end=" ")
merged2.display()