import itertools

import_list = open('input.txt')
read_list = import_list.readlines()
stripped_list = [s.strip() for s in read_list]

delimiter = ''
split_list = [list(y) for x, y in itertools.groupby(stripped_list, lambda z: z == delimiter) if not x]

elves_list = []

for i in split_list:
    elf_calorie = 0
    for j in i:
        elf_calorie += int(j)
    elves_list.append(elf_calorie)

max_index = elves_list.index(max(elves_list))
max_cal = max(elves_list)

print(max_index+1, max_cal)

sorted_elves = sorted(elves_list, reverse=True)
sum_of_top_3 = 0

for i in range(3):
    sum_of_top_3 += sorted_elves[i]

print(sum_of_top_3)