
def operation(v1, v2, operator):
    result = []
    if len(v1) != len(v2):
        return -1
    else:
        for i in range(len(v1)):
            if "penjumlahan" == operator:
                result.append(v1[i]+v2[i])
            elif "pengurangan" == operator:
                result.append(v1[i]-v2[i])
            elif "pembagian" == operator:
                result.append(v1[i]//v2[i])
            else:
                result.append(v1[i]*v2[i])
        return result
