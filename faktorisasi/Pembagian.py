print("Nama     : Muhammad Rizal Pahlevi")
print("NIM      : A11.2020.12692")
print("Kelas    : 4210")


def red_bagi(x, y):
    i = x
    result = 0
    while i > 0:
        i = i - y
        result = result + 1  # result ++
    return result


print("_______Rekursif Pembagian_______")
print(red_bagi(40, 10))
'''
i = 40
    while i > 0 :
        True
i = 40 - 10 = 30 True
    result = 0 + 1 = 1

i = 30 - 10 = 20 True
    result = 1 + 1 = 2
    
i = 20 - 10 = 10 True
    result = 2 + 1 = 3

i = 10 - 10 = 0 False
    result = 3 + 1 = 4

return result // return 4
'''


def red_bagi(x, y):
    i = x
    result = 0
    while i > 0:
        i = i - y
        result = result + 1  # result ++
    return result


print(red_bagi(8, 2))
'''
i = 8
    while i > 0 :
        True
i = 8 - 2 = 6 True
    result = 0 + 1 = 1

i = 6 - 2 = 4 True
    result = 1 + 1 = 2
    
i = 4 - 2 = 2 True
    result = 2 + 1 = 3

i = 2 - 2 = 0 False
    result = 3 + 1 = 4

    >> return result // return 4 
'''
