
def penjumlahan(v1, v2):
    result = []
    if len(v1) != len(v2):
        return -1
    else:
        for i in range(len(v1)):
            result.append(v1[i]+v2[i])
        return result


def pengurangan(v1, v2):
    result = []
    if len(v1) != len(v2):
        return -1
    else:
        for i in range(len(v1)):
            result.append(v1[i]-v2[i])
        return result


def perkalian(v1, v2):
    result = []
    if len(v1) != len(v2):
        return -1
    else:
        for i in range(len(v1)):
            result.append(v1[i]*v2[i])
        return result


def pembagian(v1, v2):
    result = []
    if len(v1) != len(v2):
        return -1
    else:
        for i in range(len(v1)):
            result.append(v1[i]/v2[i])
        return result
