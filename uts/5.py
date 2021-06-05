def insertionSort(n, x):
    temp = 0
    for i in range(1, n):
        temp = x[i]
        j = i-1
        while j >= 0 and temp < x[j]:
            x[j+1] = x[j]
            j = j-1
            i = i-2
        x[j+1] = temp
    return x


def binarysearch(k, n, A):
    # k = angka yang di cari
    # n = jumlah data pada list
    # A =list itu sendiri
    found = False
    BB = 0
    BA = n-1
    while BB <= BA and not found:
        mid = int((BA+BB)/2)
        if A[mid] == k:
            found = True
            print("ketemu di index ke- ", mid, "and exist")
        else:
            if A[mid] > k:
                BA = mid-1
            else:
                BB = mid+1
    return found


a2 = [145, 77, 20, 1, 120, 3, 4]
print(a2, "Sebelum di sort ")
a = (insertionSort(7, a2))
print(a, "Sesudah di sort ")
cari = int(input("Cari angka berapa : "))
print(binarysearch(cari, 7, a))
