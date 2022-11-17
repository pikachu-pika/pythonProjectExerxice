# PATTERN PRINTING

# no_rows=5  mostly

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def pattern1(no_rows):
    for rows in range(1, no_rows + 1):
        for columns in range(1, rows + 1):
            print(columns, end=" ")
        print()


# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

def pattern2(no_rows):
    for rows in range(1, no_rows + 1):
        for columns in range(no_rows, 0, -1):
            print(rows, end=' ')
        print()
        no_rows -= 1


# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

def pattern3(no_rows):
    for rows in range(no_rows, 0, -1):
        for columns in range(1, rows + 1):
            print(rows, end=' ')
        print()


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def pattern4(no_rows):
    for rows in range(no_rows, 0, -1):
        for columns in range(1, rows + 1):
            print(columns, end=' ')
        print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def pattern5(no_rows):
    for rows in range(1, no_rows + 1):
        for columns in range(1, rows + 1):
            print(rows, end=" ")
        print()


# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

def pattern6(no_rows):
    for rows in range(1, no_rows + 1):
        for columns in range(1, rows + 1):
            print(rows * 2 - 1, end=" ")
        print()


# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

def pattern7(no_rows):
    for rows in range(1, no_rows + 1):
        for columns in range(rows, 0, -1):
            print(columns, end=" ")
        print()


#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

def pattern8(no_rows):
    for rows in range(1, no_rows + 1):
        for spaces in range(1, (no_rows - rows) + 1):
            print(" ", end=" ")
        for columns in range(1, rows + 1):
            print(columns, end=" ")
        print()


#         1
#       2 2
#     3 3 3
#   4 4 4 4
# 5 5 5 5 5

def pattern9(no_rows):
    for rows in range(1, no_rows + 1):
        for spaces in range(1, (no_rows - rows) + 1):
            print(" ", end=" ")
        for columns in range(1, rows + 1):
            print(rows, end=" ")
        print()


#         5
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5

def pattern10(no_rows):
    for rows in range(no_rows, 0, -1):
        for spaces in range(1, rows):
            print(" ", end=" ")
        for columns in range(rows, no_rows + 1):
            print(columns, end=" ")
        print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def pattern11(no_rows):
    num = 1
    for rows in range(1, no_rows + 1):
        for columns in range(1, rows + 1):
            print(num, end=" ")
            num += 1
        print()


#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

def pattern12(no_rows):
    for rows in range(1, no_rows + 1):
        for spaces in range(1, (no_rows - rows) + 1):
            print(" ", end=" ")
        for columns in range(rows, 0, -1):
            print(columns, end=" ")
        for columns in range(2, rows + 1):
            print(columns, end=" ")
        print()


#         1
#       2 2 2
#     3 3 3 3 3
#   4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5

def pattern13(no_rows):
    for rows in range(1, no_rows + 1):
        for spaces in range(1, (no_rows - rows) + 1):
            print(" ", end=" ")
        for columns in range(1, rows * 2):  # (1,((rows*2)-1)+1)
            print(rows, end=" ")
        print()


#         5
#       4 5 4
#     3 4 5 4 3
#   2 3 4 5 4 3 2
# 1 2 3 4 5 4 3 2 1

def pattern14(no_rows):
    for rows in range(no_rows, 0, -1):
        for spaces in range(1, rows):
            print(" ", end=" ")
        for columns in range(rows, no_rows + 1):
            print(columns, end=" ")
        for columns in range(no_rows - 1, rows - 1, -1):
            print(columns, end=" ")
        print()


# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

def pattern15(no_rows):
    for rows in range(1, no_rows + 1):
        for columns in range(1, no_rows + 1):
            if columns <= rows:
                print(rows, end=" ")
            else:
                print(columns, end=" ")
        print()


# 1
# 2  4
# 3  6  9
# 4  8  12  16
# 5  10  15  20  25
# 6  12  18  24  30  36
# 7  14  21  28  35  42  49
# 8  16  24  32  40  48  56  64        # no_rows=8

def pattern16(no_rows):
    for rows in range(1, no_rows):
        for columns in range(1, rows + 1):
            print(rows * columns, end=" ")
        print()


# PASCAL'S TRIANGLE

#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1

def pascal_triangle(n):
    pas_list = []
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(pas_list[i - 1][j - 1] + pas_list[i - 1][j])
        pas_list.append(temp_list)
    return pas_list


def pattern17(no_rows):
    pas_list = pascal_triangle(no_rows)

    for rows in range(no_rows):
        for spaces in range(no_rows - rows - 1):
            print(format(" ", "<2"), end=" ")  # format func to print them properly

        for columns in pas_list[rows]:
            print(format(columns, "3"), end="   ")
        print()


