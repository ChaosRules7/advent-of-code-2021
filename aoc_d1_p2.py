
window_a = []
window_b = []

x = None
y = None
a_sum = 0
b_sum = 0
counter = 0

input = open('aoc_d1_p1_in.txt')

for depth in input:
    y = x
    x = int(depth)


    if y != None:

        if len(window_a) == 3:

            window_a.append(y)
            window_b.append(x)
            window_a.remove(window_a[0])
            window_b.remove(window_b[0])

            for c in window_a:
                a_sum += c
            for d in window_b:
                b_sum += d

            if b_sum > a_sum:
                counter += 1
                print(f'{b_sum} -Increase- {counter}')
            if b_sum < a_sum:
                print(f'{b_sum} -Decrease-')
            else:
                print(f'{b_sum} -Level-')

            a_sum = 0
            b_sum = 0

        else:
            window_a.append(y)
            window_b.append(x)
            print('Debug')

print(f'\n{counter} Increases were detected')

