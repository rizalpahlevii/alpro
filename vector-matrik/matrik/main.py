import myLib


def main():
    v1 = [[12, 22, 32], [56, 66, 76], [11, 21, 19]]
    v2 = [[10, 20, 30], [21, 31, 41], [42, 52, 62]]

    print("Penjumlahan : ", myLib.operation(v1, v2, "penjumlahan"))
    print("Pengurangan : ", myLib.operation(v1, v2, "pengurangan"))
    print("Perkalian : ", myLib.operation(v1, v2, "perkalian"))
    print("Pembagian : ", myLib.operation(v1, v2, "pembagian"))


main()
