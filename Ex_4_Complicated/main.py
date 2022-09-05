# Задача с четвертями (вывдящая сами координаты в диапазоне до 10)
num = int(input())
coor = [0,0]
if num == 1:
    for i in range(1,10):
        coor[0] = i
        for j in range(1,10):
            coor[1] = j
            print(coor, end= " | ")
if num == 2:
    for i in range(1,10):
        coor[0] = -i
        for j in range(1,10):
            coor[1] = j
            print(coor, end= " | ")
if num == 3:
    for i in range(1,10):
        coor[0] = -i
        for j in range(1,10):
            coor[1] = -j
            print(coor, end= " | ")
if num == 4:
    for i in range(1,10):
        coor[0] = i
        for j in range(1,10):
            coor[1] = -j
            print(coor, end= " | ")


