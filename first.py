x = int(input('Сколько списков будет? : '))
y = 1
w = 0	
list = []
sort_list = []

for i in range(x):
	list.append([])

while y <= x:
	print('Введите значение которое будем добавлять в список №', y, 'либо Нажмите Enter, если список полон:\n')	
	value = input()
	if value == '':
		print('Формирование списка', y, 'закончено\n')
		w += 1
		y += 1
		if y <= x:
			print('Формируем спиок', y, '\n')
		continue
	list[w].append(int(value))

def uniq_list(x, y):
	for i in x:
		for n in i:
			if n not in y:
				y.append(n)
	y.sort()
	return(y)

print(uniq_list(list, sort_list))