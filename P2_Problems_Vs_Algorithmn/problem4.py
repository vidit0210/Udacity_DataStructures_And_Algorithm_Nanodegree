def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    l_0 = []
    l_1 = []
    l_2 = []
    data = []
    for l in input_list:
        if l == 0:
            l_0.append(l)
        elif l == 1:
            l_1.append(l)
        else:
            l_2.append(l)

    data = l_0 + l_1 + l_2

    return data


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2])
