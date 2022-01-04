from src.picker import QuestionSelector

d1 = {}
d2 = {'6.1':5}
d3 = {6:5}
d4 = {1:10, 2:15}
d5 = {1:10, 2:0}
d6 = {1:0, 2:0}
d7 = {'5':25, '2':30,'5.1': 21}

picker = QuestionSelector(d7)
print(picker)