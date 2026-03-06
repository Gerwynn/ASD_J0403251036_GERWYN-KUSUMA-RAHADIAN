#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Shell Sort (Ascending)
# ======================================================================================

def shellSort_asc(data):
    sublistcount = len(data) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort_asc(data, startposition, sublistcount)

        # Debugging: Print the list after each pass
        print(f"After increment of size {sublistcount}, the list is: {data}")

        sublistcount //= 2

def gapInsertionSort_asc(data, start, gap):
    for i in range(start + gap, len(data), gap):
        currentvalue = data[i]
        position = i

        while position >= gap and data[position - gap] > currentvalue:
            data[position] = data[position - gap]
            position -= gap

        data[position] = currentvalue

data = [54,26,93,17,77,31,44,55,20]
shellSort_asc(data)
print(data)