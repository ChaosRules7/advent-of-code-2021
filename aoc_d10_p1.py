
input_file = open('aoc_d10_in.txt')

OPEN_SYMBOLS = {'(': 1, '[': 2, '{': 3, '<': 4}
CLOSE_SYMBOLS = {')': 1, ']': 2, '}': 3, '>': 4}

id_counter = 0
input_dict = {}

for line in input_file:
    input_dict[id_counter] = line.rstrip('\n')
    id_counter += 1

corruption_dict = {')': 0, ']': 0, '}': 0, '>': 0}
for key in input_dict.keys():
    open_list = []
    for symbol in input_dict[key]:
        if symbol in OPEN_SYMBOLS.keys():
            open_list.append(OPEN_SYMBOLS[symbol])

        elif symbol in CLOSE_SYMBOLS.keys():
            if CLOSE_SYMBOLS[symbol] == open_list[-1]:
                open_list.pop()
            elif CLOSE_SYMBOLS[symbol] != open_list[-1]:
                corruption_dict[symbol] += 1
                # print(f'For Key {key} the corrupt symbol is {symbol}')
                # print(open_list)
                break
            else:
                print('Error Close Check')

corruption_score = 0
corruption_score += corruption_dict[')'] * 3
corruption_score += corruption_dict[']'] * 57
corruption_score += corruption_dict['}'] * 1197
corruption_score += corruption_dict['>'] * 25137

# print(corruption_dict)
print(f'\nThe final Score is {corruption_score}')