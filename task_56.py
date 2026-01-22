def compress_string(value: str):
    result = []
    current_char = value[0]
    count = 1

    for ch in value[1:]:
        if ch == current_char:
            count += 1
        else:
            result.append(current_char + (str(count) if count > 1 else ''))
            current_char = ch
            count = 1

    result.append(current_char + (str(count) if count > 1 else ''))

    return ''.join(result)

print(compress_string('aaabbcdd'))
print(compress_string('tttttffffqfff'))