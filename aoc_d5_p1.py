# function to filter out the data set separator
def no_sep(a):
    return a != '->'


BOARD_SIZE = 1000
INPUT_SIZE = 500

input_d5 = open('aoc_d5_in.txt')

# start of parsing input data into a dictionary
valves_dict = {}
line_counter = 0
for lines_in in input_d5:
    valves_raw = list(filter(no_sep, lines_in.rstrip('\n').split(' ')))
    # print(valves_raw)
    start = valves_raw[0].split(',')
    end = valves_raw[1].split(',')

    valves_sing = {}
    valves_sing['x_start'] = int(start[0])
    valves_sing['y_start'] = int(start[1])
    valves_sing['x_end'] = int(end[0])
    valves_sing['y_end'] = int(end[1])

    valves_dict[str(line_counter)] = valves_sing
    line_counter += 1
# end of parsing input data into dictionary

# start of filtering out data points from diagonal vents
cross_valve_dict = {}
for x in range(0, INPUT_SIZE):
    if valves_dict[str(x)]['x_start'] != valves_dict[str(x)]['x_end']:
        if valves_dict[str(x)]['y_start'] != valves_dict[str(x)]['y_end']:
            cross_valve_dict[str(x)] = valves_dict[str(x)]
            del valves_dict[str(x)]

        elif valves_dict[str(x)]['y_start'] == valves_dict[str(x)]['y_end']:
            pass

        else:
            print('Error y clean')

    elif valves_dict[str(x)]['x_start'] == valves_dict[str(x)]['x_end']:
        pass

    else:
        print('Error x clean')
# end of filtering out data points from diagonal vents

# start setting up a board of the sea floor
sea_map = {}
for layer_1 in range(0, BOARD_SIZE):
    layer_map = {}
    for slice_1 in range(0, BOARD_SIZE):
        layer_map[slice_1] = 0
    sea_map[layer_1] = layer_map
# end setting up a board of the sea floor

# print(cross_valve_dict)
# start placing vents on the board of the sea floor
for valve_key in valves_dict.keys():
    if valves_dict[valve_key]['x_start'] == valves_dict[valve_key]['x_end']:
        if valves_dict[valve_key]['y_start'] < valves_dict[valve_key]['y_end']:
            for position_1 in range(int(valves_dict[valve_key]['y_start']), int(valves_dict[valve_key]['y_end'])+1):
                sea_map[position_1][int(valves_dict[valve_key]['x_start'])] += 1

        elif valves_dict[valve_key]['y_start'] > valves_dict[valve_key]['y_end']:
            for position_2 in range(int(valves_dict[valve_key]['y_end']), int(valves_dict[valve_key]['y_start'])+1):
                sea_map[position_2][int(valves_dict[valve_key]['x_start'])] += 1

        else:
            print('Error y mapping')

    elif valves_dict[valve_key]['y_start'] == valves_dict[valve_key]['y_end']:
        if valves_dict[valve_key]['x_start'] < valves_dict[valve_key]['x_end']:
            for position_3 in range(int(valves_dict[valve_key]['x_start']), int(valves_dict[valve_key]['x_end'])+1):
                sea_map[int(valves_dict[valve_key]['y_start'])][position_3] += 1

        elif valves_dict[valve_key]['x_start'] > valves_dict[valve_key]['x_end']:
            for position_4 in range(int(valves_dict[valve_key]['x_end']), int(valves_dict[valve_key]['x_start'])+1):
                sea_map[int(valves_dict[valve_key]['y_start'])][position_4] += 1

        else:
            print('Error x mapping')

    else:
        print('Error overall mapping')
# end placing vents on the board of the sea floor

# start placing the cross valves
for cross_valve_keys in cross_valve_dict.keys():
    if cross_valve_dict[cross_valve_keys]['x_start'] > cross_valve_dict[cross_valve_keys]['x_end']:
        if cross_valve_dict[cross_valve_keys]['y_start'] > cross_valve_dict[cross_valve_keys]['y_end']:
            span = cross_valve_dict[cross_valve_keys]['x_start'] - cross_valve_dict[cross_valve_keys]['x_end']
            for span_round in range(0, span + 1):
                sea_map[cross_valve_dict[cross_valve_keys]['y_start'] - span_round][cross_valve_dict[cross_valve_keys]['x_start'] - span_round] += 1

        elif cross_valve_dict[cross_valve_keys]['y_start'] < cross_valve_dict[cross_valve_keys]['y_end']:
            span = cross_valve_dict[cross_valve_keys]['x_start'] - cross_valve_dict[cross_valve_keys]['x_end']
            for span_round in range(0, span + 1):
                sea_map[cross_valve_dict[cross_valve_keys]['y_start'] + span_round][cross_valve_dict[cross_valve_keys]['x_start'] - span_round] += 1

        else:
            print('Error Cross X Start high')

    elif cross_valve_dict[cross_valve_keys]['x_start'] < cross_valve_dict[cross_valve_keys]['x_end']:
        if cross_valve_dict[cross_valve_keys]['y_start'] > cross_valve_dict[cross_valve_keys]['y_end']:
            span = cross_valve_dict[cross_valve_keys]['x_end'] - cross_valve_dict[cross_valve_keys]['x_start']
            for span_round in range(0, span + 1):
                sea_map[cross_valve_dict[cross_valve_keys]['y_start'] - span_round][cross_valve_dict[cross_valve_keys]['x_start'] + span_round] += 1

        elif cross_valve_dict[cross_valve_keys]['y_start'] < cross_valve_dict[cross_valve_keys]['y_end']:
            span = cross_valve_dict[cross_valve_keys]['x_end'] - cross_valve_dict[cross_valve_keys]['x_start']
            for span_round in range(0, span + 1):
                sea_map[cross_valve_dict[cross_valve_keys]['y_start'] + span_round][cross_valve_dict[cross_valve_keys]['x_start'] + span_round] += 1
                # print('Piep')
                # print(f'Accessing Point {cross_valve_dict[cross_valve_keys]["x_start"] + span_round}:{cross_valve_dict[cross_valve_keys]["y_start"] + span_round}')

        else:
            print('Error Cross X Start low')

    else:
        print('Error Cross')

    # print(cross_valve_dict[cross_valve_keys])

# start of counting spots with multiple vents
solution_counter = 0        # counts number of spots with more then 1 vent
one_counter = 0             # counts number of spots with one vent (debugging purpose)
zero_counter = 0            # counts number of spots with no vents (debugging purpose)
check_counter = 0           # counts number of spots checked for vents (debugging purpose)
for layer_2 in range(0, BOARD_SIZE):
    for slice_2 in range(0, BOARD_SIZE):
        if sea_map[layer_2][slice_2] >= 2:
            solution_counter += 1
            # print(sea_map[layer_2][slice_2])

        elif sea_map[layer_2][slice_2] == 1:
            one_counter += 1

        elif sea_map[layer_2][slice_2] == 0:
            zero_counter += 1

        else:
            print('Error solution calc')
        check_counter += 1
    # print(f'Detected multi valves on {solution_counter} / {check_counter} Valves')
# end counting spots with multiple valves


print(f'\nThe Solution is {solution_counter}')                              # prints out the solution
print(f'\nCheck Sum is {solution_counter + one_counter + zero_counter}')    # prints out is check sum (debugging)
print(f'Healthy check sum is {check_counter}\n')                            # prints out the set point check sum (debugging)

# for z in sea_map.keys():
#     print(sea_map[z].values())

# print(sea_map[589])
