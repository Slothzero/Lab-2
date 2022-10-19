# Лабораторная работа №2 Python

var = int(input("""Чтобы нарисовать флаг Литвы, введите 1
Чтобы вывести повторяющийся рисунок, введите 2
Чтобы вывести график функции f(x)=|x|, введите 3
Чтобы вывести диаграмму по книгам, введите 4\n
"""))

match var:
    case 1:

        # Рисуем флаг с помощью RGB-палитры, табуляции и reset color символа

        print("\u001b[48;2;255;200;0m" + '\t\t\t\t' + "\u001b[0m")
        print("\u001b[48;2;0;128;50m" + '\t\t\t\t' + "\u001b[0m")
        print("\u001b[48;2;200;30;0m" + '\t\t\t\t' + "\u001b[0m")

    case 2:

        number = int(input('Сколько раз повторить рискунок?\n'))   # number - сколько раз выведется рисунок

        # Повторяющийся рисунок
        from time import sleep

        # Функция вывода с задрежкой
        def delay(line):
            print(line)
            sleep(0.25)

        # Функция, ктороая непосредственно рисует
        def symbol(number):
            for i in range(number):
                delay('\033[2;31;47m\t\t\033[0;0m\t\t\t\t\t\t\t\t\t\033[2;31;47m\t\t\033[0;0m')
                delay('\t\t\033[2;31;47m\t\t\033[0;0m\t\t\t\t\t\033[2;31;47m\t\t\033[0;0m')
                delay('\t\t\t\t\033[2;31;47m\t\033[0;0m\t\t\t\033[2;31;47m\t\033[0;0m')
                delay('\t\t\t\t\t\033[2;31;47m\t\033[0;0m\t\033[2;31;47m\t\033[0;0m')
                delay('\t\t\t\t\t\033[2;31;47m\t\033[0;0m\t\033[2;31;47m\t\033[0;0m')
                delay('\t\t\t\t\t\t\033[2;31;47m\t\033[0;0m')
                delay('\t\t\t\t\t\t\033[2;31;47m\t\033[0;0m')
                delay('\t\t\t\t\t\t\033[2;31;47m\t\033[0;0m')

        symbol(number)

    case 3:

        # Т.к. я не разобрался как перемещать кусрор с помощью escape-символов в этом задании график выводится одновреммено с координатными прямыми
        print('   ^f(x)')
        for j in range(8):
            print(f'  {9 - j}|' + '\t' * (8 - j) + '\033[2;31;41m\t\033[0;0m')
        print('  1|\033[2;37;41m____\033[0;0m________________________________> x')
        for j in range(10):
            print(f'{j}\t', end='')

    case 4:
        import csv

        # Подсчет количества книг, подходящих под условие и общего количества книг
        with open('books.csv') as f:
            f_reader = csv.DictReader(f, delimiter=';')
            count12 = 0
            countAll = 0
            for row in f_reader:
                if row['Возрастное ограничение на книгу'] == '12':
                    count12 += 1
                countAll += 1

        # Вычисление процента подходящих книг от общего количества
        percent = round(count12 / countAll, 2) * 100

        # Построение диаграммы подходящих книг
        print(f'Из всех {countAll} книг, количество книг для возраста 12 лет - {count12}')
        for i in range(95):
            if i == 0:
                # Вывод процента черным цветом на желтом фоне
                print(f"\u001b[48;2;255;200;0m\u001b[30m{percent}%\u001b[0m", end='')
            # Остальная диаграмма
            if i + 5 < percent:
                print("\u001b[48;2;255;200;0m" + ' ' + "\u001b[0m", end='')
            else:
                print("\u001b[48;2;128;128;128m" + ' ' + "\u001b[0m", end='')
            i += 1

        # Пересчет процента для книг, не подходящих под условие
        percent = round((countAll - count12) / countAll, 2) * 100

        print(f'\nКоличетсво остальных книг - {countAll - count12}')
        for i in range(95):
            if i == 0:
                # Вывод процента черным на красном фоне
                print(f"\u001b[48;2;200;30;0m\u001b[30m{percent}%\u001b[0m", end='')
            if i + 5 < percent:
                print("\u001b[48;2;200;30;0m" + ' ' + "\u001b[0m", end='')
            else:
                print("\u001b[48;2;128;128;128m" + ' ' + "\u001b[0m", end='')
            i += 1


def Decartes():
    delay('  ^ f(x)')
    for j in range(9):
        delay(f' {9-j}|')









