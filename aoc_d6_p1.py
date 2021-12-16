
TARGET_DAY = 256

def transform_int(x):
    return int(x)

day_0_input = open('aoc_d6_in.txt')


for fish_in in day_0_input:
    fish_raw = fish_in

fish_raw_2 = fish_raw.split(',')

fish_populus = {}
fish_counter = 0
for fish_init in fish_raw_2:
    fish_populus[fish_counter] = int(fish_init)
    fish_counter += 1

# print(fish_populus)

day_counter = 0
fish_counter_2 = len(fish_populus)
while day_counter < TARGET_DAY:
    birth_counter = 0
    for fish_single in range(0, fish_counter_2):
        # print(f'Checking fish {fish_single}')
        # print(fish_populus)
        if fish_populus[fish_single] == 0:
            fish_populus[fish_single] = 6
            birth_counter += 1

        elif fish_populus[fish_single] > 0:
            fish_populus[fish_single] -= 1

        else:
            print('Error Fish Check')

    for birth_interval in range(1, birth_counter + 1):
        fish_populus[fish_counter_2 - 1 + birth_interval] = 8

    print(f'Day {day_counter}: {len(fish_populus)} Fish')

    fish_counter_2 = len(fish_populus)
    day_counter += 1


print(f'\nAfter {TARGET_DAY} Days there are {len(fish_populus)}')



