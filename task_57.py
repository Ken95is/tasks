matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# print(range(len(matrix)))
n = len(matrix)
m = len(matrix[0])

if n == m:
    print('matrix is square')
else:
    print('error')

count = 0
for i in range(len(matrix)): # len = 3, range = (0, 3)
    print(matrix[i][i]) # matrix[i][i] = matrix[0][0] и далее увеличивается [1][1], [2][2]
    count += matrix[i][i] # count = matrix[i][i] который = 1 потом + 5 + 9 
print(count)
main_diagonal_sum = (count, )
print(main_diagonal_sum)

# я оставил принты для себя так как мне легче ориентироваться и видеть что к чему

count = 0
for i in range(len(matrix)):
    print(matrix[i][len(matrix)-1 - i]) # здесь во втором индексе используем длину матрицы -1 и -i который в первой итерации равен 0 что приводит к 2 во втором индексе, потом 3-1-1=1, и в конце 3-1-2=0
    count += matrix[i][len(matrix)-1 - i]
print(count)

secondary_diagonal_sum = (count, )
print(secondary_diagonal_sum)


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9,10,11,12],
#     [13,14,15,16],
# ]

# print(n)
# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[2][2])
# print(matrix[0][2])
# print(matrix[1][1])
# print(matrix[2][0])