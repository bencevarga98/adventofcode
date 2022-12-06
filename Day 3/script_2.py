import string

#Import, read and strip inputs
import_list = open('input.txt')
read_list = import_list.readlines()
stripped_list = [s.strip() for s in read_list]

abc_values = dict(zip(list(string.ascii_lowercase+string.ascii_uppercase),range(1,53)))
shared_values_total = 0

for line in range(0,len(stripped_list),3):
    shared_char = ''
    for char in stripped_list[line]:
        if char in stripped_list[line+1] and char in stripped_list[line+2]:
            shared_char = char

    shared_values_total += abc_values[shared_char]

print(shared_values_total)
    