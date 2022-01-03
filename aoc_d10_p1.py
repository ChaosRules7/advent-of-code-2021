
input_file = open('aoc_d10_in.txt')

OPEN_SYMBOLS = {'(': 1, '[': 2, '{': 3, '<': 4}
CLOSE_SYMBOLS = {')': 1, ']': 2, '}': 3, '>': 4}


id_counter = 0
input_dict = {}

for line in input_file:
    input_dict[id_counter] = line.rstrip('\n')
    id_counter += 1

corruption_dict = {')': 0, ']': 0, '}': 0, '>': 0}
corruption_list = []
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
                corruption_list.append(key)
                break
            else:
                print('Error Close Check')

corruption_score = 0
corruption_score += corruption_dict[')'] * 3
corruption_score += corruption_dict[']'] * 57
corruption_score += corruption_dict['}'] * 1197
corruption_score += corruption_dict['>'] * 25137

# print(corruption_dict)
# print(f'\nThe final Score is {corruption_score}')

for corruption_key in corruption_list:
    del input_dict[corruption_key]


completion_list = []
for key in input_dict.keys():
    open_list = []
    for symbol in input_dict[key]:
        if symbol in OPEN_SYMBOLS.keys():
            open_list.append(OPEN_SYMBOLS[symbol])

        elif symbol in CLOSE_SYMBOLS.keys():
            if CLOSE_SYMBOLS[symbol] == open_list[-1]:
                open_list.pop()

            else:
                print('Error Close Check')

    completion_score = 0
    for order in range(-1, -1 - len(open_list), -1):
        completion_score *= 5
        completion_score += open_list[order]

    completion_list.append(completion_score)

completion_list.sort()

while len(completion_list) > 1:
    completion_list.pop()
    completion_list.pop(0)

print(completion_list[0])

