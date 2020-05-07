def sum_i(some_list):
    """
    Sum contents of some list using for loop.
    :param some_list: A list of numbers
    :return: A number
    """

    instant_sum = 0

    for number in some_list:
        instant_sum += number
    return instant_sum


def sum_r(some_list):
    """
    Sum contents of some list using recursion.
    :param some_list: A list of numbers
    :return: A number
    """

    if len(some_list) == 1:
        return some_list[0]
    else:
        return some_list[0] + sum_r(some_list[1:])


if __name__ == '__main__':

    test_list = [5, 12, -2, 6, 8]
    expected = sum(test_list)
    result_i = sum_i(test_list)
    result_r = sum_r(test_list)

    if expected != result_i:
        print('The iterative function does not match the built-in function.')
    else:
        print(result_i)

    if expected != result_r:
        print('The recursive function does not match the built-in function.')
    else:
        print(result_r)
