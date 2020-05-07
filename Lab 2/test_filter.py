import csv
from sensor import generate_sensor_data
from amp_filter import apply_amp_filter

if __name__ == '__main__':

    # Generate 1000 points of sensor data, then run them through the amp filter
    # then zip to get first column as sensor data and second column as (amp) filtered sensor data.
    sensor_data = generate_sensor_data(1000)
    amp_filter_data = apply_amp_filter(sensor_data)
    data = zip(sensor_data, amp_filter_data)

    with open('filter.csv', 'w') as f:
        csv_file = csv.writer(f)
        csv_file.writerows(data)

        # An alternative to 'csv_file.writerows(data)' would have been:
        # for row in data:
        #     csv_file.writerow(row)