#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * * * *

#   * * * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

def pattern18(no_rows):
    for rows in range(1, (no_rows // 2) + 1):
        for columns in range(rows):
            print("*", end=" ")
        print()

    print()
    for rows in range((no_rows // 2), 0, -1):
        for columns in range(rows):
            print("*", end=" ")
        print()


#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

def pattern19(no_rows):
    for rows in range(1, (no_rows // 2 + 1) + 1):
        for columns in range(rows):
            print("*", end=" ")
        print()

    for rows in range(no_rows // 2, 0, -1):
        for columns in range(rows):
            print("*", end=" ")
        print()


#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *


def pattern20(no_rows):
    for rows in range(1, (no_rows // 2 + 1) + 1):
        for spaces in range(no_rows - rows):
            print(" ", end=" ")

        for columns in range(rows):
            print("*", end=" ")
        print()

    for rows in range(no_rows // 2, 0, -1):
        for spaces in range(no_rows - rows):
            print(" ", end=" ")

        for columns in range(rows):
            print("*", end=" ")
        print()


#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *

def pattern21(no_rows):
    for rows in range(no_rows // 2, 0, -1):
        for spaces in range(no_rows // 2 - rows):
            print("", end=" ")

        for columns in range(rows):
            print("*", end=" ")
        print()

    for rows in range(1, no_rows // 2 + 1):
        for spaces in range(no_rows // 2 - rows):
            print("", end=" ")

        for columns in range(rows):
            print("*", end=" ")
        print()


#         *
#        * *
#       * * *
#      * * * *
#     * * * * *
#    * * * * * *
#     * * * * *
#      * * * *
#       * * *
#        * *
#         *


def pattern22(no_rows):
    for rows in range(1, no_rows // 2 + 1):
        for spaces in range(no_rows // 2 - rows):
            print("", end=" ")

        for columns in range(rows):
            print("*", end=" ")
        print()

    for rows in range(no_rows // 2 - 1, 0, -1):
        for spaces in range(no_rows // 2 - rows):
            print("", end=" ")

        for columns in range(rows):
            print("*", end=" ")
        print()


#       *
#      * *
#     *   *
#    *     *
#   *       *
#    *     *
#     *   *
#      * *
#       *


def pattern23(no_rows):
    for rows in range(1, no_rows // 2 + 1):
        for spaces in range(no_rows // 2 - rows):
            print("", end=" ")

        for columns in range(1, rows + 1):
            if columns == 1 or columns == rows:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    for rows in range(no_rows // 2 - 1, 0, -1):
        for spaces in range(no_rows // 2 - rows):
            print("", end=" ")

        for columns in range(1, rows + 1):
            if columns == 1 or columns == rows:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# A
# B C
# D E F
# G H I J
# K L M N O
# P Q R S T U
# V W X Y Z [ \

def pattern24(no_rows):
    num = 65
    for rows in range(1, no_rows + 1):
        for columns in range(1, rows + 1):
            print(chr(num), end=" ")
            num += 1
        print()


# P
# Py
# Pyt
# Pyth
# Pytho
# Python

# Displays until  full word
def pattern25(word):
    word = str(word)
    x = ""
    for i in word:
        x += i
        print(x)


# Displays till entered by user or till full word
def pattern26(no_rows, word):
    word = str(word)
    for rows in range(1, no_rows + 1):
        if len(word) >= rows:
            print(word[:rows])
        else:
            break


#   1 * 2 * 3 * 4
#
#   1 * 2 * 3
#
#   1 * 2
#
#   1

def pattern27(no_rows):
    for rows in range(no_rows):
        c = 1
        print(c, end=" ")
        for columns in range(no_rows - rows - 1, 0, -1):
            print("*", end=" ")
            c += 1
            print(c, end=" ")
        print("\n")


# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def pattern28(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lis = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        lis.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print('\n'.join(lis[:0:-1] + lis))


# H
# HE
# HEL
# HELL
# HELLO

def pattern29(letter):
    for end in range(0, len(letter) + 1):
        print(letter[0:end])


# HELLO
# HELL
# HEL
# HE
# H

def pattern30(letter):
    for end in range(len(letter), 0, -1):
        print(letter[0:end])


# O
# LO
# LLO
# ELLO
# HELLO

def pattern31(letter):
    for start in range(len(letter), -1, -1):
        print(letter[start:len(letter)])

# def pattern(no_rows):
#     for rows in range():
#         for columns in range():
#             print(, end=" ")
#         print()
