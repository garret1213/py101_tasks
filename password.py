"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""
password = input("Введите пароль: ")
if len(password) >= 8:
    print('Пароль сложный')
else:
    print('Пароль простой')
