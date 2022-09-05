# Задача 3 (координаты четверть)
x = int(input("Input x "))
y = int(input("Input y "))
if (x > 0) and (y > 0):
    print("1 четветь")
elif (x < 0) and (y > 0):
    print("2 четветь")
elif (x < 0) and (y < 0):
    print("3 четветь")
elif (x > 0) and (y < 0):
    print("4 четветь")
