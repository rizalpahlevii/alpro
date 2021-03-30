

def generate(n, a):
    i = 0

    while i != n:

        for j in range(i, n):
            print("start")
            print("Loop ", i, ",i =", i, "/j=", j)
            print("    a[i] > a[j]")
            print("    a[%d] > a[%d]" % (i, j))
            type = 'true' if a[i] > a[j] else 'false'
            print("    %d > %d = %s" % (a[i], a[j], type))
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            print("a = ", a)
            print("j++")
            print("index [%d] > index [%d]" % (i, j))
            print("end")
            print("============")
            print(a)

        i += 1

    return a


a = [11, 90, 23, 908, 123, 32]
print(generate(len(a), a))
