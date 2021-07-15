def faktorial(n):
    if n == 1:
        return n
    else:
        return n * faktorial(n-1)


# user input
num = int(input("Masukkan angka : "))

if num < 0:
    print("Input Invalid ! Masukkan angkat positif")
elif num == 0:
    print("Faktorial dari number 0 adalah 1")
else:
    print("Faktorial dari nomor", num, "=", faktorial(num))
