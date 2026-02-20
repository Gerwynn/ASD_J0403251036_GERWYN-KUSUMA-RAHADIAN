#===============================================================
# Nama  : Gerwyn Kusuma Rahadian
# NIM   : J0403251036
# Kelas : A1
#===============================================================

#===============================================================
# Implementasi Dasar : Node pada Linked List
#===============================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstansiasi
    def __init__(self, data):
        self.data = data #Menyimpan data atau nilai pada list
        self.next = None #Pointer ini menunjuk ke node berikutnya (tidak menunjuk ke node lain)

# 1) Membuat node dengan instansiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C
head = nodeA #Menetapkan nodeA sebagai head (awal) dari linked list
nodeA.next = nodeB #Node A menunjuk ke Node B
nodeB.next = nodeC #Node B menunjuk ke Node C

# 3) Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #Pindah ke node berikutnya (next)

    