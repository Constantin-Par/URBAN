grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = sorted(list(students))
dict_sr_ball = {}

for i in range(0, len(list_students)):
    dict_sr_ball.update({list_students[i]: sum(grades[i]) / len(grades[i])})

print(dict_sr_ball)
