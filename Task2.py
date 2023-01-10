# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = bool(input('Введите x: '))
# y = bool(input('Введите y: '))
# z = bool(input('Введите z: '))

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not (x or y or z) == (not(x) and not(y) and not(z)):
                print(f'For x = {x}, y = {y}, z = {z}: TRUE')
            else:
                print(f'For x = {x}, y = {y}, z = {z}: FALSE')