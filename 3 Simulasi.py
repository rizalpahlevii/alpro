print("Nama     : Muhammad Rizal Pahlevi")
print("NIM      : A11.2020.12692")
print("Kelas    : 4210")

print("\nLinst Awal :", [2, 3, 1, 4, 5, 6, 8, 7])


def Selection(n, A):
    ###
    # n = Panjang List
    # A = list
    ###
    x = 0
    while x != n:
        for y in range(x, n):
            if A[x] > A[y]:
                temp = A[y]
                A[y] = A[x]
                A[x] = temp
        x += 1
    return A


print("\nHasil Selection Sort : ", Selection(
    8, [2, 3, 1, 4, 5, 6, 8, 7]), "\n")


def Binary(p1, L, f):
    ###
    # p1 = Panjang List
    # L = list
    # f = angka yang dicari
    ###
    found = False
    bb = 0
    ba = p1 - 1
    while bb <= ba and not found:
        mid = (ba+bb)//2
        if L[mid] == f:
            print("\tAngka Ditemuka")
            found = True
        else:
            if L[mid] > f:
                ba = mid - 1
            else:
                bb = mid + 1
    return found


print(Binary(8, Selection(8, [2, 3, 1, 4, 5, 6, 8, 7]), f=int(
    input("Cari Angka :"))), "\n")
