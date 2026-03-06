#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Bubble Sort (Ascending)
# ======================================================================================

# 1.  Implementasi algoritma bubble sort pada Python.

def bubbleSort_asc(data):
    for passnum in range(len(data)-1, 0, -1):
        for i in range(passnum):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubbleSort_asc(data)
print(data)

# 2. Implementasi algoritma bubble sort yang lebih efisien.

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1

alist = [20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)