mhs1 = {
    'ID': 101,
    'Matkul': 'Algoritma Dan Pemrograman',
    'UTS': 85,
    'UAS': 90
}

mhs2 = {
    'ID': 102,
    'Matkul': 'Algoritma Dan Pemrograman',
    'UTS': 80,
    'UAS': 85
}

mhs3 = {
    'ID': 103,
    'Matkul': 'Algoritma Dan Pemrograman',
    'UTS': 80,
    'UAS': 90
}


print('Mahasiswa 1 :\n ', mhs1)
print('Mahasiswa 2 :\n ', mhs2)
print('Mahasiswa 3 :\n ', mhs3)

# Menambahkan/Mengubah Entry
mhs1['UTS'] = 90
print("Perubahan :\n", mhs1, '\n')

# Mengecek Keberadaan Key
a = 'UTS' in mhs1  # Apakah UTS ada di mhs1?
print(a)
b = 'UAS' in mhs2  # Apakah UAS ada di mhs2?
print(b)
c = 'Remidi' in mhs3  # Apakah Remidi ada di mhs3?
print(c)

print('\n')
# Mendapat nilai dengan pengulangan otomatis

d = mhs3.values()
print(d, '\n')
