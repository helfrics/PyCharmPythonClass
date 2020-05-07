def reverse_r(some_list):
    """
    Reverse order of some list using recursion
    :param some_list: A list
    :return: A new list
    """

    if not some_list:
        return some_list
    else:
        return some_list[-1:] + reverse_r(some_list[:-1])


def reverse_i(some_list):
    """
    Reverse order of some list using iteration
    :param some_list: A list
    :return: A new list
    """

    position = len(some_list) - 1
    new_list = []

    while position >= 0:
        new_list.append(some_list[position])
        position -= 1
    return new_list


if __name__ == '__main__':

    number_list = [1, 2, 3, 4, 5, 6]
    letter_list = ['a', 'b', 'coin', 'd', 'e']

    print('Original:', number_list)
    print('reverse_r:', reverse_r(number_list))
    print('reverse_i:', reverse_i(number_list))
    print('Original:', letter_list)
    print('reverse_r:', reverse_r(letter_list))
    print('reverse_i:', reverse_i(letter_list))
