def mergeSort(L, ascending=True):
    result = []
    if len(L) == 1:
        return L
    mid = len(L) // 2

    teilliste1 = mergeSort(L[:mid])

    teilliste2 = mergeSort(L[mid:])

    x, y = 0, 0
    while x < len(teilliste1) and y < len(teilliste2):
        if teilliste1[x] > teilliste2[y]:
            result.append(teilliste2[y])
            y = y + 1

        else:
            result.append(teilliste1[x])
            x = x + 1

    result = result + teilliste1[x:]

    result = result + teilliste2[y:]
    if ascending == True:
        return result
    else:
        result.reverse()
        return result


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = mergeSort(input_list, False)
    x = 0
    y = 0
    for i in range(len(input_list)):
        if(i % 2 == 0):
            x = x * 10 + input_list[i]
        else:
            y = y * 10 + input_list[i]
    return x, y


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case = [[4, 11, 2, 5, 9, 8], [9114, 852]]
test_case = [[4, 6, 2, 5, 9, 7], [964, 752]]
test_case = [[3, 6, 2, 5, 9, 7], [963, 752]]
