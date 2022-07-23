x = int(input('Сколько списков будет? : '))
y = 1
w = 0	
l = []

for i in range(x):
	l.append([])

while y <= x:
	print('Введите значение которое будем добавлять в список', y, ': ')	
	value = input()
	if value == '':
		w += 1
		y += 1
		continue
	print(value, 'Добавлено в список №', y)
	l[w].append(value)
	

print(l)