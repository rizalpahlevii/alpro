import myLib


def main():
    v1 = [1, 2, 3]
    v2 = [2, 8, 6]

    print("Penjumlahan : ", myLib.operation(v1, v2, "penjumlahan"))
    print("Pengurangan : ", myLib.operation(v1, v2, "pengurangan"))
    print("Perkalian : ", myLib.operation(v1, v2, "perkalian"))
    print("Pembagian : ", myLib.operation(v1, v2, "pembagian"))


main()
