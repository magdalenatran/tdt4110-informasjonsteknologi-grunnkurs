import pprint
def separate(numbers, threshold):
    a = []
    b = []
    for element in numbers:
        if element < threshold:
            a.append(element)
        else:
            b.append(element)
    return a, b


numbers = [1, 2, 3, 4, 5]
threshold = 2
liste = separate(numbers, threshold)
print(liste)


def multiplication_table(n):
    table = []
    for i in range(1,n+1):
        table.append([])
        for j in range(1,n+1):
            table[i-1].append(i*j)
    return table

gangetabell = multiplication_table(5)
pprint.pprint(gangetabell)
