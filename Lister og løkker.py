number_list = list(range(100))
print(number_list)


sum = 0
for element in number_list:
    if (element%3)==0 or (element%10)==0:
        sum += element
print(sum)

oddetall = number_list[1::2]
print(oddetall)

partall = number_list[::2]
print(partall)

liste = []
for i in range(50):
    liste.append(oddetall[i])
    liste.append(partall[i])

print(liste)

print(number_list[::-1])