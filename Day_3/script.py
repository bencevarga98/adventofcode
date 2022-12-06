import string

#Import, read and strip inputs
import_list = open('input.txt')
read_list = import_list.readlines()
stripped_list = [s.strip() for s in read_list]

abc_values = dict(zip(list(string.ascii_lowercase+string.ascii_uppercase),range(1,53)))
shared_values_total = 0

for line in stripped_list:
    first_half = line[:int(len(line)//2)]
    second_half = line[int(len(line)//2):]
    shared_char = ''

    for char in first_half:
        if char in second_half:
            shared_char = char

    shared_values_total += abc_values[shared_char]

print(shared_values_total)