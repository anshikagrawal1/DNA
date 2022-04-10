def isBasetwo(num, base):
    for i in range(len(num)):
        if (num[i].isnumeric() and (ord(num[i]) >= ord('0') and ord(num[i]) < (ord('0') + base)) == False):
            return False
    return True


def decodeBinarySeq(binarySeq):
    if (isBasetwo(binarySeq, 2)):
        pass
        if ((L >= 8 and L <= 24) and L % 2 == 0):
            pass
    else:
        result = "Invalid input"
        return result

    bases = {'00': 'C', '01': 'G', '10': 'A', '11': 'T'}
    seq = ""
    i1 = 0
    for i in binarySeq[0:L:2]:
        # print(binarySeq[i:i+2])
        seq = seq + bases[binarySeq[i1:i1 + 2]]
        i1 += 2
    return seq


binarySeq = input()
L = len(binarySeq)

print(decodeBinarySeq(binarySeq))