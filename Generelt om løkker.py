sum = 0
for i in range(101):
    sum += i
print('Summen av de 100 første tallene er', sum)

produkt = 1
i = 1
while produkt < 1000:
    i += 1
    produkt *= i
print('Løkken kjørte', i, 'ganger og produktet ble', produkt)


tall1 = int(input('Skriv inn et tall: '))
tall2 = int(input('Skriv inn et nytt tall: '))

produkt = int(input('Hva er {} * {}? '. format(tall1, tall2)))
svar = tall1 * tall2

while produkt != svar:
    produkt = int(input('Hva er {} * {}? '.format(tall1, tall2)))

print('Stemmer. Svaret er', tall1*tall2)


