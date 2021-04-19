def bubbleSort(n, A):
    swap = False
    while not swap:
        swap = True
        for j in range(1, n):
            if A[j-1] > A[j]:
                swap = False
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp

    return A


print(bubbleSort(3, [45, 90, 12]))
