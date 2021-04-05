# creating a function for insertion
def insertion_sort(A):
    temp = 0
    for i in range(1, len(A)):
        temp = A[i]
        j = i - 1

        while j >= 0 and temp < A[j]:
            temp = A[i]
            #     temp =  5
            # J = i - 1
            #    J = 1 - 1
            # J >= 0 and temp < A[j]
            #     J >= 0 and 5 < A[0]
            #          0 >= 0 and 5 < 10 true = tukar
            # A[j+i] = A[j]
            #      A[0 + 1] = A[0 - 1]
            #          A[1] = A[0 ]
            #              A[1] = 10
            # j = j - 1
            #     j = 0 - 1
            #          j = -1
            # i = i - 1
            #     i = 1 - 2
            #          i = -1
            # temp =  5
            # temp = A[i]
            #     temp =  13
            # J = i - 1
            #    J = 2 - 1
            # temp = A[i]
            #     temp =  8
            # J = i - 1
            #    J = 3 - 1
            # J >= 0 and temp < A[j]
            #     J >= 0 and 8 < A[2]
            #          0 >= 0 and 8 < 13 true = tukar
            # A[j+i] = A[j]
            #      A[2 + 1] = A[2 - 1]
            #          A[3] = A[2 ]
            #              A[3] = 13
            # j = j - 1
            #     j = 2 - 1
            #          j = 1
            # i = i - 1
            #     i = 3 - 2
            #          i = 1
            # temp =  8
            # J >= 0 and temp < A[j]
            #     J >= 0 and 8 < A[1]
            #          0 >= 0 and 8 < 10 true = tukar
            # A[j+i] = A[j]
            #      A[1 + 1] = A[1 - 1]
            #          A[2] = A[1 ]
            #              A[2] = 10
            # j = j - 1
            #     j = 1 - 1
            #          j = 0
            # i = i - 1
            #     i = 1 - 2
            #          i = -1
            # temp =  8
            # temp = A[i]
            #     temp =  2
            # J = i - 1
            #    J = 4 - 1
            # J >= 0 and temp < A[j]
            #     J >= 0 and 2 < A[3]
            #          0 >= 0 and 2 < 13 true = tukar
            # A[j+i] = A[j]
            #      A[3 + 1] = A[3 - 1]
            #          A[4] = A[3 ]
            #              A[4] = 13
            # j = j - 1
            #     j = 3 - 1
            #          j = 2
            # i = i - 1
            #     i = 4 - 2
            #          i = 2
            # temp =  2
            # J >= 0 and temp < A[j]
            #     J >= 0 and 2 < A[2]
            #          0 >= 0 and 2 < 10 true = tukar
            # A[j+i] = A[j]
            #      A[2 + 1] = A[2 - 1]
            #          A[3] = A[2 ]
            #              A[3] = 10
            # j = j - 1
            #     j = 2 - 1
            #          j = 1
            # i = i - 1
            #     i = 2 - 2
            #          i = 0
            # temp =  2
            # J >= 0 and temp < A[j]
            #     J >= 0 and 2 < A[1]
            #          0 >= 0 and 2 < 8 true = tukar
            # A[j+i] = A[j]
            #      A[1 + 1] = A[1 - 1]
            #          A[2] = A[1 ]
            #              A[2] = 8
            # j = j - 1
            #     j = 1 - 1
            #          j = 0
            # i = i - 1
            #     i = 0 - 2
            #          i = -2
            # temp =  2
            # J >= 0 and temp < A[j]
            #     J >= 0 and 2 < A[0]
            #          0 >= 0 and 2 < 5 true = tukar
            # A[j+i] = A[j]
            #      A[0 + 1] = A[0 - 1]
            #          A[1] = A[0 ]
            #              A[1] = 5
            # j = j - 1
            #     j = 0 - 1
            #          j = -1
            # i = i - 1
            #     i = -2 - 2
            #          i = -4
            # temp =  2
            A[j+1] = A[j]
            j = j-1
            i = i-2
        A[j+1] = temp
    return A


list1 = [10, 5, 13, 8, 2]
print("The unsorted list is:", list1)

print("The sorted list1 is:", insertion_sort(list1))
print("Muhammad Rizal Pahelvi")
print("A11.2020.12692")
