# Programs to calculate sum of given series

# 1 + 2 + 3 + 4 + .....N

def series1(n):
    su = n * (n + 1) // 2  # math formula

    # su = 0
    # for i in range(1, n + 1):
    #     su += i

    return su


# 2 + 4 + 6 + 8 + .....N

def series2(n):
    su = sum(i for i in range(2, n + 1, 2))

    # su = 0
    # for i in range(2, n + 1, 2):
    #     su += i

    return su


# 2 + 4 + 6 + 8 + .....Nth term

def series3(n):
    su = sum(i * 2 for i in range(1, n + 1))

    # su = 0
    # for i in range(1, n + 1):
    #     su += i * 2
    return su


# 1 + 3 + 5 + 7 + .....N

def series4(n):
    su = sum(i for i in range(1, n + 1, 2))

    # su = 0
    # for i in range(1, n + 1, 2):
    #     su += i
    return su


# 1 + 3 + 5 + 7 + .....Nth term

def series5(n):
    su = sum(i * 2 - 1 for i in range(1, n + 1))

    # su = 0
    # for i in range(1, n + 1):
    #     su += (i * 2 - 1)
    return su


#  1 + 1/2 + 1/3 + 1/4 + 1/5 + .....1/n

def series6(n):
    su = 0
    for i in range(1, n + 1):
        su += 1 / i

    return su.__round__(2)


# 1 + 4 + 9 + 16 + 25 + .....N

def series7(n):
    su = 0
    for i in range(1, n + 1):
        su += (i * i)

    return su


# 1 + 8 + 27 + 64 + .....N

def series8(n):
    su = 0
    for i in range(1, n + 1):
        su += (i * i * i)

    return su


# x/2 + x/4 + x/8 + x/16 + Nth term

def series9(x, n):
    su = 0
    c = 2
    for i in range(1, n + 1):
        su += (x / c)
        c *= 2

    return su.__round__(2)


# 1**3/x + 3**3/x + 5**3/x + 7**3/x + ..... Nth term

def series10(x, n):
    su = 0
    c = 1
    for i in range(1, n + 1):
        su += (c ** 3 / x)
        c += 2

    return su.__round__(2)


# 2**x + 4**x + 6**x + 8**x + .....Nth term

def series11(x, n):
    su = 0
    for i in range(1, n + 1):
        su += ((i * 2) ** x)
    return su


# 1! + 2! + 3! + 4! + ..... n!

def series12(n):
    su = 0
    for i in range(1, n + 1):
        f = 1
        for j in range(1, i + 1):
            f *= j
        su += f
    return su


# a**1/1 + a**2/2 + a**3/6 + a**4/24 + a**5/25 + ..... + a**n/n! (factorial)

def series13(a, n):
    su = 0
    for i in range(1, n + 1):
        f = 1
        for j in range(1, i + 1):
            f *= j
        su += (a ** i) / f

    return su.__round__(2)


# x+5**2/1+2  +  x+25**2/3+4  +  x+125**2/5+6 + ..... Nth term

def series14(x, n):
    su = 0
    c = 1
    t = 5
    for i in range(1, n + 1):
        su = su + (x + (t ** 2)) / (c + c + 1)
        c += 2
        t *= 5
    return su.__round__(2)


# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + .....N

def series15(n):
    n1, n2 = 0, 1
    su = 0

    if n == 0:
        su = 0

    elif n == 1:
        su = 0 + 1 + 1

    else:
        while n1 <= n:
            su += n1
            n3 = n1 + n2

            n1 = n2
            n2 = n3

    return su


# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + .....Nth term

def series16(n):
    n1, n2 = 0, 1
    count = 0
    su = 0

    if n == 1:
        su = 0

    else:
        while count < n:
            su += n1
            n3 = n1 + n2

            n1 = n2
            n2 = n3
            count += 1

    return su


# 1/a + 2/a**2 + 3/a**3 + ... + n/a**n

def series17(a, n):
    su = 0
    for i in range(1, n + 1):
        su = su + (i / (a ** i))
    return su.__round__(2)


# 1/1 + (1 + 2) / (1 * 2) + (1 + 2 + 3) / (1 * 2 * 3) + -------- + (1 + 2 + 3 + ----- + n ) / (1 * 2 * 3 * ----- * n)

def series18(n):
    su = 0
    for i in range(1, n + 1):
        f = 1
        ad = 0
        for j in range(1, i + 1):
            ad += j
            f *= j
        su = su + (ad / f)
    return su


# a + aa + aaa + aaaa + aaaaa + aaaaaa     N times  or till Nth term
# e.g. 8 + 88 + 888 + 8888 + 88888 + 888888

def series19(a, n):
    su = 0
    for i in range(1, n + 1):
        su += a
        a = a * 10 + a
    return su


# 2 - 4 + 6 - 8 + …… - 20 ... +or- n

def series20(n):
    su = 0
    c = 1
    for i in range(2, n + 1, 2):
        if c % 2 != 0:
            su += i
        else:
            su -= i
        c += 1
    return su


# 1+ 12+ 123+ 1234+ ....... 12345....n

def series21(n):
    su = 0
    c = 1
    for i in range(1, n + 1):
        su += c
        c = c * 10 + (i + 1)
    return su
