import random

class Card:
    def __init__(self, name):
        bag = [x for x in range(1, 91)]
        self.card = [Card.gen_string(bag), Card.gen_string(bag), Card.gen_string(bag)] #Генерирует 3 списка каждый список строка карточки
        self.name = name
        self.count_barrel = 15


    def gen_string(bag):  #Метод генерации карточек на основе мешка удаляя полученное число из "мешка", что бы числа не повторялись в карточке
        string = ['' for _ in range(9)]           #Создается пустой список с элементами ['', '', '', '', '', '', '', '']
        for x in range(0, 5):                      #Цилк запускающий в диапозоне от 0, 1, 2, 3, 4
            digit = random.randint(0, 8)            #Случайны выбор позиции заменяемого элемента
            while string[digit] != '':
                digit = random.randint(0, 8)
            string[digit] = bag.pop(random.randint(0, len(bag) - 1)) #Добавляет случайны номер боченка в карточку в позицию digit, после удаляя его из "мешка"
        return string
    #Тут я пытался сделать соритировку по возрастанию, но тут изначально в список с str добавляются int и sort(), и shuffle не подходят так как работают только с int и float
    #Видел как делают через 'None', но так до конца и не понял как это реализовано, там уже работает sort().
    def __str__(self):                                                      #Перегрузка оператора str, формирвание и визуализация карточки
        result = '{:-^20}\n'.format(self.name)
        for x in range(3):
            result += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(*self.card[x]) + '\n'
        return result + '--------------------------'

player = Card(' Карточка игрока ') #Создания экземпляра для игрока
computer = Card(' Карточка компьютера ') #Создание экземпляра дял компьютера

bag = [x for x in range(1, 91)] #Собственно игровой мешок
while True:
    if len(bag) < 1: #Проверка, не закончились ли в мешке бочонки
        print('Бочёнки в мешке закончились. Результат:\n у компьютера осталось {} числа/чисел,\n у игрока осталось {} числа/чисел.'.format(computer.count_barrel, player.count_barrel))
        break
    barrel = bag.pop(random.randint(0, len(bag) - 1)) #Удаляет боченок из мешка который вытащили
    print('\nНовый бочонок: {} (осталось {})'.format(barrel, len(bag))) #Выводит инфу какой боченок и сколько осталось (капитан очевидность)
    print(computer) #Выводит карточку компьютера
    print(player)   #Выводит карточку игрока
    reply = input('У вас есть такой бочонок? (y/n/q)') #Запрашивает действия от игрока
    reply = reply.lower() #Все ответы преобразует в нижни регистр
    while len(reply) == 0 or reply not in 'ynq': #В случае некорректного ввода повторяет информацию
        print('\n\n!!! Не корректтный ввод!\n')
        print('Новый бочонок: {} (осталось {})'.format(barrel, len(bag)))
        print(computer)
        print(player)
        reply = input('Зачеркнуть цифру? (y/n/q)')
        reply = reply.lower()

    if reply == 'q': #Выходит из игры если игрок ввел 'q'
        print('Вы вышли из игры. Вы так и не выиграли.')
        break
    elif reply == 'y': #При вводде 'y'
        check = False
        for x in range(3): #Цикл проверки если такое номер бочонка в карточке
            if barrel in player.card[x]:
                check = True
                player.card[x][player.card[x].index(barrel)] = '-'
                player.count_barrel -= 1
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if check: #Проверка у кого сколько не закрытых ячеек
            if player.count_barrel < 1:
                print('Вы Выиграли!')
                break
            elif computer.count_barrel < 1:
                print('Компьютер Выиграл!')
                break
        else: #Если такого числа не при вводе 'y' тогда проигрыш
            print('Вы проиграли! Такого числа нет на Вашей карточке!')
            break
    elif reply == 'n':
        check = False
        for x in range(3): #Проверка наличия числа в карточне, при вводе 'n'
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