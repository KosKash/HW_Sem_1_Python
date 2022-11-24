# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

count = 0
bool_list = [False, True]
for x in bool_list:
    for y in bool_list:
        for z in bool_list:
            left = (not (x or y or z))
            right = (not x and not y and not z)
            if left == right:
                print('OK')
                count += 1
if count == 8: print("Утверждение истинно")
else: print("Утверждение ложно")

                 
