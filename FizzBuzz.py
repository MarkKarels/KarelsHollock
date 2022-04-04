"""
Write a fizzbuzz() function that takes in a number, n, and returns a list of the numbers from 1 to n.
For multiples of three, use "Fizz" instead of the number, and for the multiples of five, use "Buzz".
For numbers that are multiples of both three and five, use "FizzBuzz" (capitalization matters).

For example, fizzbuzz(16) should return
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16].
"""


def fizzbuzz(limit):
    lst = []
    count = 1
    for i in range(limit):
        if count % 3 != 0 and count % 5 != 0:
            lst.append(count)
            count += 1
        elif count % 3 == 0 and count % 5 != 0:
            lst.append("Fizz")
            count += 1
        elif count % 3 != 0 and count % 5 == 0:
            lst.append("Buzz")
            count += 1
        else:
            lst.append("FizzBuzz")
            count += 1

    return lst


print(fizzbuzz(16))