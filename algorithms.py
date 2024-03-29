# without index
def linear_search1(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return True

    return False


# with index
def linear_search2(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return f'Found At Index {i}'

    return 'Not Found'


# multiple indexes
def linear_search3(lst, n):
    index = []
    for i in range(len(lst)):
        if lst[i] == n:
            index.append(i)
    if index is None:
        return 'Not Found'
    else:
        return f'Found At Indexes {index}'


# without index
def binary_search1(lst, n):
    lst.sort()
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        if lst[mid] == n:
            return True

        else:
            if lst[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1

    return False


# with index
def binary_search2(lst, n):  # list must be sorted to get index
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        if lst[mid] == n:
            return f'Found At Index {mid}'

        else:
            if lst[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1

    return 'Not Found'
