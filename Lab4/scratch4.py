import numpy as np
import random
import time
import matplotlib.pyplot as plt
import json

a = np.array([1, 2, 3])
b = np.array([3, -2, 5])
c = a + b

# Endpoint inclusive while most Python excludes endpoint
random.uniform(2, 25)
random.randint(2, 35)
random.choice(['Win', 'Lose', 'Draw'])
np.random.normal(0, 1)
np.random.normal(0, 1, 100)
np.random.normal(0, 1, (100, 3))

time.time()
# Pauses script for 2 seconds
time.sleep(2)
# DO NOT DO one liners as follows, but just get the idea:
# start = time.time(); time.sleep(2); end = time.time(); print(end - start)

times = np.linspace(0, 10, 1000)
values = np.sin(np.pi * times)
noise_values = values + np.random.normal(0, 0.05, 1000)

plt.plot(times, noise_values, linewidth=2, color='mediumaquamarine', label='Noise')
plt.plot(times, values, linestyle='dashed', label='Orig')
plt.title('Signal Analysis')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.legend()
plt.ylim(-1.0, 1.0)
# plt.show()
# OR DO:
plt.savefig('my_graph.png')

# NOW FOR HW2 json files (formatted with lists and dictionaries)
# see json-data.py in GitHub stuff
# use 'import requests' to get info into dict format for python when you query a website
# result = requests.get('https://tools.leaningcontainer.com/sample-json.json)
# pass and debug for info about how it worked out, what it retrieved
# user_data = result.json() will turn results into a json file

with open('donuts.json', 'r') as file:
    data = json.load(file)

condensed_dict = {}
for donut in data:
    print('For {} donuts, can have toppings:'.format(donut['name']))
    toppings = [topping_data['type'] for topping_data in donut['topping']]
    # for topping in toppings:
    #     print('\t{}'.format(topping))
    condensed_dict[donut['name']] = toppings

with open('donuts_condensed.json', 'w') as file:
    json.dump(condensed_dict, file)

if __name__ == '__main__':
    print(c)
