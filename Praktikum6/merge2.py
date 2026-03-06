#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Merge Sort (Descending)
# ======================================================================================

def mergeSort_desc(data):
    if len(data) > 1:
        mid = len(data) // 2
        L = data[:mid]
        R = data[mid:]

        mergeSort_desc(L)
        mergeSort_desc(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1

data = [54,26,93,17,77,31,44,55,20]
mergeSort_desc(data)
print(data)