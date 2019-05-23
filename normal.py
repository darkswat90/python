# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def _calculate_damage(self, player):
        return self.damage // player.armor

    def attack(self, player):
        enemy.health -= self._calculate_damage(player)


class Player(Person):
    pass


class Enemy(Person):
    pass



class FinalFight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        attack = self.player
        while self.player.health < 0 and self.enemy.health < 0:
            if attack == self.player:
                self.enemy.attack(self.player)
                attack = self.enemy
                print(attack)
            else:
                self.player.attack(self.enemy)
                attack = self.player

        if player.health < 0:
            print('Player win!')
        else:
            print('Enemy win!')


player = Player('Varian', 100, 5, 20)
enemy = Enemy('Guldan', 100, 7, 50)
final = FinalFight(player, enemy).fight

final()