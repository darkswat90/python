# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
	def __init__(self, maxspeed, color, name, is_police):
		self.maxspeed = maxspeed
		self.color = color
		self.name = name
		self.is_police = False

	def get_go(self):
		print('Машина поехала')

	def get_stop(self):
		print('Машина остановилась')
	
	def get_direct(self):
		dr = input ("Введите 'r', что бы повернуть на право\n Введите 'l', что бы повернууть на лево")
		if dr == str('r'):
			print('Машина повернула на право')
		elif dr == str('l'):
			print('Машина повернулана лево')

mazda_car = TownCar('160', 'red', 'mazda_3', 0)
print(mazda_car.is_police)
mazda_car.get_direct()

class SportCar:
	def __init__(self, maxspeed, color, name, is_police):
		self.maxspeed = maxspeed
		self.color = color
		self.name = name
		self.is_police = False

	def get_go(self):
		print('Машина поехала')

	def get_stop(self):
		print('Машина остановилась')
	
	def get_direct(self):
		dr = input ("Введите 'r', что бы повернуть на право\n Введите 'l', что бы повернууть на лево")
		if dr == str('r'):
			print('Машина повернула на право')
		elif dr == str('l'):
			print('Машина повернулана лево')

lambo_car = SportCar('300', 'gold', 'lambo_urus', 0)
print(lambo_car.is_police)
lambo_car.get_direct()

class WorkCar:
	def __init__(self, maxspeed, color, name, is_police):
		self.maxspeed = maxspeed
		self.color = color
		self.name = name
		self.is_police = False

	def get_go(self):
		print('Машина поехала')

	def get_stop(self):
		print('Машина остановилась')
	
	def get_direct(self):
		dr = input ("Введите 'r', что бы повернуть на право\n Введите 'l', что бы повернууть на лево")
		if dr == str('r'):
			print('Машина повернула на право')
		elif dr == str('l'):
			print('Машина повернулана лево')

man_car = WorkCar('120', 'white', 'man_TGM', 0)
print(man_car)
man_car.get_direct()

class PoliceCar:
	def __init__(self, maxspeed, color, name, is_police):
		self.maxspeed = maxspeed
		self.color = color
		self.name = name
		self.is_police = True

	def get_go(self):
		print('Машина поехала')

	def get_stop(self):
		print('Машина остановилась')
	
	def get_direct(self):
		dr = input ("Введите 'r', что бы повернуть на право\n Введите 'l', что бы повернууть на лево")
		if dr == str('r'):
			print('Машина повернула на право')
		elif dr == str('l'):
			print('Машина повернулана лево')

lada_car = WorkCar('120', 'police_color', 'Lada_10', 1)
print(lada_car)
lada_car.get_direct()


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:
	def __init__(self, maxspeed, color, name, is_police):
		self.maxspeed = maxspeed
		self.color = color
		self.name = name
		self.is_police = False

	def get_go(self):
		print('Машина поехала')

	def get_stop(self):
		print('Машина остановилась')
	
	def get_direct(self):
		dr = input ("Введите 'r', что бы повернуть на право\n Введите 'l', что бы повернууть на лево")
		if dr == str('r'):
			print('Машина повернула на право')
		elif dr == str('l'):
			print('Машина повернулана лево')


class SportCar(TownCar):
	pass

class WorkCar(TownCar):
	pass

class PoliceCar(TownCar):
	def __init__(self, maxspeed, color, name, is_police):
		super().__init__(maxspeed, color, name, is_police)
		self.is_police = True


lada_car = PoliceCar('120', 'police_color', 'Lada_10', 1)
print(lada_car.is_police)
lada_car.get_direct()
