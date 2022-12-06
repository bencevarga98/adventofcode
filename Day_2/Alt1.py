scores = {"A X":4, "A Y":8, "B X":1, "A Z":3, "C X":7, "B Y":5, "B Z":9, "C Y":2, "C Z":6}
 
opened_data = open("input2.txt").readlines()
stripped_list = [s.strip() for s in opened_data]
total_score = 0

for i in stripped_list:
    total_score += scores[i]
print(total_score)
