def bubbleSort(A):
    n = len(A)
    # A  = LIst itu sendiri
    # n = panjang list

    swap = False
    # variable untuk menyimpan data list sementara
    # variable untuk menampung data hasil yang ditukar

    # algorithm
    while not swap:
        # keadaan true artinya harus di cek dengan loopingan
        swap = True
        for j in range(1, n):  # loop sebanyak 9 kali
            if A[j-1] > A[j]:  # membandingkan 0 > 1
                swap = False
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp

    return A


print(bubbleSort([33, 11, 22, 99, 100, 102, 200, 50, 20]))
