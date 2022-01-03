STEPS = 1000

input_file = open('aoc_d11_in.txt')

line_counter = 0
input_dict = {}
for line in input_file:
    clean_line = line.rstrip('\n')
    column_counter = 0
    line_dict = {}
    for column in clean_line:
        line_dict[column_counter] = int(column)
        column_counter += 1

    input_dict[line_counter] = line_dict
    line_counter += 1

flash_counter_total = 0
for step in range(0, STEPS):
    flash_counter = 0
    for y in input_dict.keys():
        for x in input_dict[y].keys():
            input_dict[y][x] += 1

    while True:
        energy_counter = 0
        spread_coords = {}
        spread_counter = 0
        for y in input_dict.keys():
            for x in input_dict[y].keys():
                adjacent_coords = {}
                if input_dict[y][x] > 9:
                    input_dict[y][x] = 0
                    if y > 0:
                        adjacent_coords['0_angle'] = {'x_coord': x, 'y_coord': y - 1}
                        if x < len(input_dict[y]) - 1:
                            adjacent_coords['45_angle'] = {'x_coord': x + 1, 'y_coord': y - 1}

                        if x > 0:
                            adjacent_coords['315_angle'] = {'x_coord': x - 1, 'y_coord': y - 1}

                    if y < len(input_dict) - 1:
                        adjacent_coords['180_angle'] = {'x_coord': x, 'y_coord': y + 1}
                        if x < len(input_dict[y]) - 1:
                            adjacent_coords['135_angle'] = {'x_coord': x + 1, 'y_coord': y + 1}

                        if x > 0:
                            adjacent_coords['225_angle'] = {'x_coord': x - 1, 'y_coord': y + 1}

                    if x > 0:
                        adjacent_coords['270_angle'] = {'x_coord': x - 1, 'y_coord': y}

                    if x < len(input_dict[y]) - 1:
                        adjacent_coords['90_angle'] = {'x_coord': x + 1, 'y_coord': y}

                spread_coords[spread_counter] = adjacent_coords
                spread_counter += 1

        for a in spread_coords.keys():
            for b in spread_coords[a].keys():
                if input_dict[spread_coords[a][b]['y_coord']][spread_coords[a][b]['x_coord']] > 9:
                    pass
                elif input_dict[spread_coords[a][b]['y_coord']][spread_coords[a][b]['x_coord']] <= 9:
                    if input_dict[spread_coords[a][b]['y_coord']][spread_coords[a][b]['x_coord']] > 0:
                        input_dict[spread_coords[a][b]['y_coord']][spread_coords[a][b]['x_coord']] += 1
                        energy_counter += 1
                else:
                    print('Error Spread Processing')

        if energy_counter > 0:
            pass
        elif energy_counter == 0:
            break
        else:
            print('Error Energy Counter')

    for y in input_dict.keys():
        for x in input_dict[y].keys():
            if input_dict[y][x] == 0:
                flash_counter += 1
            elif input_dict[y][x] > 0:
                pass
            else:
                print('Error flash count')

    flash_counter_total += flash_counter
    if flash_counter == 100:
        print(f'Synchro Flash!!! Step {step + 1}')
    # print(f'Step {step}: {flash_counter} Flashes')

print(f'\nAfter {STEPS} steps there were {flash_counter_total} Flashes')





