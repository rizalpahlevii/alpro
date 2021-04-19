def add2Matrices(mA, mB):
    baris1 = len(mA)
    kolom1 = len(mB[0])
    baris2 = len(mA)
    kolom2 = len(mB[0])
    if baris1 != baris2 or kolom1 != kolom2:
        return -1
    else:
        mAB = [0]*baris1
        for x in range(baris1):
            mAB[x] = [0]*kolom1

        for x in range(baris1):
            for y in range(kolom2):
                mAB[x][y] = mA[x][y] * mB[x][y]

        return mAB


mA = [[3, 4, 5], [5, 6, 7], [6, 7, 8]]
mB = [[1, 2, 3], [4, 4, 4], [9, 10, 11]]

print("hasil a * b = ", add2Matrices(mA, mB))
