#Import, read and strip inputs
import_list = open('input.txt')
read_list = import_list.readlines()
stripped_list = [s.strip() for s in read_list]
splitted_list = [item.split(',') for item in stripped_list]

count_of_match = 0

for pair in splitted_list:
    first = pair[0].split('-')
    second = pair[1].split('-')
    
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        count_of_match += 1
    elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        count_of_match += 1

print(count_of_match)