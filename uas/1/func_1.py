def hitungPangkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitungPangkat(bilangan, pangkat-1)
    return bilangan


bil = int(input("Masukkan bilangan : "))
pgk = int(input("Masukkan pangkat : "))
print(f'Hasil = {hitungPangkat(bil,pgk)}')
