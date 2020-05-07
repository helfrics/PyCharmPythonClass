import csv
import math


def load_data_from_file(filename):
    """
    Make two lists from one file.
    :param filename: A string that calls a file
    :return: Two lists, first is time indexes, second is positions as floats
    """
    with open(filename, 'r') as f:
        csv_file = csv.reader(f)
        list_one = []
        list_two = []
        counter = 0
        for row in csv_file:
            if counter > 0:
                list_one.append(float(row[0]))
                list_two.append(float(row[1]))
            else:
                pass
            counter += 1
    return list_one, list_two


def greater_than_index(some_list, number):
    """
    Give position of first element in list greater than or equal to number.
    :param some_list: A list
    :param number: A number
    :return: A number
    """
    i = 0
    for item in some_list:
        if item < number:
            pass
        else:
            return i
        i += 1


def values(filename):
    """
    Extract initial, max, and final positions from file data.
    :param filename: A string that calls a file
    :return: A list
    """
    data = load_data_from_file(filename)
    positions = data[1]
    c_initial = positions[0]
    c_max = max(positions)
    c_final = positions[-1]
    c_values = [c_initial, c_max, c_final]
    return c_values


def characteristics(filename):
    """
    Calculate rise time, peak time, percentage overshoot, and settling time from file data.
    :param filename: A string that calls a file
    :return: A list
    """
    data = load_data_from_file(filename)
    times = data[0]
    positions = data[1]
    c_values = values(filename)
    relative_to_final = []
    for position in positions:
        position = abs(position - c_values[2])
        relative_to_final.append(position)
    relative_to_initial = []
    for place in positions:
        place = abs(place - c_values[0])
        relative_to_initial.append(place)
    ten_percent_position = abs(0.1 * c_values[2] - c_values[0])
    ninety_percent_position = abs(0.9 * c_values[2] - c_values[0])
    ten_percent_index = greater_than_index(relative_to_initial, ten_percent_position)
    ninety_percent_index = greater_than_index(relative_to_initial, ninety_percent_position)
    ten_percent_time = times[ten_percent_index]
    ninety_percent_time = times[ninety_percent_index]
    t_r = ninety_percent_time - ten_percent_time
    t_p = times[positions.index(c_values[1])]
    percent_overshoot = ((c_values[1] - c_values[2]) / (c_values[2] - c_values[0])) * 100
    threshold = abs(0.02 * (c_values[2] - c_values[0]))
    settling_index = greater_than_index(reversed(relative_to_final), threshold)
    t_s = times[-settling_index]
    c_times = (t_r, t_p, percent_overshoot, t_s)
    return c_times


def get_system_params(percent_overshoot, settling_time):
    """
    Calculate mass, spring, and damping constants.
    :param percent_overshoot: A float
    :param settling_time: A float
    :return: A list
    """
    zeta = -math.log(percent_overshoot/100) / (((math.pi ** 2) + (math.log(percent_overshoot/100) ** 2)) ** (1/2))
    omega_n = 4 / (zeta * settling_time)
    mass = 1
    spring = omega_n ** 2
    damping = 2 * zeta * omega_n
    params = (mass, spring, damping)
    return params


def analyze_data(filename):
    """
    Make a dictionary from file data.
    :param filename: A string that calls a file
    :return: A dictionary
    """
    c_values = values(filename)
    c_times = characteristics(filename)
    params = get_system_params(c_times[2], c_times[3])
    dictionary = {'c_initial': c_values[0], 'c_max': c_values[1], 'c_final': c_values[2], 'rise_time': c_times[0],
                  'peak_time': c_times[1], 'perc_overshoot': c_times[2], 'settling_time': c_times[3],
                  'system_mass': params[0], 'system_spring': params[1], 'system_damping': params[2]}
    return dictionary


if __name__ == '__main__':

    # test_list = [2, 6, 7, 38, 50, 61]
    # test_number = 38
    # print(test_list)
    # print(test_number)
    # print(greater_than_index(test_list, test_number))
    #
    # print(load_data_from_file('data1.csv'))
    print(values('data1.csv'))
    print(characteristics('data1.csv'))
    print(get_system_params(85.448, 19))
    # print(analyze_data('data1.csv'))
