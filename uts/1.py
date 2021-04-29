panjang = float(input("Masukkan Panjang Kolam dalam cm : "))
lebar = float(input("Masukkan Lebar Kolam dalam cm: "))
tinggi = float(input("Masukkan tinggi dinamis dalam cm :"))

volume = (panjang*lebar*tinggi) * (3/4)
liter = volume / 1000

satuHari = liter * 2
satuBulan = satuHari * 30

print("Dibutuhkan ", satuBulan, " liter untuk mandi satu bulan")
