
TARGET_DAY = 256


def transform_int(x):
    return int(x)


fish_input = open('aoc_d6_in.txt')
for x in fish_input:
    fish_raw = x

fish_list = fish_raw.split(',')

fish_list = list(map(transform_int, fish_list))

fish_populus = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

for fish_single in fish_list:
    fish_populus[fish_single] += 1

day_counter = 0
new_fish_populus = {}
while day_counter < TARGET_DAY:
    birth_counter = 0
    for freq_key in fish_populus.keys():
        if freq_key > 0:
            new_fish_populus[freq_key - 1] = fish_populus[freq_key]

        elif freq_key == 0:
            birth_counter = fish_populus[freq_key]

        else:
            print('Error fish check')

    new_fish_populus[8] = birth_counter
    new_fish_populus[6] += birth_counter
    fish_populus = new_fish_populus
    day_counter += 1
    print(f'Day {day_counter}')

populus_counter = 0

for head_count in fish_populus.keys():
    populus_counter += fish_populus[head_count]

print(f'After {day_counter} Days, there are {populus_counter} Fish')
