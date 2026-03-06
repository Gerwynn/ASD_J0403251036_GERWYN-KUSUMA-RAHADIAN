def bubbleSort_desc(nilai):
    for passnum in range(len(nilai)-1, 0, -1):
        for i in range(passnum):
            if nilai[i] < nilai[i + 1]: 
                temp = nilai[i]
                nilai[i] = nilai[i + 1]
                nilai[i + 1] = temp

nilai = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
print(f"Seluruh nilai kandidat sebelum di sorting : {nilai}")
bubbleSort_desc(nilai)
print(f"Seluruh nilai kandidat setelah di sorting : {nilai}")

# 1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah skor lima kandidat tersebut dari yang paling tinggi hingga terendah.

print(f"Skor 5 kandidat dengan nilai tertinggi : {nilai[:5]}")

# 2. Kandidat berapa saja yang lolos?

print(f"Kandidat yang lolos adalah kandidat dengan skor : {nilai[:5]}")