def operation(m1, m2, operator):
    r1 = len(m1)
    c1 = len(m1[0])
    r2 = len(m2)
    c2 = len(m2[0])

    if r1 != r2 or c1 != c2:
        return -1
    else:
        result = [0]*r1
        for i in range(r1):
            result[i] = [0]*c1

        for i in range(r1):
            for j in range(c1):
                if "penjumlahan" == operator:
                    result[i][j] = m1[i][j]+m2[i][j]
                elif "pengurangan" == operator:
                    result[i][j] = m1[i][j]-m2[i][j]
                elif "pembagian" == operator:
                    result[i][j] = m1[i][j]//m2[i][j]
                else:
                    result[i][j] = m1[i][j]*m2[i][j]

        return result
