print("Populasi Hewan Ternak")

kuda = {
    "nama": 'Kuda',
    "tahun_2015": 100,
    "tahun_2016": 200,
    "tahun_2017": 300,
}

sapi = {
    "nama": 'Sapi',
    "tahun_2015": 100,
    "tahun_2016": 200,
    "tahun_2017": 300,
}

kambing = {
    "nama": 'Kambing',
    "tahun_2015": 100,
    "tahun_2016": 200,
    "tahun_2017": 300,
}

kerbau = {
    "nama": 'Kerbau',
    "tahun_2015": 100,
    "tahun_2016": 200,
    "tahun_2017": 300,
}

for i, j in kuda.items():
    print(i, '=', j)

print('\n')

for i, j in sapi.items():
    print(i, '=', j)
print('\n')

for i, j in kambing.items():
    print(i, '=', j)
print('\n')

for i, j in kerbau.items():
    print(i, '=', j)
print('\n')

# accessing data
print('Data kuda tahun 2016 = ', kuda['tahun_2016'])
print('Data kerbau tahun 2016 = ', kerbau['tahun_2016'])
print('Data sapi tahun 2016 = ', sapi['tahun_2016'])
print('\n')
# update data
print("Data awal kerbau pada tahun 2015 = ", kerbau['tahun_2015'])
kerbau['tahun_2015'] = 800
print("Data akhir kerbau pada tahun 2015 = ", kerbau['tahun_2015'])
