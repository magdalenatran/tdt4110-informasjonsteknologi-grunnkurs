from turtle import *
import time

# for a in range(4):
#     forward(100)
#     left(90)
#
#
# for b in range(16,0,-3):
#     pensize(b)
#     forward(50)
#
# for c in range(250, 0, -7):
#     pensize(1)
#     forward(c)
#     left(90)

print('Jeg kan tegne en blomst av regulære polygoner')
antallKanter = int(input('Velg antall kanter: '))
omkrets = int(input('Velg omkrets på polygonet: '))
antallBlomst = int(input('Velg antall {}-kanter i blomsten: '. format(antallKanter)))

lengdeKant = omkrets/antallKanter
grader = 360

for d in range(antallBlomst):
    for e in range(antallKanter):
        forward(lengdeKant)
        left(grader/antallKanter)
    left(grader/antallBlomst)

time.sleep(10)

