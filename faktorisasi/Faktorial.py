print("Nama     : Muhammad Rizal Pahlevi")
print("NIM      : A11.2020.12692")
print("Kelas    : 4210")


def Faktorial(x):
    if x == 1:
        return 1
    else:
        return x * Faktorial(x - 1)


print("_______Rekursif Faktorial_______")

print(Faktorial(2))
'''
x = 2
x == ? False
return x * Faktorial(x - 1)
return 2 * Faktorial(2 - 1)

x = 1
x == ? True
return x * Faktorial(1)
return 2 * return 1
return 2 * 1 = 6
Jadi, 2! = 2
'''


def Faktorial(x):
    if x == 1:
        return 1
    else:
        return x * Faktorial(x - 1)


print(Faktorial(1))
'''
x = 1
x == ? True
return x * Faktorial(1)
return return 1
return 1 = 1
Jadi, 1! adalah 1
'''
