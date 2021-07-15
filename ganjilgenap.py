tmp = []


def CetakRecursiveGanjil(x):
    if (x % 2) != 0:
        if(x > 1):
            s = x-2
            tmp.append(s)
            CetakRecursiveGanjil(s)
        else:
            print(*tmp, sep=", ")
    else:
        print("bukan bilangan ganjil")


def main():
    CetakRecursiveGanjil(int(input("angka : ")))


main()
