#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Shell Sort (Descending)
# ======================================================================================

def shellSort_desc(data):
    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] < temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 2

data = [54,26,93,17,77,31,44,55,20]
shellSort_desc(data)
print(data)