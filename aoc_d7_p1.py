
def transform_int(x):
    return int(x)


input_file = open('aoc_d7_in.txt')


for y in input_file:
    input_raw = y
    input_positions = input_raw.split(',')
    input_positions = list(map(transform_int, input_positions))

min_position = min(input_positions)
max_position = max(input_positions)

solution_dic = {'final_position': None, 'final_fuel': 9999999999}

for target_position in range(min_position, max_position + 1):
    fuel_counter = 0
    progress_counter = 0
    for crab_sub in input_positions:
        shift_range = 0
        if crab_sub == target_position:
            pass
        elif crab_sub > target_position:
            shift_range = crab_sub - target_position
            fuel_counter += 0.5 * shift_range ** 2 + 0.5 * shift_range
        elif crab_sub < target_position:
            shift_range = target_position - crab_sub
            fuel_counter += 0.5 * shift_range ** 2 + 0.5 * shift_range
        else:
            print('Error Fuel Count')

        progress_counter += 1
        # print(f'{round(progress_counter / len(input_positions), 2)}%')

    if fuel_counter < solution_dic['final_fuel']:
        solution_dic['final_fuel'] = fuel_counter
        solution_dic['final_position'] = target_position
    elif fuel_counter > solution_dic['final_fuel']:
        pass
    elif fuel_counter == solution_dic['final_fuel']:
        pass
    else:
        print('Error solution check')

    print(f'{round(target_position / max_position, 2) * 100}%')

print(f'For Target Position {solution_dic["final_position"]}, the fuel required is {solution_dic["final_fuel"]}')
