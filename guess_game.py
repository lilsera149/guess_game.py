import random

# Компьютер загадывает число от 1 до 100
secret_number = random.randint(1, 100)
print("Я загадал число от 1 до 100. Попробуй угадать!")

# Цикл работает бесконечно, пока игрок не угадает
while True:
    user_guess = int(input("Введи свой вариант: "))
    
    if user_guess < secret_number:
        print("Моё число больше! Попробуй еще раз.")
    elif user_guess > secret_number:
        print("Моё число меньше! Попробуй еще раз.")
    else:
        print("🎉 Ура! Ты угадал число!")
        break # Выходим из цикла, игра окончена
