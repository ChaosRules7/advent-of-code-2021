import re

file_input = open('aoc_d8_in.txt')

dict_counter = 0
input_dict = {}
for x in file_input:
    raw_input = x
    sep_input = raw_input.split('|')

    example_raw = sep_input[0].split(' ')
    output_raw = sep_input[1].split(' ')

    example_fine = []
    for y in range(0, 10):
        example_fine.append(example_raw[y])

    output_fine = []
    for z in range(1, 5):
        output_fine.append(output_raw[z].rstrip('\n'))

    build_dict = {'input_values': example_fine, 'output_values': output_fine}
    input_dict[dict_counter] = build_dict
    dict_counter += 1

solution_counter = 0
for main_clock in range(0, len(input_dict)):
    print(f'Line {main_clock}')
    # print(input_dict[main_clock]['output_values'])
    for sub_clock_01 in range(0, 10):
        if len(input_dict[main_clock]['input_values'][sub_clock_01]) == 2:
            input_dict[main_clock][1] = input_dict[main_clock]['input_values'][sub_clock_01]
            # print(input_dict[main_clock][1])

        elif len(input_dict[main_clock]['input_values'][sub_clock_01]) == 3:
            input_dict[main_clock][7] = input_dict[main_clock]['input_values'][sub_clock_01]
            # print(input_dict[main_clock][7])

        elif len(input_dict[main_clock]['input_values'][sub_clock_01]) == 4:
            input_dict[main_clock][4] = input_dict[main_clock]['input_values'][sub_clock_01]
            # print(input_dict[main_clock][4])

        elif len(input_dict[main_clock]['input_values'][sub_clock_01]) == 7:
            input_dict[main_clock][8] = input_dict[main_clock]['input_values'][sub_clock_01]

    pattern = re.compile(rf'(\w*)([{input_dict[main_clock][1]}])(\w*)([{input_dict[main_clock][1]}])(\w*)')
    input_dict[main_clock]['a'] = pattern.sub(r'\1\3\5', input_dict[main_clock][7])
    # print(input_dict[main_clock]['a'])

    input_dict[main_clock]['bd'] = pattern.sub(r'\1\3\5', input_dict[main_clock][4])
    # print(input_dict[main_clock]['bd'])

    for sub_clock_02 in range(0,10):
        entry = input_dict[main_clock]['input_values'][sub_clock_02]
        if len(entry) == 5:
            if input_dict[main_clock][1][0] in entry and input_dict[main_clock][1][1] in entry:
                input_dict[main_clock][3] = entry
                for letter in entry:
                    if letter == input_dict[main_clock]['a']:
                        pass
                    elif letter == input_dict[main_clock][1][0]:
                        pass
                    elif letter == input_dict[main_clock][1][1]:
                        pass
                    elif letter == input_dict[main_clock]['bd'][0]:
                        pass
                    elif letter == input_dict[main_clock]['bd'][1]:
                        pass
                    else:
                        input_dict[main_clock]['g'] = letter
                        # print(input_dict[main_clock]['g'])

                for letter in entry:
                    if letter == input_dict[main_clock]['a']:
                        pass
                    elif letter == input_dict[main_clock]['g']:
                        pass
                    elif letter == input_dict[main_clock][1][0]:
                        pass
                    elif letter == input_dict[main_clock][1][1]:
                        pass
                    else:
                        input_dict[main_clock]['d'] = letter
                        # print(input_dict[main_clock]['d'])

                for letter_small in input_dict[main_clock]['bd']:
                    if letter_small == input_dict[main_clock]['d']:
                        pass
                    else:
                        input_dict[main_clock]['b'] = letter_small
    for sub_clock_04 in range(0, 10):
        entry = input_dict[main_clock]['input_values'][sub_clock_04]
        if len(entry) == 5:
            if input_dict[main_clock]['bd'][0] in entry and input_dict[main_clock]['bd'][1] in entry:
                input_dict[main_clock][5] = entry

                for letter in entry:
                    if letter == input_dict[main_clock]['a']:
                        pass
                    elif letter == input_dict[main_clock]['g']:
                        pass
                    elif letter == input_dict[main_clock]['b']:
                        pass
                    elif letter == input_dict[main_clock]['d']:
                        pass
                    else:
                        input_dict[main_clock]['f'] = letter
                        # print(input_dict[main_clock]['d'])

                for letter_small in input_dict[main_clock][1]:
                    if letter_small == input_dict[main_clock]['f']:
                        pass
                    else:
                        input_dict[main_clock]['c'] = letter_small
    for sub_clock_05 in range(0, 10):
        entry = input_dict[main_clock]['input_values'][sub_clock_05]
        if len(entry) == 5:
            if input_dict[main_clock]['b'] in entry:
                pass
            elif input_dict[main_clock]['f'] in entry:
                pass
            else:
                input_dict[main_clock][2] = entry
                for letter in entry:
                    if letter == input_dict[main_clock]['a']:
                        pass
                    elif letter == input_dict[main_clock]['g']:
                        pass
                    elif letter == input_dict[main_clock]['c']:
                        pass
                    elif letter == input_dict[main_clock]['d']:
                        pass
                    else:
                        input_dict[main_clock]['e'] = letter

    for sub_clock_03 in range(0, 10):
        entry = input_dict[main_clock]['input_values'][sub_clock_03]
        if len(entry) == 6:
            if input_dict[main_clock]['c'] not in entry:
                input_dict[main_clock][6] = entry

            elif input_dict[main_clock]['e'] not in entry:
                input_dict[main_clock][9] = entry

            elif input_dict[main_clock]['d'] not in entry:
                input_dict[main_clock][0] = entry
                # print('Test 2')
            else:
                print(f'Error check 6 length - Entry is {entry}')
                print(f'checked against {input_dict[main_clock]["d"]}{input_dict[main_clock]["e"]}{input_dict[main_clock]["c"]}')

    pattern_2 = re.compile(rf'[{input_dict[main_clock][2]}]{{5}}')
    pattern_3 = re.compile(rf'[{input_dict[main_clock][3]}]{{5}}')
    pattern_5 = re.compile(rf'[{input_dict[main_clock][5]}]{{5}}')
    pattern_6 = re.compile(rf'[{input_dict[main_clock][6]}]{{6}}')
    pattern_9 = re.compile(rf'[{input_dict[main_clock][9]}]{{6}}')
    pattern_0 = re.compile(rf'[{input_dict[main_clock][0]}]{{6}}')
    # print(input_dict[main_clock][3])
    # print(input_dict[main_clock]['output_values'][1])

    debug_counter = 0
    for sub_clock_03 in range(0, 4):
        entry = input_dict[main_clock]['output_values'][sub_clock_03]
        if len(entry) == 2:
            solution_counter += 1 * (10**(3-sub_clock_03))
            debug_counter += 1 * (10 ** (3 - sub_clock_03))

        elif len(entry) == 3:
            solution_counter += 7 * (10**(3-sub_clock_03))
            debug_counter += 7 * (10 ** (3 - sub_clock_03))

        elif len(entry) == 4:
            solution_counter += 4 * (10**(3-sub_clock_03))
            debug_counter += 4 * (10 ** (3 - sub_clock_03))

        elif len(entry) == 7:
            solution_counter += 8 * (10 ** (3 - sub_clock_03))
            debug_counter += 8 * (10 ** (3 - sub_clock_03))

        elif len(entry) == 5:

            if re.search(pattern_2, entry):
                solution_counter += 2 * (10 ** (3 - sub_clock_03))
                debug_counter += 2 * (10 ** (3 - sub_clock_03))

            elif re.search(pattern_3, entry):
                solution_counter += 3 * (10 ** (3 - sub_clock_03))
                debug_counter += 3 * (10 ** (3 - sub_clock_03))
                print(entry)
                print(input_dict[main_clock][3])

            elif re.search(pattern_5, entry):
                solution_counter += 5 * (10 ** (3 - sub_clock_03))
                debug_counter += 5 * (10 ** (3 - sub_clock_03))

        elif len(entry) == 6:

            if re.search(pattern_6, entry):
                solution_counter += 6 * (10 ** (3 - sub_clock_03))
                debug_counter += 6 * (10 ** (3 - sub_clock_03))

            elif re.search(pattern_9, entry):
                solution_counter += 9 * (10 ** (3 - sub_clock_03))
                debug_counter += 9 * (10 ** (3 - sub_clock_03))

            elif re.search(pattern_0, entry):
                solution_counter += 0 * (10 ** (3 - sub_clock_03))
                debug_counter += 0 * (10 ** (3 - sub_clock_03))

        else:
            print('Error Calc')

    # print(debug_counter)


print(f'The Solution is {solution_counter}')




# pattern = re.compile(r'(\w*)(b|c)(\w*)(b|c)(\w*)')
# test = 'bac'

# bool_test = bool(re.search(pattern, test))
# sub_test = pattern.sub(r'\1\3\5', test)

# print(bool_test)
# print(sub_test)