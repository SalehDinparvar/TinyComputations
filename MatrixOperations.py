
import math


def mprint(m):
    print("********")
    for i in range(len(m)):  # rows
        for ii in range(len(m[i])):  # columns
            if m[i][ii][1] == 1:
                print(m[i][ii][0], end="       ")  # set desired spaces
            else:
                print("(" + str(m[i][ii][0]) + "/" + str(m[i][ii][1]) + ")", end="   ")
        print()
    print("********")


def mat():  # Input Matrice:
    x = int(input("Number of rows:   "))
    y = int(input("Number of coloumns:   "))
    Matrice = []
    for i in range(x):
        row = []
        for ii in range(y):
            intry = []
            intry.append(
                float(input("Enter value " + str(len(Matrice) + 1) + ", " + str(ii + 1) + ":   ")))  # nominator
            # intry.append(float(input("Enter denominator " + str(len(Matrice) + 1) + ", " + str(ii + 1) + ":   ")))
            intry.append(1)
            row.append(intry)
        Matrice.append(row)
    # mprint(Matrice)
    return Matrice


def sade(l):  # within single intrie
    a = []
    if l[0] == int(l[0]) and l[1] == int(l[1]):
        for i in range(int(min(l) + 1)):
            if i != 0:
                if l[0] % i == 0 and l[1] % i == 0:
                    a = [l[0] // i, l[1] // i]
                    l = a
    return l


def sade2(m):  # simplify all intries
    for i in range(len(m)):
        for ii in range(len(m[i])):
            m[i][ii] = sade(m[i][ii])
    return m


def sade3(m):  # simplify rows
    m = sade2(m)
    for i in range(len(m)):  # for every row
        l = []
        dv = []  # divisors/factors
        for ii in m[i]:
            l.append(ii[0])
        for j in range(int(min(l) + 1)):
            if j != 0 and j != 1:
                state = 1
                for iii in l:  # filter non-factors
                    if iii % j != 0:
                        state = 0
                if state:
                    dv.append(j)
        for ii in range(len(m[i])):  # for every element within the row
            if len(dv) > 0:
                m[i][ii][0] //= max(dv)
        if len(dv) > 0:
            print("R_" + str(1 + i) + "=" + "R_" + str(1 + i) + "/" + str(max(dv)))
            mprint(m)
    return m


def prog():
    m = mat()
    mprint(m)
    m = sade3(m)
    c = []
    while True:
        sat = int(input("Enter starting row:  "))  # row
        c.append(int(input("Multiplier nominator:  ")))  # constant
        c.append(int(input("Multiplier denominator:  ")))  # constant
        gsat = int(input("Enter target row:  "))
        for i in range(len(m[0])):  # for every column
            m[gsat - 1][i][0] = m[gsat - 1][i][0] * c[1] * m[sat - 1][i][1] + m[gsat - 1][i][1] * c[0] * m[sat - 1][i][
                0]
            m[gsat - 1][i][1] *= m[sat - 1][i][1] * c[1]
        print("R_" + str(gsat) + "=" + str(c[0]) + "/" + str(c[1]) + "*R_" + str(sat))
        mprint(m)
        m = sade3(m)


prog()

#creative commons, share alike 
# Saleh Dinparvar, 27 Oct 2020
