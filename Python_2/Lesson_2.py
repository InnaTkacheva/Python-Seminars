# Задача 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]

# var 1:
# my_list_1 = [12, 65, 58, 2, 12, 122, 41, 67]
# my_list_2 = [122, 7, 12, 3, 67]
# my_result = []
# for i in range(len(my_list_1)):
#     if not (my_list_1[i] in my_list_2):
#         my_result.append(my_list_1[i])
# print(my_result)

# var 2:
# my_list_1 = [12, 65, 58, 2, 12, 122, 41, 67]
# my_list_2 = [122, 7, 12, 3, 67]
# my_result = set(my_list_1) - set(my_list_2)
# print(list(my_result))

# var 3:
# my_list_1 = [12, 65, 58, 2, 12, 122, 41, 67]
# my_list_2 = [122, 7, 12, 3, 67]
# for number in my_list_1[:]:
#     if number in my_list_2:
#         my_list_1.remove(number)
# print(my_list_1)


# Задача 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013. 
# Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# var 1:
# data = input("Введите дату в формате дд.мм.гггг.: ")
# print(data)
# new_data = data.split(".")
# print(new_data)
# if new_data[0] == "01":
#     print("Первое", end=" ")
# elif new_data[0] == "02":
#     print("Второе", end=" ")
# elif new_data[0] == "03":
#     print("Третье", end=" ")
# else:
#     print("Такой дня в месяце нет", end=" ")
# if new_data[1] == "01":
#     print("Января", end=" ")
# elif new_data[1] == "02":
#     print("Февраля", end=" ")
# elif new_data[1] == "03":
#     print("Марта", end=" ")
# else:
#     print("Такого месяца нет", end=" ")   
# print(new_data[2], "года")

# var 2:
# data = "01.02.2020"

# d, m, y = data.split(".")

# print(d, m, y)

# months = {
#     "01": "января",
#     "02": "февраля",
#     "03": "марта"
# }

# days = {
#     "01": "первое",
#     "02": "второе",
#     "03": "третье"
# }

# result = f"{days[d]} {months[m]} {y} года"
# print(result)

# Задача 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# В этом случае ответ будет: [5, 8]


my_list = [2, 2, 5, 12, 8, 2, 12]

result = []

for i in my_list:
    if my_list.count(i) == 1:
        result.append(i)

print(result)