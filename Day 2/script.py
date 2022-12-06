from enum import Enum

class Actions(Enum):
    rock_o = 'A'
    rock_p = 'X'

    paper_o = 'B'
    paper_p = 'Y'

    scis_o = 'C'
    scis_p = 'Z'

class Scores(Enum):
    rock = 1
    paper = 2
    scis = 3
    win = 6
    tie = 3


import_list = open('input2.txt')
read_list = import_list.readlines()
stripped_list = [s.strip() for s in read_list]

score = 0

for round in stripped_list:
    print(round)
    if round[2] == Actions.rock_p.value:
        score += Scores.rock.value
        if round[0] == Actions.rock_o.value:
            score += Scores.tie.value
            print('Tie')
        elif round[0] == Actions.paper_o.value:
            print('Round lost')
        elif round[0] == Actions.scis_o.value:
            score += Scores.win.value
            print('Win')
        print(score)

    elif round[2] == Actions.paper_p.value:
        score += Scores.paper.value
        if round[0] == Actions.rock_o.value:
            score += Scores.win.value
            print('Win')
        elif round[0] == Actions.paper_o.value:
            score += Scores.tie.value
            print('Tie')
        elif round[0] == Actions.scis_o.value:
            print('Round lost')
        print(score)
        
    elif round[2] == Actions.scis_p.value:
        score += Scores.scis.value
        if round[0] == Actions.rock_o.value:
            print('Round lost')
        elif round[0] == Actions.paper_o.value:
            score += Scores.win.value
            print('Win')
        elif round[0] == Actions.scis_o.value:
            score += Scores.tie.value
            print('Tie')
        print(score)

print(score)

