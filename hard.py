# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.



class Production:
	def __init__(self, name, color, type_toy):
		self.name = name
		self.color = color
		self.type_toy = type_toy

	def buy_mater(self):
		print('Закупка сырья')
	
	def sewing(self):
		print('Пошив')

	def paint(self):
		print('Окраска')
	
	def new_toy(self):
		self.buy_mater()
		self.sewing()
		self.paint()
			
class Toy(Production):
	pass


lion = Toy('Artur', 'Yellow', 'Animals')
print(lion)



# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка




class Production:
	def __init__(self, name, color, type_toy):
		self.name = name
		self.color = color
		self.type_toy = type_toy

	def buy_mater(self):
		print('Закупка сырья')
	
	def sewing(self):
		print('Пошив')

	def paint(self):
		print('Окраска')
	
	def new_toy(self):
		self.buy_mater()
		self.sewing()
		self.paint()

		if type_toy == 'animals':
			toy = AnimalsToy(name, color, type_toy)
		elif type_toy == 'robots':
			toy = RobotToy(name, color, type_toy)
		return toy
					
class Toy(Production):
	pass

class AnimalsToy(Toy):
	pass

class RobotToy(Toy):
	pass


toy_1 = Production('Zex', 'Black', 'robots').new_toy
toy_2 = Production('Artur', 'Yellow', 'animals').new_toy

