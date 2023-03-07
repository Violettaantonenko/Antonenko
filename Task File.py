# 1.	Имеется текстовый файл.
# Получить текст, в котором в конце каждой строки из заданного файла добавлен восклицательный знак.
# file = open ("text_task1.txt", "r", encoding= "UTF-8")
# for line in file:
    


# 2.	Создать файл input.txt и записать в него 10 чисел через пробел.
# Считать из него эти числа. Затем записать их произведение в файл output.txt.
# file = open ("input.txt", "r", encoding= "UTF-8")
# some_str = file.read()
# some_str = some_str.replace("\n", " ").rstrip().split()
# some_str = list (map(int,some_str))
# print(some_str)
# pr = 1
# for numb in some_str:
#     pr *= numb
# print(pr)
# file = open("output.txt", "w", encoding="UTF-8")
# file.write(str(pr))
# file.close()

# 3.	Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара,
# цену единицы и дату поступления товара на склад.
# Вывести список товаров, хранящихся больше месяца и стоимость которых превышает 1 000 000 р.



# 4.	Написать программу “Викторина”. У вас есть 2 файла.
# В первом содержаться 10 вопросов(каждый вопрос в своей строке) во втором
# 10 ответов( каждый ответ как и вопрос в своей строке). Вам нужно считывать
# по 1 вопросу из файла с вопросами и давать на них ответ. Если ответ верный,
# добавлять к счётчику верных ответов 1 балл.
# В конце программа выводит количество верных ответов на вопросы.
# file = open ("Вопросы.txt", "r", encoding= "UTF-8")
# file2 = open ("Ответы.txt","r", encoding= "UTF-8")
# count = 0
# for line in file:
#     print (line.rstrip())
#     answer = input("Ваш ответ:").capitalize()
#     ans = file2.readline().rstrip()
#     if ans == answer:
#         count += 1
#     else:
#         count +=0
# print(count)

# 5.	Создать словарь в качестве ключа которого будет 5-ти значное число, а в качестве значений кортеж состоящий
# из 2-ух элементов – имя(str) и возраста(int).
# Сделать 5-6 элементов словаря и записать данный словарь на диск в файл json формата
# import json
# dictionary = {23545:("Denis",23),
#               34000:("Anna",40),
#               90455:("Hleb",13),
#               12889:("Mark",28),
#               53679:("Lisa",18)}
# with open ("json_file.json", "w", encoding= "UTF-8") as file:
#     json.dump (dictionary,file)

# 6.	Прочитать сохранённый json – файл и записать данные на диск в csv файл.
# Первое значение каждой строки должно начинаться со слова person, значения разделить ;
#

# 8.	Вашей задачей будет восстановление исходной строки обратно.
# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
# Для решение вам необходимо открыть файл для чтения 8.txt
numb= set('0123456789')
x = 0
chislo_povtor = ''
rasshifrovano = ''
with open("8.txt", "r", encoding= "UTF-8") as file:
    some_str = file.readline().rstrip()
simvol = some_str[x]
x += 1
while x < len(some_str):
    while some_str[x] in numb:
        chislo_povtor += some_str[x]
        x += 1
        if x >(len(some_str) - 1):
            break
    rasshifrovano += (simvol* (int(chislo_povtor)))
    chislo_povtor = ''
    if x > (len(some_str) - 1):
        break
    simvol = some_str[x]

    x += 1
with open ("rasshifrovka.txt", 'w', encoding= "UTF-8") as file2:
    file2.write(rasshifrovano)
