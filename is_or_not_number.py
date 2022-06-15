# CONTAINS FUNCTIONS TO CHECK WHETHER THE NUM IS ____ OR NOT
# All functions start with "is_" and whether it is
# do not use func for float and negative numbers
# is_perfect_square() can be used for both whole and float no.

import math


def is_even():
    n = int(input("Enter The Number :->"))

    if n % 2 == 0:
        return True

    else:
        return False


def is_odd():
    n = int(input("Enter The Number :->"))

    if n % 2 != 0:
        return True

    else:
        return False


# Armstrong Number is a positive number if it is equal to the sum of cubes of its digits is called Armstrong number.
# e.g. 153 = 1**3 + 5**3 + 3**3  = 1+125+27 =153
def is_armstrong():
    n = int(input("Enter The Number :->"))

    c = n
    su = 0
    while c > 0:
        last_digit = c % 10
        su += math.pow(last_digit, 3)
        c = c // 10

    if n == su:
        return True

    else:
        return False


# A palindromic number is a number that remains the same when its digits are reversed.
# reverse of no. is equal e.g. 12321 == 12321
def is_palindrome():
    n = int(input("Enter The Number :->"))

    c = n
    reverse = 0
    while c > 0:
        last_digit = c % 10
        reverse = reverse * 10 + last_digit
        c = c // 10

    if n == reverse:
        return True

    else:
        return False


# 25 = 25*25 = 6_25  An Automorphic number is a number whose square “ends” in the same digits as the number itself
def is_automorphic():
    n = int(input("Enter The Number :->"))

    sq = n * n
    times = 0
    c = n
    while c > 0:
        times += 1
        c = c // 10

    remain = sq % int(math.pow(10, times))

    if n == remain:
        return True

    else:
        return False


# In mathematics, a Niven number (or harshad number) in a given number base is
# an integer that is divisible by the sum of its digits when written in that base.
def is_niven():  # 81 = 8+1 =9
    n = int(input("Enter The Number :->"))

    c = n
    su = 0
    while c > 0:
        last_digit = c % 10
        su += last_digit
        c = c // 10

    if n % su == 0:
        return True

    else:
        return False


# A neon number is a number where the sum of digits of square of the number is equal to the number
#  For example if the input number is 9, its square is 9*9 = 81 and sum of the digits is 9. i.e. 9 is a neon number.
def is_neon():
    n = int(input("Enter The Number :->"))

    sq = n * n
    su = 0
    while sq > 0:
        last_digit = sq % 10
        su += last_digit
        sq = sq // 10

    if n == su:
        return True

    else:
        return False


# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
# For instance, 6 has divisors 1, 2 and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number
def is_perfect():
    n = int(input("Enter The Number :->"))
    su = 0

    for i in range(1, n):
        if n % i == 0:
            su += i

    if n == su:
        return True

    else:
        return False


def is_prime():  # has 2 factors
    n = int(input("Enter The Number :->"))

    fact = 0

    for i in range(1, n + 1):
        if n % i == 0:
            fact += 1

    if fact == 2:
        return True

    else:
        return False


def is_composite():  # has more than 2 factors
    n = int(input("Enter The Number :->"))

    fact = 0

    for i in range(1, n + 1):
        if n % i == 0:
            fact += 1

    if fact > 2:
        return True

    else:
        return False


def is_perfect_square():  # importing math module
    n = input("Enter The Number :->")
    bol = n.isdigit()

    if bol:
        n = int(n)
        root = math.sqrt(n)

        if int(root + 0.5) ** 2 == n:
            return True
        else:
            return False

    else:
        lis = list(n.split('.'))
        if len(lis[1]) % 2 == 0:
            n = f"{lis[0]}{lis[1]}"
            n = int(n)
            root = math.sqrt(n)

            if int(root + 0.5) ** 2 == n:
                return True
            else:
                return False

        else:
            return False


# A number is said to be Buzz Number if it ends with 7 or is divisible by 7. Example: 1007 is a Buzz Number.
def is_buzz():
    n = int(input("Enter The Number :->"))

    if n % 7 == 0 or n % 10 == 7:
        return True
    else:
        return False


# A circular prime is a prime number with the property that the number generated
# at each intermediate step when cyclically permuting its digits will be prime.
# For example, 1193 is a circular prime, since 1931, 9311 and 3119 all are also prime.
def is_circular_prime():
    n = int(input("Enter The Number :->"))

    def prime(num):
        fact = 0
        for j in range(1, num + 1):
            if num % j == 0:
                fact += 1

        if fact == 2:
            return True

        else:
            return False

    c = n
    times = 0
    while c > 0:
        times += 1
        c = c // 10

    c = n
    bol = True
    for i in range(times):
        if prime(c):
            last = c % 10
            first = c // 10
            c = (last * 10 ** (times - 1)) + first

        else:
            bol = False
            break

    if bol:
        return True

    else:
        return False


