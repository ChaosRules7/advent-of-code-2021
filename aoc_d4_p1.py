import numpy as np


def no_space(x):
    return x != ''


input_draw = open('aoc_d4_in.txt')
input_boards = open('aoc_d4_in_b.txt')

draw_seq = []
for number in input_draw:
    draw_seq = number.split(',')

# print(draw_seq)

counter = 1
boards = {}
winner = []
debug_counter = 0
board_counter = 0

for line in input_boards:
    debug_counter += 1
    if counter == 1:
        board_lines = [list(filter(no_space, line.rstrip('\n').split(' ')))]
        counter += 1
    elif counter < 6:
        board_lines.append(list(filter(no_space, line.rstrip('\n').split(' '))))
        counter += 1
    elif counter == 6:
        counter = 1
        boards[str(board_counter)] = board_lines
        board_counter += 1
    else:
        print('Error Line read')

lucky_number = None
for bingo in draw_seq:

    if len(boards) > 0:
        for board_1 in boards.keys():
            for line_1 in range(0, 5):
                for column_1 in range(0, 5):
                    if boards[board_1][line_1][column_1] == bingo:
                        boards[board_1][line_1][column_1] = '999'
                    elif boards[board_1][line_1][column_1] != bingo:
                        pass
                    else:
                        print('Error Board Replace')

        winner_keys = []
        for board_2 in boards:
            for line_2 in range(0, 5):
                bingo_counter_1 = 0
                for column_2 in range(0, 5):
                    if boards[board_2][line_2][column_2] == '999':
                        bingo_counter_1 += 1
                    elif boards[board_2][line_2][column_2] != '999':
                        pass
                    else:
                        print('Error Bingo Count')

                if bingo_counter_1 == 5:
                    winner.append(boards[board_2])
                    winner_keys.append(board_2)
                    lucky_number = bingo
                    # print('Horizontal Winner')
                    print(f'It wins number {board_2} (H)')
                elif bingo_counter_1 < 5:
                    pass
                else:
                    print('Error Bingo Check')

            for column_3 in range(0, 5):
                bingo_counter_2 = 0
                for line_3 in range(0, 5):
                    if boards[board_2][line_3][column_3] == '999':
                        bingo_counter_2 += 1
                    elif boards[board_2][line_3][column_3] != '999':
                        pass
                    else:
                        print('Error V Bingo Count')

                if bingo_counter_2 == 5:
                    winner.append(boards[board_2])
                    winner_keys.append(board_2)
                    lucky_number = bingo
                    print(f'It wins number {board_2} (V)')
                    # print('Vertical Winner')
                elif bingo_counter_2 < 5:
                    pass
                else:
                    print('Error V Bingo Check')

        for delete_keys in winner_keys:
            try:
                del boards[delete_keys]
            except KeyError:
                print(f'Key Error with {delete_keys}')

        # print(lucky_number)
                

print(len(boards))
print(boards.keys())

print(f'\Winner is {winner[-1]}')
print(f'Lucky Number was {lucky_number}')


card_score = []
for line_4 in range(0, 5):
    for column_4 in range(0, 5):
        if winner[-1][line_4][column_4] != '999':
            card_score.append(int(winner[-1][line_4][column_4]))
        elif winner[-1][line_4][column_4] == '999':
            pass
        else:
            print('Error Score')

sum_score = 0
for score in card_score:
    sum_score += int(score)
    # print(f'\nAdd {score}')
    # print(sum_score)

print(f'\nThe Winning score is {sum_score * int(lucky_number)}')

