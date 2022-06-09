# Задача 34. 
# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

# Функция сплитит многочлен на отдельные элементы и формирует словарь
# def addPolyToMap(poly, result):
#     polyParts = poly.split("+") # Сплитим многочлен на отдельные элементы по +
#     for i in polyParts: # Проходим по всем элементам 
#         parts = i.strip().split('*') # Разбираем каждый элемент вида 5*х^y на ['5','x^y'] 
#         if(len(parts)>1): # Если у нас есть x 
#             if(parts[1] in result.keys()): # Если ключ 'х^у' уже есть то суммируем значения иначе добавлем этот ключ в мапу
#                 result[parts[1]]=result[parts[1]]+int(parts[0])
#             else:
#                 result[parts[1]]=int(parts[0])
#         else: # Если у нас свободный член без х
#             if(0 in result.keys()): # Так как x у нас нет, то в качестве ключа используем 0
#                 result[0]=result[0]+int(parts[0]) 
#             else:
#                 result[0]=int(parts[0])

# file_1 = open("HW_6_task_1_1.txt", "r") 
# poly_1 = file_1.read() 
# file_1.close()


# file_2 = open("HW_6_task_1_2.txt", "r") 
# poly_2 = file_2.read() 
# file_2.close()

# result = {}

# addPolyToMap(poly_1, result) # Определение функции addPolyToMap() выше ^
# addPolyToMap(poly_2, result)
  
# # Формируем итоговую строку
# res = ""
# for i in result:
#     if(res!=""):
#         res += " + "
#     res += str(result[i])
#     if(i!=0):
#         res += '*' + i

# print(res)
# result_file = open("HW_6_task_1_3.txt", "w") 
# result_file.write(res)
# result_file.close()

# Задача 39. 
# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 

# def play (sweets):
#     current_user = 1
#     while sweets !=0:
#             user = int(input(f"Игрок {current_user}: введите количество конфет 1-28: "))
#             if user > 28 or user < 1 or user > sweets:
#                 print("Введено некорректное количество конфет, введите еще раз")
#                 continue    
#             sweets = sweets - user
#             print(f"Осталось конфет: {sweets}")
            
#             if current_user == 1:
#                 current_user = 2
#             else:
#                 current_user = 1
#     print(f"Выиграл {current_user} игрок")       

# play(2022)

# Задача 42.
# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
# попробуйте строку 111111111111111111222222222222222222


# def encode (text):
#     last_char = ''
#     char_count = 0
#     result = ''
#     substr = ''

#     for i in text:
#         if last_char == '': # условие для начала работы по списку
#             last_char = i
#             char_count = 1
#         else:
#             if last_char == i:
#                 if(char_count==127): # 256 символов (- исп для повторяющихся, после исп для неповторяющихся)
#                     result+=chr(char_count) + last_char # chr - перевод int в конкретный символ
#                     char_count = 0
#                 char_count +=1
#                 if substr != '':
#                     result += chr(127+len(substr)) + substr
#                     substr = ''
#             else:
#                 if char_count > 1:
#                     result+=chr(char_count) + last_char # chr - перевод int в конкретный символ
#                     char_count = 1
#                 else:
#                     if(len(substr)==127):
#                         result += chr(127+len(substr)) + substr
#                         substr = ''
#                     substr +=last_char
#             last_char = i 
#     if char_count > 1:
#         result+=chr(char_count) + last_char
#     if substr != '':
#             substr += last_char
#             result += chr(127+len(substr)) + substr
#     return(result)

# def decode (text):
#     result = ''
#     i = 0
#     while i < len(text):
#         if(ord(text[i])-127>0): 
#             count = ord(text[i])-127 # кол-во неповторяющихся символов
#             i+=1
#             for j in range(count):
#                 result+=text[i]
#                 i+=1
#         else:
#             for j in range(ord(text[i])): # ord - перевод char(символ) в int
#                 result+=text[i+1]
#             i+=2
#     return(result)
        

# file = open("HW_6_task_42_1.txt", "r") 
# text = file.read() 
# file.close()
# encoded = encode(text)
# file = open("HW_6_task_42_2.txt", "w", encoding="utf-8") 
# file.write(encoded) 
# file.close()
# print(encoded)

# decoded = decode(encoded)
# print(decoded)

# if(len(text)==len(decoded)):
#     print('len OK')
#     err = 0
#     for i in range(len(text)):
#         if(text[i]!=decoded[i]):
#             err+=1
#     print('Err: '+ str(err))
# else:
#     print('len NOT OK')
#     print(text)
#     print(decoded)