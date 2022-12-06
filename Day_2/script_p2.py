from enum import Enum

class Actions(Enum):
    rock_o = 'A'
    lose = 'X'

    paper_o = 'B'
    draw = 'Y'

    scis_o = 'C'
    win = 'Z'

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
    if round[2] == Actions.lose.value:
        #Give 0 points for losing
        score += 0

        if round[0] == Actions.rock_o.value:
            score += Scores.scis.value
        elif round[0] == Actions.paper_o.value:
            score += Scores.rock.value
        elif round[0] == Actions.scis_o.value:
            score += Scores.paper.value

    elif round[2] == Actions.draw.value:
        #Give 3 points for draw
        score += Scores.tie.value

        if round[0] == Actions.rock_o.value:
            score += Scores.rock.value
        elif round[0] == Actions.paper_o.value:
            score += Scores.paper.value
        elif round[0] == Actions.scis_o.value:
            score += Scores.scis.value
        
    elif round[2] == Actions.win.value:
        #Give 6 points for winning
        score += Scores.win.value

        if round[0] == Actions.rock_o.value:
            score += Scores.paper.value
        elif round[0] == Actions.paper_o.value:
            score += Scores.scis.value
        elif round[0] == Actions.scis_o.value:
            score += Scores.rock.value

 
    

print(score)

