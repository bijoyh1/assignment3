import math


def feistel(input, k):
    L0 = input[:4]
    R0 = input[4:]
    L1 = R0
    R1 = exclusiveOr(L0, F(R0, k))
    temp = R1
    R1 = L1
    L1 = temp
    return L1 + R1


def exclusiveOr(a, b):
    xor = ""
    for x in range(4):
        if a[x] == b[x]:
            xor = xor + "0"
        else:
            xor = xor + "1"
    return xor


def F(R0, k):
    total = (2 * math.pow(BinarytoDecimal(R0), BinarytoDecimal(k))) % 16
    total = DecimaltoBinary(total)
    if len(total)!= 4:
        total = "0" + total
    return total

def DecimaltoBinary(a):
    a = int(a)
    if a >=1:
        return str(DecimaltoBinary(a//2)) +  str(a%2)
    else:
        return ""

def BinarytoDecimal(a):
    total = 0
    for x in range(4):
        total = total + int(a[3-x])*math.pow(2,x)
    return total


print(F("1111","0110"))
