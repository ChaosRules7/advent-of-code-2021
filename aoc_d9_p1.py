
WIDTH = 10
HEIGHT = 5

input_file = open('aoc_d9_in.txt')

line_counter = 0
input_dict = {}
for x in input_file:
    input_line = x.rstrip('\n')
    line_dict = {}
    position_counter = 0
    for y in input_line:
        line_dict[position_counter] = int(y)
        position_counter += 1

    input_dict[line_counter] = line_dict
    line_counter += 1

# for z in range(0, HEIGHT):
#     print(input_dict[z].values())

solution_counter = 0
debug_low_points = 0
debug_rest = 0
for row in range(0, len(input_dict)):
    for column in range(0, len(input_dict[0])):
        current_position = input_dict[row][column]
        low_point_counter = False
        if column - 1 >= 0:
            if input_dict[row][column-1] <= current_position:
                low_point_counter = True
            elif input_dict[row][column-1] > current_position:
                pass
            else:
                print('Error')

        if column + 1 < len(input_dict[0]):
            if input_dict[row][column+1] <= current_position:
                low_point_counter = True
            elif input_dict[row][column+1] > current_position:
                pass
            else:
                print('Error')

        if row - 1 >= 0:
            if input_dict[row-1][column] <= current_position:
                low_point_counter = True
            elif input_dict[row-1][column] > current_position:
                pass
            else:
                print('Error')

        if row + 1 < len(input_dict):
            if input_dict[row+1][column] <= current_position:
                low_point_counter = True
            elif input_dict[row+1][column] > current_position:
                pass
            else:
                print('Error')

        if not low_point_counter:
            solution_counter += 1 + current_position
            debug_low_points += 1
            # print(f'Row: {row} - Column: {column}')
        elif low_point_counter:
            debug_rest += 1
        else:
            print('Error Count')


print(f'The Solution is {solution_counter}')
print(f'\nLow Points: {debug_low_points}')
print(f'Not Low Points: {debug_rest}')
print(f'Control sum: {debug_rest + debug_low_points}')
