numbers = [10, 3, 5, 8, 3, 9, 2, 8]

# new_list = set(numbers)
# print(new_list)
# num = list(new_list)
# print(num[::-1])
# print(num[-2:-1])
# print(num[-2::-1])

unique_num = []
for n in numbers:
    if n not in unique_num:
        unique_num.append(n)
print(unique_num)

swap_bool = True
while swap_bool:
    swap_bool = False
    for i in range(len(unique_num) - 1):
        if unique_num[i] > unique_num[i + 1]:
            unique_num[i], unique_num[i + 1] = unique_num[i + 1], unique_num[i]
            swap_bool = True
unique_num.reverse()
print(f'{unique_num} \n {unique_num[1]}')