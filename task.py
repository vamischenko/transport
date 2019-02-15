March = []
help_array = []

def inMarch():
	print("Введите номер машрута")
	num = input()
	print("Название начального пункта маршрута")
	first = input()
	print("Название конечного пункта маршрута")
	end = input()
	print("Количество транспорта на маршруте (легкой и грузовой через пробел)")
	tran = input().split(' ')
	help_array.append(num)
	help_array.append(first)
	help_array.append(end)
	help_array.append(tran)
	March.append(help_array)

def inMarch_eight_el():
	i=0
	while (i<8):
		inMarch()
		i += 1

def outTable():
	for row in March:
		print(row)

def infoMar(number):
	for row in March:
		if (row[0] == a):
			print(row)
		else:
			print('Нет информации!') 

def infoGruz():
	kol = 0
	for row in March:
		if(row[3][1]>0):
			kol += 1
		else:
			print("No")
	print("Количество маршрутов, использующих грузовой транспорт " + kol)

def addIn():
	inMarch()