#Дано предложение, в котором слова разделены одним пробелом (начальных и конечных пробелов нет). 
#Получить и вывести на экран все его слова.

fraza = input('Введите предложение: ')
nom = 0
slovo = ''
while nom <= len(fraza) - 1: #Рассматриваем все символы
					#предложения (их номера в памяти
					#компьютера)
	#Формируем очередное слово
	if fraza[nom] != ' ': #Если символ – не пробел
		#Добавляем его к величине slovo
		slovo = slovo + fraza[nom]
		#Переходим к следующему символу
		nom = nom + 1
	else: #Встретился пробел – слово закончилось
		#Печатаем его
		print(slovo)
		#Готовимся формировать новое слово
		slovo = ''
		#Переходим к следующему символу – началу следующего слова
		nom = nom + 1
#В конце работы инструкции while было сформировано,
#но не напечатано последнее слово
#Печатаем его
print(slovo)

#В программе, использующей срез, рассуждения немного сложнее.
#Они приведены в комментариях:

fraza = input('Введите предложение: ')
nach = 0
while nach <= len(fraza) - 1:
#Получаем очередное слово
#Если есть ближайший пробел, начиная с позиции nach
	if fraza.find(' ', nach) != -1:
	#Определяем его позицию
		poz = fraza.find(' ', nach)
		#Определяем очередное слово
		slovo = fraza[nach:poz]
		#Печатаем его
		print(slovo)
		#'Переходим' на первый символ следующего слова
		nach = poz + 1
	else: #Больше пробелов нет - осталось последнее слово
		#Определяем его
		slovo = fraza[nach:len(fraza)]
		#и печатаем
		print(slovo)
		#Меняем значение nach так,
		#чтобы инструкция while больше не выполнялась
		nach = len(fraza) + 1
