n = int(input('Skriv inn et tall: '))
k = int(input('Skriv inn et tall: '))

"""
sum = 0
for i in range (1,n+1):
    ledd_i = i**2 * (-1)**(i+1)

    if sum + ledd_i > k:
        print(sum)
        break
    sum += ledd_i
"""


i = 0
ledd_i = 0
sum = 0

while sum + ledd_i <= k:
    i += 1
    sum += ledd_i
    ledd_i = i**2 * (-1)**(i+1)

print('Den minste summen av tallserien under', k, 'er', sum)


