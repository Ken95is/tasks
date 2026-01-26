numbers = [2, 1, 5, 1, 3, 2, 6, 2]
k = 3

num_sum = sum(numbers[:k])
max_sum = []
max_index = []

# print(num_sum)
print(len(numbers))
for i in range(len(numbers)-2):
    num_sum = sum(numbers[i:k+i])
    max_sum.append(num_sum) 
        # print(num_sum)

for i in numbers:
    max_index = numbers[4:7]

print(max_sum)
print(max_index)
print(max(max_sum))

# big O notation
# временная сложность
