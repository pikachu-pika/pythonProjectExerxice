# SUM,PRODUCT,MEAN,MEDIUM,MAXIMUM,MINIMUM OF N NUMBER OF NUMBERS
# DISTANCE FORMULA , LCM , HCF , FACTORS , FACTORIAL , FACTORS

import math


def numbers_arithmetic():
    print("If You Need Their Sum Enter 1")
    print("If You Need Their Product Enter 2")
    print("If You Need Their Average Enter 3")
    choice = int(input("Enter Your Choice :->"))
    times = int(input("Enter The The Number Of Time You Want To Enter Values :->"))

    if choice == 1:
        su = 0
        for i in range(times):
            n = float(input("Enter A Number :->"))
            su += n

        return su

    elif choice == 2:
        su = 1
        for i in range(times):
            n = float(input("Enter A Number :->"))
            su *= n

        return su

    elif choice == 3:
        su = 0
        avg = 0
        for i in range(times):
            n = float(input("Enter A Number :->"))
            su += n
            avg = su / times

        return avg.__round__(2)

    else:
        print("Wrong Choice Entered")


def numbers_comparison():
    print("If You Need The Greatest Number Enter 1")
    print("If You Need The Smallest Number Enter 2")
    print("If You Need The Median Number Enter 3")
    choice = int(input("Enter Your Choice :->"))
    times = int(input("Enter The The Number Of Time You Want To Enter Values :->"))

    if choice == 1:
        mx = int(input("Enter A Number :->"))
        for i in range(times - 1):
            n = int(input("Enter A Number :->"))
            if n > mx:
                mx = n

        return mx

    if choice == 2:
        mn = int(input("Enter A Number :->"))
        for i in range(times - 1):
            n = int(input("Enter A Number :->"))
            if n < mn:
                mn = n

        return mn

    if choice == 3:
        lis = []
        for i in range(times):
            n = int(input("Enter A Number :->"))
            lis.append(n)

        for i in range(len(lis)):
            for j in range(i + 1, len(lis)):
                if lis[i] > lis[j]:
                    lis[i], lis[j] = lis[j], lis[i]

        if times % 2 == 0:
            median = 1 / 2 * (lis[(int(times) // 2) - 1] + lis[((int(times) // 2) + 1) - 1])
            return median

        else:
            median = lis[(int((times + 1)) // 2) - 1]
            return median

    else:
        print("Wrong Choice Entered")


def distance_of_coordinates():
    abscissa1 = float(input("Enter The 'x coordinate' or 'abscissa' Of The First Ordered Pair :-> "))
    ordinate1 = float(input("Enter The 'y coordinate' or 'ordinate' Of The First Ordered Pair :-> "))
    abscissa2 = float(input("Enter The 'x coordinate' or 'abscissa' Of The Second Ordered Pair :-> "))
    ordinate2 = float(input("Enter The 'y coordinate' or 'ordinate' Of The Second Ordered Pair :-> "))

    distance = math.sqrt(math.pow((abscissa1 - abscissa2), 2) + math.pow((ordinate1 - ordinate2), 2))
    return distance


def hcf_of_two():  # TWO NUMBERS
    n1 = int(input("Enter The First Number :->"))
    n2 = int(input("Enter The Second Number :->"))

    if n1 < n2:
        mn = n1
    else:
        mn = n2

    hcf = 0
    for i in range(mn, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i
            break

    return hcf


def lcm_of_two():  # TWO NUMBERS
    n1 = int(input("Enter The First Number :->"))
    n2 = int(input("Enter The Second Number :->"))

    if n1 > n2:
        mx = n1
    else:
        mx = n2

    while True:
        if mx % n1 == 0 and mx % n2 == 0:
            lcm = mx
            break
        mx += 1

    return lcm


def lcm_of_array():  # importing math module
    times = int(input("Enter The The Number Of Time You Want To Enter Values :->"))
    lis = []

    for i in range(times):
        n = int(input("Enter A Number :->"))
        lis.append(n)

    lcm = lis[0]
    for i in range(1, len(lis)):
        lcm = lcm * lis[i] // math.gcd(lcm, lis[i])
    return lcm


def hcf_of_array():  # importing math module
    times = int(input("Enter The The Number Of Time You Want To Enter Values :->"))
    lis = []

    for i in range(times):
        n = int(input("Enter A Number :->"))
        lis.append(n)

    num1 = lis[0]
    num2 = lis[1]
    gcd = math.gcd(num1, num2)
    for i in range(2, len(lis)):
        gcd = math.gcd(gcd, lis[i])

    return gcd


# Factor a number or algebraic expression that divides another number or expression evenly—i.e., with no remainder.
# Factors of 12: 1, 2, 3, 4, 6, 8, 12.
def factors():
    fac = []
    n = int(input("Enter The Number :->"))

    fac = [i for i in range(1, n + 1) if n % i == 0]
    # for i in range(1, n + 1):
    #     if n % i == 0:
    #         fac.append(i)

    return fac


# Factorial is the product of all positive integers less than or equal to n. Examples: 4! = 4 × 3 × 2 × 1 = 24
def factorial1():
    n = int(input("Enter The Number :->"))

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)


# A series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
# Program to return Fibonacci series up to n value
def fibonacci_till():
    ntill = int(input("Till Which Number? :-> "))
    n1, n2 = 0, 1
    lis = []

    if ntill < 0:
        return "Please enter a positive integer"

    elif ntill == 0:
        lis = [0]

    elif ntill == 1:
        lis = [0, 1, 1]

    else:
        while n1 <= ntill:
            lis.append(n1)
            n3 = n1 + n2

            n1 = n2
            n2 = n3

    return lis


#  Program to return the Fibonacci sequence up to n-th term
def fibonacci_terms():
    nterms = int(input("How many terms? :-> "))
    n1, n2 = 0, 1
    count = 0
    lis = []

    if nterms <= 0:
        return "Please enter a positive integer"

    elif nterms == 1:
        lis = [0]

    else:
        while count < nterms:
            lis.append(n1)
            n3 = n1 + n2

            n1 = n2
            n2 = n3
            count += 1

    return lis


# Finding the fibonacci numbers in between a certain range
def fibonacci_between():
    nstart = int(input("Enter The Lower Limit :-> "))
    nend = int(input("Enter The Upper Limit:-> "))
    n1, n2 = 0, 1
    lis = []

    if nend < 0 or nstart < 0:
        return "Please enter a positive integer"

    elif nend == 0:
        lis = [0]

    elif nstart == 0 and nend == 1:
        lis = [0, 1, 1]

    elif nstart == 1 and nend == 1:
        lis = [1, 1]

    else:
        while n1 <= nend:
            if nstart <= n1 <= nend:
                lis.append(n1)
            n3 = n1 + n2

            n1 = n2
            n2 = n3

    return lis
