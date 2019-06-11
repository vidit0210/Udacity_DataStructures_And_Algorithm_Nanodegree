import random


def get_min_max(arr):
    min = arr[0]
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
        if n < min:
            min = n

    return(min, max)


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)


print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 10)]
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 10)]
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 10)]
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 10)]
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 10)]
random.shuffle(l)
