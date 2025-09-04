from random import randint
welcome_text = 'Угадай'

rand = randint(1, 101)
print('Угадайте число от 1 до 100')


def main():
    while True:
        user_number = int(input('Введите число: '))
        if (user_number < rand):
            print('Ваше число меньше того, что загадано')

        elif (user_number > rand):
            print('Ваше число больше того, что загадано')
        elif (user_number == rand):
            print('Отличная интуиция! Вы угадали число:)')
            break


main()
