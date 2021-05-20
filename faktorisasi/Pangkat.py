print("Nama     : Muhammad Rizal Pahlevi")
print("NIM      : A11.2020.12692")
print("Kelas    : 4210")


def red_pangkat(x, y):
    if y == 1:
        return x
    else:
        return x * red_pangkat(x, y - 1)


print("_______Rekursif Pangkat_______")

print(red_pangkat(2, 3))

'''
x= 2 , y = 3
y == 1 ? False
return x * pangkat(x, y-1)
return 2 * pangkat(9, 3-1)

x= 2 , y = 2
y == 1 ? False
return x * pangkat(x, y-1)
return 2 * pangkat(9, 2-1)

x= 2 , y = 1
y == 1 ? True
return 2 * 2 * (return x)
return 2 * 2 * (return 2)
return 2 * 2 * 2 = 8
Jaka, 2 Pangkat 3 adalah 8

'''


def red_pangkat(x, y):
    if y == 1:
        return x
    else:
        return x * red_pangkat(x, y - 1)


print(red_pangkat(9, 2))
'''
x= 9 , y = 2
y == 1 ? False
return x * pangkat(x, y-1)
return 9 * pangkat(9, 2-1)

x= 9 , y = 1
y == 1 ? True
return 9 * (return x)
return 9 *(return 2)
return 9 * 9 = 81
Jaka, 9 Pangkat 2 adalah 81
'''
