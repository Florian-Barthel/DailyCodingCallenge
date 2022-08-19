import numpy as np

"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def solution(list_of_numbers, k):
    array_of_numbers = np.expand_dims(np.array(list_of_numbers), axis=-1)
    combination_array = np.add(array_of_numbers.T, array_of_numbers) - k
    combination_array = np.logical_not(combination_array.astype(np.bool))
    sum_exists = np.any(combination_array)

    if sum_exists:
        index = np.where(combination_array)
        print('{} and {} can be added to reach {}.'.format(
            list_of_numbers[index[0][0]],
            list_of_numbers[index[0][1]],
            k)
        )
    else:
        print('No sum exists.')


solution(list_of_numbers=[10, 4, 354, 723, 12, 11], k=23)
