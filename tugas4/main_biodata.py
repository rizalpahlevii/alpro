import biodata as biodataModule


def main():
    print(80*'-')
    nama = input("Masukkan Nama : ")
    umur = input("Masukkan Umur : ")
    mafa = input("Masukkan Makanan Favorit : ")
    mifa = input("Masukkan Minuman Favorit : ")
    hobi = input("Masukkan Hobi : ")
    cita2 = input("Masukkan Cita Cita : ")
    print(80*'-')

    biodataModule.tampilanBiodata(nama, umur, mafa, mifa, hobi, cita2)
    print(80*'-')


main()
