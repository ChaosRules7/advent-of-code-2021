

input_file = open('aoc_d8_in.txt')

input_clean = []
for x in input_file:
    input_raw = x
    input_sep = input_raw.split('|')
    input_fine = input_sep[1].split(' ')
    for y in range(1, 5):
        input_clean.append(input_fine[y].rstrip('\n'))

solution_counter = 0
for output in input_clean:
    if len(output) == 2:
        solution_counter += 1
    elif len(output) == 3:
        solution_counter += 1
    elif len(output) == 4:
        solution_counter += 1
    elif len(output) == 7:
        solution_counter += 1
    else:
        pass

print(f'The solution is {solution_counter}')