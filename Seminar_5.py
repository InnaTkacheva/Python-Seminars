# def myPow(x):
#     return x*x

# # c помощью lambda:
# myPow2 = lambda x: x*x

# res1 = myPow(2)
# res2 = myPow2(2)

# li = [1,2,3,4,5,7,9,0]
# print(li)
# li2 = []
# for item in li:
#     # li2.append(item*item)
#     li2.append(myPow(item))

# print(li2)

# res = list(map(myPow, li))
# print(res)

# res2 = list(map(lambda e: e*e, li))
# print(res2)


# Задача 1:
# Напишите программу, которая проверит 
# истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

# def to_bool(x):
#     if x == 0:
#         return False
#     return True    


# def Ex2():
#     # ¬(X ⋁ Y ) = ¬X ⋀ ¬Y
#     for ix in range(2):
#         for iy in range(2):
#             x = to_bool(ix)
#             y = to_bool(iy)
#             if not (not(x or y) == (not(x) and not(y))) :
#                 return False
#     return True
          

# def Ex2():
#     # ¬(X ⋁ Y ) = ¬X ⋀ ¬Y
#     to_bool = lambda e: e!=0
#     for ix in range(2):
#         for iy in range(2):
            
#             x = to_bool(ix)
#             y = to_bool(iy)
#             if not (not(x or y) == (not(x) and not(y))) :
#                 return False
#     return True


# if Ex2():
#     print("ok")
# else:
#      print("not ok")

# Задача 2:
# Помните игру с конфетами из модуля "Математика и Информатика"? 
# Создайте такую игру для игры человек против человека
# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота "интеллектом" 

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




