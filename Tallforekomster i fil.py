def number_of_lines():
    f = open('numbers.txt', 'r')
    lines = 0
    for line in f:
        lines += 1
    f.close()
    return lines

def number_frequency():


lines = number_of_lines()
print(lines)

