# Muhammad Rizal Pahlevi
# A11.2020.12692

def selectionShort(n, a):
    # n = panjang list
    # a = list angka

    i = 0

    while i != n:

        for j in range(i, n):
            if a[i] > a[j]:
                # start
                # Loop  0 ,i = 0 /j= 0
                #     a[i] > a[j]
                #     a[0] > a[0]
                #     11 > 11 = false
                # a =  [11, 90, 23, 908, 123, 32]
                # j++
                # # index [0] > index [0]
                # # end
                # # ============
                # # start
                # # Loop  0 ,i = 0 /j= 1
                # #     a[i] > a[j]
                # #     a[0] > a[1]
                # #     11 > 90 = false
                # # a =  [90, 11, 23, 908, 123, 32]
                # # j++
                # # index [0] > index [1]
                # # end
                # # ============
                # # start
                # # Loop  0 ,i = 0 /j= 2
                # #     a[i] > a[j]
                # #     a[0] > a[2]
                # #     90 > 23 = true
                # # a =  [23, 11, 90, 908, 123, 32]
                # # j++
                # # index [0] > index [2]
                # # end
                # # ============
                # # start
                # # Loop  0 ,i = 0 /j= 3
                # #     a[i] > a[j]
                # #     a[0] > a[3]
                # #     23 > 908 = false
                # # a =  [908, 11, 90, 23, 123, 32]
                # # j++
                # # index [0] > index [3]
                # # end
                # # ============
                # # start
                # # Loop  0 ,i = 0 /j= 4
                # #     a[i] > a[j]
                # #     a[0] > a[4]
                # #     908 > 123 = true
                # # a =  [123, 11, 90, 23, 908, 32]
                # # j++
                # # index [0] > index [4]
                # # end
                # # ============
                # # start
                # # Loop  0 ,i = 0 /j= 5
                # #     a[i] > a[j]
                # #     a[0] > a[5]
                # #     123 > 32 = true
                # # a =  [32, 11, 90, 23, 908, 123]
                # # j++
                # # index [0] > index [5]
                # # end
                # # ============
                # # start
                # # Loop  1 ,i = 1 /j= 1
                # #     a[i] > a[j]
                # #     a[1] > a[1]
                # #     11 > 11 = false
                # # a =  [32, 11, 90, 23, 908, 123]
                # # j++
                # # index [1] > index [1]
                # # end
                # # ============
                # # start
                # # Loop  1 ,i = 1 /j= 2
                # #     a[i] > a[j]
                # #     a[1] > a[2]
                # #     11 > 90 = false
                # # a =  [32, 90, 11, 23, 908, 123]
                # # j++
                # # index [1] > index [2]
                # # end
                # # ============
                # # start
                # # Loop  1 ,i = 1 /j= 3
                # #     a[i] > a[j]
                # #     a[1] > a[3]
                # #     90 > 23 = true
                # # a =  [32, 23, 11, 90, 908, 123]
                # # j++
                # # index [1] > index [3]
                # # end
                # # ============
                # # start
                # # Loop  1 ,i = 1 /j= 4
                # #     a[i] > a[j]
                # #     a[1] > a[4]
                # #     23 > 908 = false
                # # a =  [32, 908, 11, 90, 23, 123]
                # # j++
                # # index [1] > index [4]
                # # end
                # # ============
                # # start
                # # Loop  1 ,i = 1 /j= 5
                # #     a[i] > a[j]
                # #     a[1] > a[5]
                # #     908 > 123 = true
                # # a =  [32, 123, 11, 90, 23, 908]
                # # j++
                # # index [1] > index [5]
                # # end
                # # ============
                # # start
                # # Loop  2 ,i = 2 /j= 2
                # #     a[i] > a[j]
                # #     a[2] > a[2]
                # #     11 > 11 = false
                # # a =  [32, 123, 11, 90, 23, 908]
                # # j++
                # # index [2] > index [2]
                # # end
                # # ============
                # # start
                # # Loop  2 ,i = 2 /j= 3
                # #     a[i] > a[j]
                # #     a[2] > a[3]
                # #     11 > 90 = false
                # # a =  [32, 123, 90, 11, 23, 908]
                # # j++
                # # index [2] > index [3]
                # # end
                # # ============
                # # start
                # # Loop  2 ,i = 2 /j= 4
                # #     a[i] > a[j]
                # #     a[2] > a[4]
                # #     90 > 23 = true
                # # a =  [32, 123, 23, 11, 90, 908]
                # # j++
                # # index [2] > index [4]
                # # end
                # # ============
                # # start
                # # Loop  2 ,i = 2 /j= 5
                # #     a[i] > a[j]
                # #     a[2] > a[5]
                # #     23 > 908 = false
                # # a =  [32, 123, 908, 11, 90, 23]
                # # j++
                # # index [2] > index [5]
                # # end
                # # ============
                # # start
                # # Loop  3 ,i = 3 /j= 3
                # #     a[i] > a[j]
                # #     a[3] > a[3]
                # #     11 > 11 = false
                # # a =  [32, 123, 908, 11, 90, 23]
                # # j++
                # # index [3] > index [3]
                # # end
                # # ============
                # # start
                # # Loop  3 ,i = 3 /j= 4
                # #     a[i] > a[j]
                # #     a[3] > a[4]
                # #     11 > 90 = false
                # # a =  [32, 123, 908, 90, 11, 23]
                # # j++
                # # index [3] > index [4]
                # # end
                # # ============
                # # start
                # # Loop  3 ,i = 3 /j= 5
                # #     a[i] > a[j]
                # #     a[3] > a[5]
                # #     90 > 23 = true
                # # a =  [32, 123, 908, 23, 11, 90]
                # # j++
                # # index [3] > index [5]
                # # end
                # # ============
                # # start
                # # Loop  4 ,i = 4 /j= 4
                # #     a[i] > a[j]
                # #     a[4] > a[4]
                # #     11 > 11 = false
                # # a =  [32, 123, 908, 23, 11, 90]
                # # j++
                # # index [4] > index [4]
                # # end
                # # ============
                # # start
                # # Loop  4 ,i = 4 /j= 5
                # #     a[i] > a[j]
                # #     a[4] > a[5]
                # #     11 > 90 = false
                # # a =  [32, 123, 908, 23, 90, 11]
                # # j++
                # # index [4] > index [5]
                # # end
                # # ============
                # # start
                # # Loop  5 ,i = 5 /j= 5
                # #     a[i] > a[j]
                # #     a[5] > a[5]
                # #     11 > 11 = false
                # # a =  [32, 123, 908, 23, 90, 11]
                # # j++
                # # index [5] > index [5]
                # # end
                # # ============
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
                print(a)

        i += 1
    return a


a = [11, 90, 23, 908, 123, 32]
print(selectionShort(len(a), a))
print("Muhammad Rizal Pahlevi")
print("A11.2020.12692")
