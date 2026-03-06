#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Selection Sort (Descending)
# ======================================================================================

def selectionSort_desc(data):
    n = len(data)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if data[j] > data[max_idx]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]

data = [54,26,93,17,77,31,44,55,20]
selectionSort_desc(data)
print(data)