
input = open('aoc_d2_p1_in.txt')


depth = 0
horizon = 0
aim = 0


for command in input:
    split_command = command.split()
    split_value = split_command[1].split('\n')

    direction = split_command[0]
    value = int(split_value[0])

    if direction == 'forward':
        horizon += value
        depth += aim * value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    else:
        print(f'Error: Command was {command}')

    print(f'Depth at {depth}; Horizon at {horizon}')

print(f'\nFinal Depth: {depth}')
print(f'Final Horizon Position: {horizon}')

print(f'The solution is {depth * horizon}')


'''
for x in input:
    split_debug = x.split(' ')
    split_debug_2 = split_debug[1].split('\n')
    print(split_debug)
    print(split_debug_2)
    
'''