# file = open ("C:/Users/ViolettaR/Desktop/Py83/text_task1.txt", "r")
# some_str = file.read().replace("\n", "!")
# print(some_str)

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
file = open ("Вопросы.txt", "r", encoding= "UTF-8")
questions = file.readline()
print(questions)
answer = input("Ваш ответ:")
file2 = open ("Ответы.txt","r", encoding= "UTF-8")
ans = file2.readline().rstrip()
print(ans)
count = 0
if answer == ans:
    count += 1
else:
    count +=0
print(count)

