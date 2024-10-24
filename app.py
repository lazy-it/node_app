"""Подвиг 2. На вход программе подаются целые числа, записанные через пробел. 
Необходимо их прочитать и с помощью list comprehension сформировать двумерный список lst размером N x N 
(квадратную таблицу чисел). Гарантируется, что из набора введенных чисел можно сформировать 
квадратную матрицу (таблицу). Полученный двумерный список отобразить командой:"""

lst = [int(x) for x in input().split()]

matrix_sqrt = len(lst) ** 0.5

if (int(matrix_sqrt)) == matrix_sqrt:
    sqrt_matrix = [lst[x:x+int(matrix_sqrt)] for x in range(0, len(lst), int(matrix_sqrt))]
    print(sqrt_matrix)
else:
    print('Невозможно составить квадратную матрицу')

