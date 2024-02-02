pr = "Jozo ty si ale klamár"
záhada = pr.split(" ") #zmení string na zoznam, zalezi co je v tých uvodzovkach
print(záhada)
print(len(záhada))  #kolko prvkov ma zoznam

#vytvor zoznam kde je 20 náhodných čísel od 1-100

import random

zoznam = []
for i in range(20):
    zoznam.append(random.randrange(1,101))

print(zoznam)

text = ("Ahoj" , "ja", "som" , "Zojka")
konecna_veta = " ".join(text)

print(konecna_veta)

zoz = []
def generuj(n:int):
    global zoz
    for i in range(n):
        zoz.append(random.randrange(0,100))
    print (zoz)
generuj(10)

#random.choice , random.shuffle

zoz2 = []
def generuj2(n:int):
    global zoz2
    for i in range(n):
        zoz2.append(i)
    print(zoz2)
generuj2(10)

print(random.choice(zoz))

def miesacka(zoznamik):
    for i in range (0,100):
        poz1 = random.randrange(0,len(zoznamik))
        poz2 = random.randrange(0,len(zoznamik))
        temp = zoznamik[poz2]
        zoznamik[poz2] = zoznamik[poz1]
        zoznamik[poz1] = temp
        # a , b = b , a
    print(zoznamik)
miesacka(zoz2)

generuj(15)

#1- max. prvok je prvy [0]
#2_ je dalsie cislo vacsie ako moje max.?
#3- prepise

def maximum(zoznamik):
    lmax = zoznamik[0]
    poz = 0
    for i in range(0,len(zoznamik)):
        if zoznamik[i] > lmax:
            lmax = zoznamik[i]
            poz = i
    return (lmax,poz)
print(maximum(zoz))

#tuple - cez okruhle zatvorky, vrati dve hodnoty

#vymyslite funkciu ktora vrati druhy najvacsi prvok

def sucet_parne(zoz):
    sucet = 0
    for prvok in zoz:
        if prvok % 2 == 0:
            sucet += prvok
    return sucet
print(sucet_parne(zoz))

def sucet_parne_poz(zoz):
    sucet2 = 0
    for i in range(0,len(zoz)):
        if i % 2 == 0:
            sucet2 += zoz[i]
    return sucet2

print(sucet_parne_poz(zoz))

def coho_je_viac(zoz):
    parne = 0
    neparne = 0
    for i in zoz:
        if i % 2 == 0:
            parne += 1
        else:
            neparne += 1
    if parne > neparne:
        print("párnych čísel je viac")
    elif neparne > parne:
        print("nepárnych čísel je viac")
    else:
        print("počet párnych a nepárnych čísel je rovnaký")

print(coho_je_viac(zoz))

zoz3 = []
def parne_pozicie(zoz):
  for cislo in range(len(zoz)):
    if cislo % 2 == 0:
      zoz3.append(zoz[cislo])
  return zoz3
print(parne_pozicie(zoz))

zoz4 = ['kuk', 5,  'ahoj', -1, 2.5, 4, None, 7]

def nie_cisla(zoz4):
  zoz5 = []
  for i in zoz4:
    if type(i) != int and type(i) != float:
      zoz5.append(i)
  return zoz5
print(nie_cisla(zoz4))

zoz6 = ['ahoj', 12, -3, 'kukuk', 6.45, True]
def spolu_do_retazca(zoz6):
  final_string = ""
  for i in zoz6:
    final_string += str(i)
  return final_string
print(spolu_do_retazca(zoz6))

def zoznam_mocnin(n):
  zoz7 = []
  for i in range(1, n+1):
    zoz7.append(i**2)
  return zoz7

print(zoznam_mocnin(6))

z = [1,5,7,12]
def je_usp(z):
  for i in range(len(z)-1):
    if z[i] > z[i+1]:
      return False
  return True
print(je_usp(z))

z2 = [4, 1, 5, 27, 7,12]
def maxx(z2):
  max = z2[0]
  for i in range(len(z2)):
    if z2[i] > max:
      max = z2[i]
  return max
print(maxx(z2))

z3 = [4, 1, 5, 27, -7,12]
def ktory_min(z3):
  min = z3[0]
  for i in range(len(z3)):
    if z3[i] < min:
      min = z3[i]
  return z3.index(min)
print(ktory_min(z3))

zoz8 = [2,3,5,2,1,4,6,5,3,7]
def p_n(zoz8):
  zoznam1 = []
  zoznam2 = []
  for i in zoz8:
    if i % 2 == 0:
      zoznam1.append(i)
    else:
      zoznam2.append(i)
  return zoznam1, zoznam2
print(p_n(zoz8))

zoz9 = [1,2,3,4,5,6,7,8,9,10]
def zisti(zoz9, hodnota):
  for i in zoz9:
    if i == hodnota:
      return True
  return False
print(zisti(zoz9, 5))









