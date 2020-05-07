import math


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


print_lyrics()


def print_twice(bruce):
    print(bruce)
    print(bruce)


print_twice('Jim')
print_twice(math.pi)


# Function with one parameter (fixed quantity)


def compute_total(price):
    """
    Computes total price of items
    :param price: A positive number
    :return: A number
    """

    quantity = 20
    return price * quantity


if __name__ == '__main__':
    item_price = 1.1326
    expected_total = 22.65
    computed_total = compute_total(item_price)

    if computed_total == expected_total:
        print("Test looks good.")
    else:
        print("Test failed.")

# Includes absolute tolerance below.

    if math.isclose(computed_total, expected_total, abs_tol=1e-2):
        print(computed_total)
    else:
        print("Test failed.")


# Function with two parameters.


def compute_total_2(price_2, quantity_2=10.0):
    """
    Computes total price of items
    :param price_2: A positive number
    :param quantity_2: A number
    :return: A number
    """
    return price_2 * quantity_2


if __name__ == '__main__':
    item_price_2 = 3.79
    item_quantity_2 = 5.31
    expected_total_2 = 20.125
    computed_total_2 = compute_total_2(item_price_2, item_quantity_2)

    if math.isclose(computed_total_2, expected_total_2, abs_tol=1e-4):
        print(computed_total_2)
    else:
        print("Test failed.")
