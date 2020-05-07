import csv
from sensor import generate_sensor_data
from amp_filter import apply_amp_filter
from statistics import mean


def mean_filter(data, w=3):
    """
    Replace each reading with mean of a variable width subset in which reading is the center.
    :param data: A list of numbers
    :param w: A positive and odd number which is the subset width
    :return: A new list of numbers
    """

    filtered = []
    final_start = int(len(data) - w + 1)
    end = w

    for number in range(final_start):
        start = number
        subset = data[start:end]
        new_datum = mean(subset)
        filtered.append(new_datum)
        end += 1

    if w > len(data) or w < 0 or w % 2 == 0:
        raise ValueError

    return filtered


if __name__ == '__main__':

    sensor_data = generate_sensor_data(1000)
    amp_filter_data = apply_amp_filter(sensor_data)
    mean_data = mean_filter(amp_filter_data)
    all_data = zip(sensor_data[1:1000], amp_filter_data[1:1000], mean_data)

    with open('mean_filter.csv', 'w') as f:
        csv_file = csv.writer(f)
        csv_file.writerows(all_data)

    test_data = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    for i in range(-3, 11):
        try:
            new_data = mean_filter(test_data, i)
            print('For test_data and w =', i, 'output:', new_data)
        except ValueError:
            print('Exception thrown for: test_data and w =', i)
