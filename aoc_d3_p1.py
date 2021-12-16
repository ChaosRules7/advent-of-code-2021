'''
string = '101010'

test = list(string)

for x in test:
    print(x)

print(int(string, 2))
'''

input = open('aoc_d3_in.txt')
one_bit = []
zero_bit = []
gamma_list = []
epsilon_list = []
gamma_bin = ''
epsilon_bin = ''
input_oxygen = {}
input_co2 = {}


for horizon in input:
    bits_in = list(horizon)
    # bits_in.remove(horizon[-1])
    for position in range(0, 12):
        if int(bits_in[position]) == 1:
            if len(one_bit) < position + 1:
                one_bit.append(1)
                zero_bit.append(0)
            else:
                one_bit[position] += 1
        elif int(bits_in[position]) == 0:
            if len(zero_bit) < position + 1:
                one_bit.append(0)
                zero_bit.append(1)
            else:
                zero_bit[position] += 1
        else:
            print(f'Error: Input was {bits_in[position]}')

print(f' Zero Bits: {zero_bit}')
print(f'One bits: {one_bit}')

for decode_p in range(0, 12):
    if one_bit[decode_p] > zero_bit[decode_p]:
        gamma_list.append(1)
        epsilon_list.append(0)
    elif one_bit[decode_p] < zero_bit[decode_p]:
        gamma_list.append(0)
        epsilon_list.append(1)
    else:
        print(f'Error Decode: Input was {one_bit[decode_p]} and {zero_bit[decode_p]}')

for x in gamma_list:
    gamma_bin += str(x)

for y in epsilon_list:
    epsilon_bin += str(y)

print(f'\nBinary Gamma is {gamma_bin}')
print(f'Binary Epsilon is {epsilon_bin}')

gamma_dec = int(gamma_bin, 2)
epsilon_dec = int(epsilon_bin, 2)

print(f'Decimal Gamma is {gamma_dec}')
print(f'Decimal Epsilon is {epsilon_dec}')
print(f'\nPower Consumption is {gamma_dec * epsilon_dec}')

input_b = open('aoc_d3_in.txt')

counter = 0
for entry_raw in input_b:
    input_oxygen[str(counter)] = entry_raw.rstrip('\n')
    input_co2[str(counter)] = entry_raw.rstrip('\n')
    counter += 1
# print(input_oxygen)

for life_position in range(0, 12):
    # print(f'\nDebug Life_Position {life_position}')
    # print(f'Debug Start Len Oxygen {len(input_oxygen)}')
    # print(f'Debug Start Len CO2 {len(input_co2)}')

    oxygen_0_count = 0
    oxygen_1_count = 0
    co2_0_count = 0
    co2_1_count = 0

    for entry_oxygen_count in input_oxygen.values():
        if entry_oxygen_count[life_position] == '0':
            oxygen_0_count += 1
        elif entry_oxygen_count[life_position] == '1':
            oxygen_1_count += 1
        else:
            print(f'Error Oxygen Count: {entry_oxygen_count[life_position]}')

    for entry_co2_count in input_co2.values():
        if entry_co2_count[life_position] == '0':
            co2_0_count += 1
        elif entry_co2_count[life_position] == '1':
            co2_1_count += 1
        else:
            print(f'Error CO2 Count: {entry_co2_count[life_position]}')

    if oxygen_1_count > oxygen_0_count:
        key_oxygen = 1
    elif oxygen_1_count < oxygen_0_count:
        key_oxygen = 0
    elif oxygen_1_count == oxygen_0_count:
        key_oxygen = 1
    else:
        print('Error Oxygen Key')

    if co2_1_count < co2_0_count:
        key_co2 = 1
    elif co2_1_count > co2_0_count:
        key_co2 = 0
    elif co2_1_count == co2_0_count:
        key_co2 = 0
    else:
        print('Error CO2 Count')

    if len(input_oxygen) > 1:
        dict_keys_oxygen = list(input_oxygen.keys())
        for oxygen_position in dict_keys_oxygen:
            if int(input_oxygen[oxygen_position][life_position]) != key_oxygen:
                # print(f'Removed {input_oxygen[oxygen_position]}')
                del input_oxygen[oxygen_position]
            elif int(input_oxygen[oxygen_position][life_position]) == key_oxygen:
                pass
            else:
                print('Error Oxygen')

    if len(input_co2) > 1:
        dict_keys_co2 = list(input_co2.keys())
        for co2_position in dict_keys_co2:
            if int(input_co2[co2_position][life_position]) != key_co2:
                # print(f'Debug Removed {input_co2[co2_position]}')
                del input_co2[co2_position]
            elif int(input_co2[co2_position][life_position]) == key_co2:
                pass
            else:
                print('Error CO2')





    # print(f'Debug Len Oxygen {len(input_oxygen)}')
    # print(f'Debug Len CO2 {len(input_co2)}')

# oxygen_key_v = list(input_oxygen.keys())

# print(input_co2)

oxygen_value = int(input_oxygen[list(input_oxygen.keys())[0]], 2)
co2_value = int(input_co2[list(input_co2.keys())[0]], 2)

print(f'\nOxygen is {oxygen_value}')
print(f'CO2 is {co2_value}')

print(f'\n The Life solution is {oxygen_value * co2_value}')


