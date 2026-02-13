# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 1: Implementasikan Fungsi	Untuk Menghapus	Node dengan	Nilai Tertentu. 
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def delete_node(self, key):
        temp = self.head
        prev = None

        # Jika list kosong
        if not temp:
            return

        # Jika node yang dihapus adalah head
        if temp.data == key:
            self.head = temp.next
            if self.head is None: # Jika hanya ada satu node
                self.tail = None
            return

        # Cari node yang akan dihapus
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika tidak ditemukan
        if temp is None:
            return

        # Hapus node
        prev.next = temp.next

        # Jika yang dihapus adalah tail
        if temp == self.tail:
            self.tail = prev


# ================================
# Contoh Penggunaan
# ================================

ll = SingleLinkedList()
ll.insert_at_end(3)
ll.insert_at_end(7)
ll.insert_at_end(12)
ll.insert_at_end(19)
ll.insert_at_end(25)

ll.delete_node(7)
ll.display()