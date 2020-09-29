import math

def liste(x, y, z):
    return list([x, y, z])

#Oppgave B

def skalarmultiplikasjon(vektor, skalar):
    vec2 = [x*skalar for x in vektor]
    return vec2

def lengde(vektor):
    nyliste = [x**2 for x in vektor]
    lengde = math.sqrt(sum(nyliste))
    print('Lengden til vektoren er:', lengde)

    vec2 = skalarmultiplikasjon(vektor, skalar)
    nyvec2 = [x**2 for x in vec2]
    lengde2 = math.sqrt(sum(nyvec2))
    print('Lengden til den skalerte vektoren er:', lengde2)

    print('Forholdet mellom de to er:', lengde2/lengde)

def prikkprodukt(v1, v2):
    prikk = sum([i*j for (i, j) in zip(v1, v2)])
    print(prikk)




vektor = liste(1.5, 3.7, 4.5)
print('Vektor:', vektor)

#Oppgave B

skalar = int(input('Skalar: '))
vec2 = skalarmultiplikasjon(vektor, skalar)
print('Vektoren ganget med en skalar:', vec2)

lengde(vektor)

prikkprodukt([1,2,3], [1,1,1])


