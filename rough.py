# import re
#
# card_no = []
#
# n = int(input())
# for i in range(n):
#     no = input()
#     card_no.append(no)
#
#
# for i in card_no:
#     if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", i) and not re.search(r"([\d])\1\1\1", i.replace("-", "")):
#         print("Valid")
#     else:
#         print("Invalid")

# regex_integer_in_range = r"[1-9][0-9]{5}"	# Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


# import re
# P = input()
#
# print (bool(re.match(regex_integer_in_range, P))
#        and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#
#
# first_multiple_input = input().rstrip().split()
#
# n = int(first_multiple_input[0])
#
# m = int(first_multiple_input[1])
#
# matrix = []
#
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)
#
# text = [line[i] for i in range(m) for line in matrix]
# text = ''.join(text)
#
# pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
# text = re.sub(pattern,r'\1 ', text)
# print(text)


# if __name__ == '__main__':
#     n = int(input())
#     arr = list(set(map(int, input().split())))
#
#     arr.sort(reverse=True)
#     print(arr[1])

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     sum_=list(student_marks.get(query_name))
#     if len(sum_)==0:
#         print(0)
#     else:
#         av=int(sum(sum_))/len(sum_)
#         print(("%.2f" % av) )

# import re
#
# def count_substring(string, sub_string):
#     matches = re.findall("(?=" + re.excape(sub_string) + ")",string)
#     return len(matches)
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

# x,y,z,n= [int(input()) for _ in range(4)]
# print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1)])





