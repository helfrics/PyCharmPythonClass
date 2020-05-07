def fibonacci(x):
    if x <= 2:
        return 1

    return fibonacci(x - 2) + fibonacci(x - 1)


"""
x:    1 2 3 4 5 6 7  8
f(x): 1 1 2 3 5 8 13 21
"""


with open('file name', 'access mode') as fh:
    fh.write('apple')

# read groceries file
with open('groceries.txt', 'r') as fh:
    text = fh.readlines()

# below is similar but with issues because
# fh = open('groceries.txt', 'r')
# text = fh.read()
# fh.close()

# write to groceries file
# with open('groceries.txt', 'w') as fh:

modified_list = [item.strip() for item in my_shopping_list]

for item in modified_list:
    if item == 'fish':
        print('What kind of fish')

if __name__ == '__main__':

    my_list = ['apples', 'bananas', 'oranges']
    length = len(my_list)
    first = my_list[0]
    print(first, length)

    for i in range(len(my_list)):
        print(my_list[i])
    for item in my_list:
        print(item)

    num_list = list(range(100))
    print(num_list[0:5])
    print(num_list[30:-30])

    what_append = my_list.append('peaches')
    what_extend = my_list.extend('peaches')
    print(what_append, what_extend)

    print(fibonacci(3))
