import numpy as np

count = 0
number = np.random.randint(1, 1001)
print("Загадано число от 1 до 1000")
min = 0
max = 1000
while True:
    predict = round((min+max)/2)
    #predict = int(input())
    count += 1
    if number == predict:
        break
    elif number > predict:
        min = predict
        print(f"Загаданное число больше {predict}")
        print(f'Попробуем:{round((max + min) / 2)}')
    elif number < predict:
        max = predict
        print(f"Загаданное число меньше {predict}")
        print(f'Попробуем:{round((max+min)/2)}')


print(f"Ого! Вы угадали число {number} за {count} попыток.")