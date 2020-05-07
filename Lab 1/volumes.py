from math import pi


def cylinder_volume(radius, height):
    """
    Calculate the volume of a cylinder
    :param radius: A positive number
    :param height: A positive number
    :return: A positive number
    """

    if radius < 0:
        raise ValueError('Radius cannot be negative')
    if height < 0:
        raise ValueError('Height cannot be negative')

    return pi * radius ** 2 * height


def torus_volume(inner_radius, outer_radius):
    """
    Calculate the volume of a torus
    :param inner_radius: A positive number
    :param outer_radius: A positive number
    :return: A positive number
    """

    if inner_radius < 0:
        raise ValueError('Inner radius cannot be negative')
    if outer_radius < 0:
        raise ValueError('Outer radius cannot be negative')
    if inner_radius > outer_radius:
        raise ValueError

    return 2 * pi ** 2 * ((outer_radius - inner_radius) / 2) ** 2 * (outer_radius - (outer_radius - inner_radius) / 2)


if __name__ == '__main__':

    try:
        print(cylinder_volume(3, 5))
    except ValueError:
        print('Cylinder code exception')

    try:
        print(torus_volume(3, -4))
    except ValueError:
        print('Torus code exception')
