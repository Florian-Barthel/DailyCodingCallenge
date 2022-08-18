import numpy as np

"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def solution(list_of_numbers, k):
    copy = list_of_numbers.copy()
    list_of_numbers = np.expand_dims(np.array(list_of_numbers), axis=-1)
    list_of_numbers = np.add(list_of_numbers.T, list_of_numbers) - k
    list_of_numbers = np.logical_not(list_of_numbers.astype(np.bool))

    sum_exists = np.any(list_of_numbers)
    if sum_exists:
        index = np.where(list_of_numbers)
        print('{} and {} can be added to reach {}.'.format(copy[index[0][0]], copy[index[0][1]], k))
    else:
        print('No sum exists.')


solution(list_of_numbers=[10, 4, 354, 723, 12, 11], k=23)
