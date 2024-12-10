# Поиск шифра
password_ = ''
print()
a = int(input('Введите целое число от 3 до 20:'))
for i in range(1, a):
    for j in range(i + 1, a+1):
        b = i + j
        if a % b == 0:
            password_ += str(i) + str(j)
print('Пароль: ', password_)