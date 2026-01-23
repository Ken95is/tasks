def longest_unique_substring(value: str):
    longest_str = ''
    current_str = ''

    for ch in value:
        if ch in current_str:
            current_str = current_str[current_str.find(ch) + 1:]
        current_str += ch
        
    
        if len(current_str) > len(longest_str):
            longest_str = current_str

    return f'longest unique string: {longest_str}\nlength: {str(len(longest_str))}'

print(longest_unique_substring('asdfghjk'))


# def longest_unique_substring(value: str):
#     result = []
#     current_char = value[0]


#     for ch in value[1:]:
#         if ch != current_char:
#             result.append(ch)
#             current_char = ch

    
#     result.insert(0, value[0])
#     return ''.join(result)

# print(longest_unique_substring('asdfghjkk'))
