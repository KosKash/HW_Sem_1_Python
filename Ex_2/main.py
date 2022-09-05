# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

count = 0
bool_list = [False, True]
for i in bool_list:
    x = i
    for j in bool_list:
        y = j
        for k in bool_list:
            z = k
            left = (not (x or y or z))
            right = (not x and not y and not z)
            if left == right:
                print('OK')
                count += 1
if count == 8: print("Утверждение истинно")
else: print("Утверждение ложно")

                 
