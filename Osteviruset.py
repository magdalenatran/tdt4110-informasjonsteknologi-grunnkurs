cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

print(cheeses['port salut'])

infected_shelves = ['A234', 'A235', 'B13', 'B15', 'C31']

infected_cheeses = []
for key, value in cheeses.items():
    for shelf in value:
        for infected_shelf in infected_shelves:
            if infected_shelf in shelf:
                infected_cheeses.append(key)
infected_cheeses = list(set(infected_cheeses))
print('Potentially infected cheeses:', infected_cheeses)

for cheese in infected_cheeses:
    if cheese in cheeses:
        del cheeses[cheese]

for key, value in cheeses.items():
    for shelf in value:
        print(shelf, key)




