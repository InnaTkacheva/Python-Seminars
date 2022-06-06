# Задача 32:
# Дана последовательность чисел. 
# Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
# import random
# import numpy

# lst = [random.randint(1, 11) for i in range(10)]
# print(lst)

# lst = list(set(lst)) # (set() - неповторяющиеся элементы по возрастанию
# print(lst)

# lst = list(numpy.unique(lst)) # numpy.unique() - неповторяющиеся элементы по возрастанию
# print(lst)

# Задача 30:
# Вычислить число c заданной точностью d
# Пример: при d = 0.001, pi = 3.141

# d = int(input("Введите число знаков после запятой: "))
# pi = 0
# for i in range(0,1000):
#     pi = pi + (((-1)**i)/(2*i+1))*4
# # znak = 1/d    
# print(round(pi, d))

import math

# d = float(input("Введите число d: "))
# pi = 0

# for i in range(0,1000):
#     pi = pi + (((-1)**i)/(2*i+1))*4
# znak = d - int(d) 
# print(znak, int(d))

# s = int(str(d).split('.')[1])
# print(s)
# count = 0
# if s%10 !=0:
#     count += 1
# print(count)    
d = 0.001
a = math.log10(1/d)
pi = pi[:a]

print(pi)


import math
d = float(input("Введите точность: "))
a = int(math.log10(1/d))
pi = 0
for i in range(10000):
    pi += (-1)**i/((2*i) + 1)*4
pi = str(pi)
pi = pi[:a]
print(pi)



