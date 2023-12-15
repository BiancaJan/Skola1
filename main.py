# random.choice a random.shuffle
zoz = []
def generuj(n:int):
    global zoz
    for i in range(n):
        zoz.append(random.randrange(0,100))
    print(zoz)

def generuj2(n:int):
    global zoz2
    for i in range(n):
        zoz2.append(i)
    print(zoz2)

def miesacka(zoznamik):
    for i in range(0,100):
        p1 = random.randrange(0,len(zoznamik))
        p2 = random.randrange(0,len(zoznamik))
        temp = zoznamik[p2]
        zoznamik[p2] = zoznamik[p1]
        zoznamik[p1] = temp
# zoznamik[p1], zoznamik[p2] = zoznamik[p2], zoznamik[p1]
# a,b = b,a
    print(zoznamik)
def maximum(zoznamik):
    lmax = zoznamik[0]
    poz = 0
    for i in range(1, len(zoznamik)):
        if imax < zoznamik[i]:
            lmax = zoznamik[i]
            poz = i
    return (lmax, poz)

generuj(15)
#generuj2(10)
#miesacka(zoz2)
#print(random.choice(zoz2))
#maximalny prvok = prva pozicia(na zaciatku)
#prehladavat od jedneho po druhom, pytat sa ci je vacsie ako to zakladne
#prepisat
#vymysli funkciu, ktorá vráti druhý najväčší prvok du

def sucet_parne(z):
    sucet = 0
    for prvok in z:
        if prvok % 2 == 0:
            sucet += prvok
    return sucet
print(sucet_parne(z))





