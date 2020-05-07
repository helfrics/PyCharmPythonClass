import random
import sys

my_args = sys.argv
print(my_args)
name = sys.argv[1]
print(my_args)

if len(sys.argv) <= 1:
    print('Please enter a name when calling this file.')
    print('Example: python scratch.py Alex')
    sys.exit(0)

my_number = random.randint(1, 10)
if my_number < 3:
    luck = 'Band'
elif my_number < 7:
    luck = 'OK'
else:
    luck = 'Good'

print('Hello, {}'.format(name))
print('Your luck today is: {}'.format(luck))
