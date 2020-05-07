

def close(first_number, second_number, third_number):
    """
    Limit absolute difference between first two numbers to third number
    :param third_number:
    :param first_number: A number
    :param second_number: A number
    :return: A Boolean value
    """

    if abs(first_number - second_number) < third_number:
        return True
    if abs(first_number - second_number) >= third_number:
        return False


if __name__ == '__main__':

    test_1 = close(1, 2, 0.5)
    print(test_1)

    test_2 = close(2, 1, 0.5)
    print(test_2)

    test_3 = close(1, 2, 1)
    print(test_3)

    test_4 = close(1, 2, 3)
    print(test_4)

    print(type(test_4))
