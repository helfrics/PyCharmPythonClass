

def gcd(a, b):
    """
    Find the greatest common divisor
    :param a: a positive integer
    :param b: a positive integer
    :return: an integer
    """

    if a < 0:
        raise ValueError
    if b < 0:
        raise ValueError

    while b != 0:
        (a, b) = (b, a % b)
    return a


if __name__ == '__main__':

    from math import gcd as god
    import random

    random_integers_list_x = random.sample(range(0, 500), 25)
    random_integers_list_y = random.sample(range(0, 500), 40)

    for x in random_integers_list_x:

        for y in random_integers_list_y:

            expected = god(x, y)
            result = gcd(x, y)

            if expected != result:
                print('gcd failed for {0} and {1}'.format(x, y))
            else:
                print(expected, result)

    try:
        gcd(-200, 45)
        print('gcd failed to throw an exception for a negative')
    except ValueError:
        pass

    print('tests complete')
