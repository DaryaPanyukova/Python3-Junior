#Удалить из заданной строки все вхождения некоторой подстроки.

st2 = '' #Начальное значение новой строки
ykaz = 0 #Начальное значение указателя
while ykaz <= len(st) - len(podst):
	#Сравниваем срез и заданную подстроку
	if st[ykaz : ykaz + len(podst)] != podst:
	#Добавляем текущий символ st[ykaz] в новую строку
		st2 = st2 + st[ykaz]
		#Смещаем указатель на 1 позицию вправо
		ykaz = ykaz + 1
	else: #Встретилась искомая подстрока
		#Пропускаем ее
		#(cмещаем указатель на len(podst) позиций вправо)
		ykaz = ykaz + len(podst)
    st2 = st2 + st[ykaz : len(st)]