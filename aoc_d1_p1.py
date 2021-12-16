

input = open('aoc_d1_p1_in.txt')


x = None
y = None
counter = 0

for depth in input:

    y = x
    x = depth

    if y != None:
        if x > y:
            counter += 1
            print(f'{x} - Increase - Counter: {counter}')
        elif x < y:
            print('Decrease')
        else:
            print('Level')

print(f'\n{counter} Increases in depth have been registered')

input.close()


