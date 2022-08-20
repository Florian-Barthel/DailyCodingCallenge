import numpy as np

"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all 
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was 
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def solution_with_division(array_of_int: np.ndarray):
    product = np.prod(array_of_int)
    return product // array_of_int


def solution_without_division(array_of_int: np.ndarray):
    result = np.zeros(array_of_int.shape, dtype=int)
    iterator = np.nditer(array_of_int, flags=['multi_index'])
    for _ in iterator:
        removed = array_of_int.copy()
        removed[iterator.multi_index] = 1
        result[iterator.multi_index] = np.prod(removed)
    return result


if __name__ == '__main__':
    test_array = np.array(
        [[3, 2, 1],
         [2, 5, 1]]
    )
    print(solution_with_division(test_array))
    print(solution_without_division(test_array))
