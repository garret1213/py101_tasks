"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
from random import randint
random_number = randint(1, 1_000_000)
user_number = (input('Здравствуйте! \n Попробуйте угадать загаданное компьютером число, находящееся в промежутке от 1 до 1000000 \n Введите число:'))
if (user_number) == random_number:
    print("Поздравляю! Вы угадали!")
if user_number.isdigit():
    if (0 >= int(user_number) <= 1_000_001):
        print("К сожалению это число не входит в промежуток.\nПожалуйста выберете число находящееся в промежутке от 1 до 1000000")
    elif int(user_number) > random_number:
        print('Число '+ str(user_number) + ',больше загаданного компьютером')
    elif random_number > int(user_number):
        print('Число '+ str(user_number) + ',меньше загаданного компьютером')
elif user_number == "exit":
    quit()
elif user_number.isdigit() == False: 
    print('Вы ввели не число')
