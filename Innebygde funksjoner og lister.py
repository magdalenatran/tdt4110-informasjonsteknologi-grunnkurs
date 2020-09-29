import random
import Counter

random_numbers = []
for i in range(100):
    random_numbers.append(random.randint(1,10))
print(random_numbers)

print('Number of 2s:', random_numbers.count(2))

print('Sum of numbers:', sum(random_numbers))

random_numbers.sort()
print(random_numbers)

#typetallet

random_numbers.reverse()
print(random_numbers)

