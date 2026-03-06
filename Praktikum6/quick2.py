#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# ======================================================================================
# Quick Sort (Descending)
# ======================================================================================

def quickSort_desc(data):
    quickSortHelper_desc(data, 0, len(data) - 1)

def quickSortHelper_desc(data, first, last):
    if first < last:
        splitpoint = partition_desc(data, first, last)
        quickSortHelper_desc(data, first, splitpoint - 1)
        quickSortHelper_desc(data, splitpoint + 1, last)

def partition_desc(data, first, last):
    pivotvalue = data[first]   

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            data[leftmark], data[rightmark] = data[rightmark], data[leftmark]

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark

data = [54,26,93,17,77,31,44,55,20]
quickSort_desc(data)
print(data)
    
