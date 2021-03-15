import aritmatika


def main():
    angka1 = 8
    angka2 = 7
    angka3 = 80
    angka4 = 99
    angka5 = 2
    angka6 = 120

    hasil1 = aritmatika.perkalian(angka1, angka2)
    hasil2 = aritmatika.pengurangan(angka3, angka4)
    hasil3 = aritmatika.pembagian(hasil2, angka5)
    hasil4 = aritmatika.penjumlahan(hasil1, hasil3)
    hasil5 = aritmatika.perkalian2(hasil4, angka6)

    print(hasil5)


main()