# Two integers a and b are said to be relatively prime, mutually prime, or co prime if the
# only positive integer that divides both of them is 1. Example: 13 and 15 are co prime.
def is_coprime():
    n1 = int(input("Enter The First Number :->"))
    n2 = int(input("Enter The Second Number :->"))

    if n1 < n2:
        mn = n1
    else:
        mn = n2

    gcd = 0
    for i in range(mn, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
            break

    if gcd == 1:
        return True
    else:
        return False


# A Duck number is a number which has zeroes present in it, but there should be no zero
# present in the beginning of the number. For example 3210 is  | 031 is not
def is_duck():
    n = input("Enter The Number :->")

    if int(n[0]) == 0:
        return False

    else:
        n = int(n)
        while n > 0:
            last = n % 10
            if last == 0:
                return True
            n = n // 10
        return False


# A happy number is a natural number in a given number base that eventually reaches 1 when iterated over
# the perfect digital invariant function for. Those numbers that do not end in 1 are -unhappy numbers.
def is_happy():
    n = int(input("Enter The Number :->"))
    if n == 1:
        return True

    r, su = 0, 0
    while n > 9:
        while n > 0:
            r = n % 10
            su += r
            n = n // 10

        n = su
        su = 0

    if n == 1:
        return True

    else:
        return False


# SAME AS ABOVE
# Magic number is the if the sum of its digits recursively are calculated
# till a single digit If the single digit is 1 then the number is a magic number.
def is_magic():
    n = int(input("Enter The Number :->"))
    if n == 1:
        return True

    r, su = 0, 0
    while n > 9:
        while n > 0:
            r = n % 10
            su += r
            n = n // 10

        n = su
        su = 0

    if n == 1:
        return True

    else:
        return False


# A spy number is a number where the sum of its digits equals the product of its digits
# For example, 1124 is a spy number, the sum of its digits is 1+1+2+4=8 and the product of its digits is 1*1*2*4=8.
def is_spy():
    n = int(input("Enter The Number :->"))

    su, pr = 0, 1
    while n > 0:
        r = n % 10
        su += r
        pr *= r
        n = n // 10

    if su == pr:
        return True
    else:
        return False


# A twin prime is a prime number that is either 2 less or 2 more than another prime number—for example,
# either member of the twin prime pair (41, 43). In other words, a twin prime is a prime that has a prime gap of two.
def is_twin_prime():
    n1 = int(input("Enter The First Number :->"))
    n2 = int(input("Enter The Second Number :->"))

    def prime(num):
        fact = 0
        for j in range(1, num + 1):
            if num % j == 0:
                fact += 1

        if fact == 2:
            return True

        else:
            return False

    if prime(n1) and prime(n2) and (n1 - n2 == 2 or n1 - n2 == -2):
        return True

    else:
        return False


# A number is called a twisted prime number if it is a prime number and reverse of this number is also a prime number.
def is_twisted_prime():
    n = int(input("Enter The Number :->"))

    def prime(num):
        fact = 0
        for j in range(1, num + 1):
            if num % j == 0:
                fact += 1

        if fact == 2:
            return True

        else:
            return False

    c = n
    reverse = 0
    while c > 0:
        last_digit = c % 10
        reverse = reverse * 10 + last_digit
        c = c // 10

    if prime(n) and prime(reverse):
        return True

    else:
        return False


# A number is said to be unique , if the digits in it are not repeated.
# For example, 12345 is a unique number. 123445 is not a unique number.
def is_unique():
    n = int(input("Enter The Number :->"))

    c = n
    times = 0
    while c > 0:
        times += 1
        c = c // 10

    lis = []
    t = n

    for i in range(times):
        last_digit = t % 10
        if last_digit in lis:
            return False
        else:
            lis.append(last_digit)
            t = t // 10

    return True


# A number is called Disarium number if the sum of its power of the positions from left to right is equal to the number.
# Example: 1 + 3*3 + 5*5*5 = 1 + 9 + 125 = 135
def is_disarium():
    n = int(input("Enter The Number :->"))

    c = n
    times = 0
    while c > 0:
        times += 1
        c = c // 10

    t, su = n, 0
    for i in range(1, times + 1):
        digit = t // int(math.pow(10, times - 1))
        su = su + int(math.pow(digit, i))
        t = t % int(math.pow(10, times - 1))
        times -= 1

    if su == n:
        return True
    else:
        return False


# A tech number can be tech number if its digits are even and the number of digits split into two number from middle
# then add these number if the added number’s square would be the same with the number it will called a Tech Number.
def is_tech():
    n = int(input("Enter The Number :->"))

    c = n
    times = 0
    while c > 0:
        times += 1
        c = c // 10

    if times % 2 == 0:
        first = n // int(math.pow(10, times // 2))
        second = n % int(math.pow(10, times // 2))
        n2 = first + second

        if n2 ** 2 == n:
            return True

    else:
        return False


# A number is said to be a pronic number if product of two consecutive integers is equal to the number,
#  is called a pronic number.Example- 42 is said to be a pronic number, 42=6×7, here 6 and 7 are consecutive integers
def is_pronic():
    n = int(input("Enter The Number :->"))

    c = 1
    while True:
        if c * (c + 1) == n:
            return True
        if c > n // 2:
            break

        c += 1

    return False


# A number is said to be an Ugly number if positive numbers whose prime factors only include 2, 3, 5.
# For example, 6(2×3), 8(2x2x2), 15(3×5) are ugly numbers while 14(2×7) is not ugly since it includes another
# prime factor 7. Note that 1 is typically treated as an ugly number.
# In this e.g.16 = 4*4 is not done 16 = 2*2*2*2 is done

def is_ugly():
    n = int(input("Enter The Number :->"))

    while n != 1:
        if n % 2 == 0:
            n = n // 2

        elif n % 3 == 0:
            n = n // 3

        elif n % 5 == 0:
            n = n // 5

        else:
            return False

    return True  # if n ==1 it will directly come here and return True


# A number is said to be special number when the sum of factorial of its digits is equal to the number itself.
# Example- 145 is a Special Number as 1!+4!+5!=145.

def is_special():
    n = int(input("Enter The Number :->"))

    def factorial(n2):
        if n2 == 0:
            return 1
        else:
            return n2 * factorial(n2 - 1)

    c = n
    su = 0
    while c > 0:
        last_digit = c % 10
        su += factorial(last_digit)
        c = c // 10

    if n == su:
        return True

    else:
        return False
