"""
You have a bag containing tiles with numbers [1, 2, 3, …, n] written on them.
Each number appears exactly once, so there are n tiles and n numbers. Now, without looking,
k number tiles are randomly picked out of the bag and discarded. Create a missing_nos() function that takes
in a list and k, and returns the missing numbers in ascending order (from smallest to greatest).

For example, missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2) should return [3, 9].
"""


def missing_nos(arr, k):
    a = arr.copy()
    b = []
    for i in range(len(a) - 1):
        if ((a[i + 1]) - a[i]) != 1:
            b.append(a[i] + 1)
    if len(b) != k:
        return print('Length of list not matching number of missing tiles!')

    b.sort()
    return b


print(missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2))