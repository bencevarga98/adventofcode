#Import, read and strip inputs
import_list = open('input.txt')
read_list = import_list.readlines()
stripped_list = [s.strip() for s in read_list]
splitted_list = [item.split(',') for item in stripped_list]

count_of_match = 0

for pair in splitted_list:
    first = pair[0].split('-')
    second = pair[1].split('-')
    print(first, second)

    overlap = False

    first_range = list(range(int(first[0]),int(first[1])+1))
    second_range = list(range(int(second[0]),int(second[1])+1))

    for num in first_range:
        if num in second_range:
            overlap = True
            
    if overlap == True:
        count_of_match += 1


print(count_of_match)