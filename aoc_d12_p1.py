import re

CAPITAL_PATTERN = re.compile(r'[A-Z]+')
LOWERCASE_PATTERN = re.compile(r'[a-z]+')
input_file = open('aoc_d12_in.txt')

map_dict = {}
for line in input_file:
    clean_line = line.rstrip('\n')
    split_points = clean_line.split('-')
    # print(split_points)
    for node in split_points:
        con_node = split_points[split_points.index(node) - 1]
        if node not in map_dict.keys():
            map_dict[node] = {'visits': 0, 'connections': [con_node]}
        elif node in map_dict.keys():
            map_dict[node]['connections'].append(con_node)
        else:
            print('Error Map setup')

print(map_dict)

path_dict = {0: {'path': ['start'], 'small_cave': False}}
path_counter = 1
check = True
while check:
    path_del_list = []
    path_add_dict = {}
    for path_id in path_dict.keys():
        if path_dict[path_id]['path'][-1] == 'end':
            pass
        elif path_dict[path_id]['path'][-1] != 'end':
            for cons in map_dict[path_dict[path_id]['path'][-1]]['connections']:
                temp_list = []
                # print(cons)
                if re.search(LOWERCASE_PATTERN, cons):
                    if cons in path_dict[path_id]['path']:
                        if cons == 'start':
                            pass
                        elif path_dict[path_id]['small_cave']:
                            pass
                        else:
                            temp_list = list(path_dict[path_id]['path'])
                            temp_list.append(cons)
                            path_add_dict[path_counter] = {}
                            path_add_dict[path_counter]['path'] = temp_list
                            path_add_dict[path_counter]['small_cave'] = True
                            path_counter += 1
                    elif cons not in path_dict[path_id]['path']:
                        temp_list = list(path_dict[path_id]['path'])
                        temp_list.append(cons)
                        path_add_dict[path_counter] = {}
                        path_add_dict[path_counter]['path'] = temp_list
                        path_add_dict[path_counter]['small_cave'] = path_dict[path_id]['small_cave']
                        path_counter += 1
                        # print(f'adding {cons} after {path_dict[path_id][-1]}')
                    else:
                        print('Error Lower case process')
                elif re.search(CAPITAL_PATTERN, cons):
                    temp_list = list(path_dict[path_id]['path'])
                    temp_list.append(cons)
                    path_add_dict[path_counter] = {}
                    path_add_dict[path_counter]['path'] = temp_list
                    path_add_dict[path_counter]['small_cave'] = path_dict[path_id]['small_cave']
                    path_counter += 1
                else:
                    print('Error Case Check')
            path_del_list.append(path_id)
        else:
            print('Error path loop')

    # print(path_counter)
    # print(path_add_dict)

    # adds the new paths
    for add_id in path_add_dict.keys():
        path_dict[add_id] = path_add_dict[add_id]

    # checks if keys were marked to delete, deletes or breaks loop if no keys are marked
    if len(path_del_list) > 0:
        for del_key in path_del_list:
            del path_dict[del_key]
    elif len(path_del_list) == 0:
        check = False
    else:
        print('Error Del function')
    # print(path_dict)


solution = len(path_dict.keys())

print(f'\nThe Solution is {solution}')
# print(path_dict)
