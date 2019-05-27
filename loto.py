
from random import randint

class Card:
    def __init__(self, name):
        self.card = __class__.generate_random_card()
        self.name = name
        self.count_barrel = 15

    @staticmethod
    def generate_random_card():
        card = [[] for _ in range(3)]
        barrels = set()
        while len(barrels) < 15:
            barrels.add(randint(1, 91))

        barrels = list(barrels)
        for index_row in range(0, 3):
            row_indexes_should_be_fill = set()
            while len(row_indexes_should_be_fill) < 5:
                row_indexes_should_be_fill.add(randint(0, 8))

            barrels_for_row = barrels[:5]
            barrels_for_row.sort(reverse=True)
            barrels = barrels[5:]

            row = [''] * 9
            for x in row_indexes_should_be_fill:
                row[x] = barrels_for_row.pop()

            card[index_row] = row
        return card

    def __str__(self):
        rez = '{:-^26}\n'.format(self.name)
        for x in range(3):
            rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
        return rez + '--------------------------'

computer = Card(' Карточка компьютера ')
player = Card(' Карточка игрока ')
bag = [x for x in range(1, 91)]
while True:
    if len(bag) < 1:
        print('Бочёнки в мешке закончились. Результат:\n'
              'у компьютера осталось {} числа/чисел,\n'
              'у игрока осталось {} числа/чисел.'
              .format(computer.count_barrel, player.count_barrel))
        break
    barrel = bag.pop(randint(0, len(bag) - 1))
    print('\nНовый бочонок: {} (осталось {})'.format(barrel, len(bag)))
    print(computer)
    print(player)
    reply = input('Зачеркнуть цифру? (y/n/q)')
    reply = reply.lower()
    while len(reply) == 0 or reply not in 'ynq':
        print('\n\n!!! Ответ не распознан!\n')
        print('Новый бочонок: {} (осталось {})'.format(barrel, len(bag)))
        print(computer)
        print(player)
        reply = input('Зачеркнуть цифру? (y/n/q)')
        reply = reply.lower()

    if reply == 'q':
        print('Вы вышли из игры. Вы так и не выиграли.')
        break
    elif reply == 'y':
        check = False
        for x in range(3):
            if barrel in player.card[x]:
                check = True
                player.card[x][player.card[x].index(barrel)] = '-'
                player.count_barrel -= 1
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if check:
            if player.count_barrel < 1:
                print('Вы Выиграли!')
                break
            elif computer.count_barrel < 1:
                print('Компьютер Выиграл!')
                break
        else:
            print('Вы проиграли! Такого числа нет на Вашей карточке!')
            break
    elif reply == 'n':
        check = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3):
            if barrel in player.card[x]:
                print('Вы проиграли! Такое число есть на Вашей карточке!')
                check = True
                break
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if check:
            break
        if player.count_barrel < 1:
            print('Вы Выиграли!')
            break
        elif computer.count_barrel < 1:
            print('Компьютер Выиграл!')
            break
