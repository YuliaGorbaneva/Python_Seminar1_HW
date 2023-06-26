# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(list_1)
# print(len(set(list_1)))
# list_2 = [list_1[0]]
# for i in list_1:
#     if i in list_2:
#         continue
#     else:
#         list_2.append(i)
# print(list_2, len(list_2))


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# n = [1, 2, 3, 4, 5]
# k = 2
# for i in range(k):
#     d = n.pop(len(n)-1)
#     n.insert(0, d)
# print(n)
# m = [2, 6, 8, 9, 6, 8, 2, 1]
# print(m)
# for i in range(len(m) - k):
#     rem = m.pop(k+i)
#     m.insert(i, rem)
# print(m)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# s = set()
# n = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# for item in n:
#     for value in item.values():
#         s.add(value)
# print(item)





# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# lst = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(lst)):
#     if lst[i] > lst[i-1]:
#         count += 1
# print(count)


#Задача про телефонные номера
inp = "+7878 +787890 +287878 +38778 +8512154"
res = dict()
for number in inp.split(" "):
    code = number[:2]
    if code not in res:
        res[code] = list()
    res[code].append(number)
print(res)
