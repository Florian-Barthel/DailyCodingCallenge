from math import inf

"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers
as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def solution(array_of_integer):

    # add an additional element to the list, so that each list index corresponds to one possible solution
    array_of_integer.append(inf)
    for i in range(len(array_of_integer)):

        # replace the number at the index of the current number with -inf
        # store the replaced number in swap_number and repeat with that number
        # until the swap_number is not a index of the list
        while 0 < array_of_integer[i] < len(array_of_integer):
            if i + 1 == array_of_integer[i]:
                array_of_integer[i] = -inf
                break
            if array_of_integer[array_of_integer[i] - 1]:
                swap_number = array_of_integer[array_of_integer[i] - 1]
                array_of_integer[array_of_integer[i] - 1] = -inf
                if 0 < swap_number < len(array_of_integer):
                    array_of_integer[i] = swap_number
                else:
                    break

        if array_of_integer[i] < 1 and array_of_integer[i] != -inf:
            array_of_integer[i] = inf

    # return the index (+1) of the first element that is not negative
    for i in range(len(array_of_integer)):
        if array_of_integer[i] > 0:
            return i + 1
    return len(array_of_integer)


if __name__ == '__main__':
    assert solution([3, 4, -1, 1]) == 2
    assert solution([1, 2, 0]) == 3
