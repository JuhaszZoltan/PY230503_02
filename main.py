from module import *

dolgozok:list[Dolgozo] = []
file = open('berek2020.txt', 'r', encoding='utf-8')
sorok = file.readlines()
for sor in sorok[1:]: dolgozok.append(Dolgozo(sor))

print(f'a cégnél dolgozó alkalmazottak száma: {len(dolgozok)}')

# összegzés
osszeg:int = 0
for d in dolgozok:
    osszeg += d.ber
print(f'a cégnek egy hónapban összesen {osszeg} HUF-ot kell kiutalnia')
# => átlag
atlagber:float = osszeg / len(dolgozok)
print(f'az átlagbér ennél a cégnél: {round(atlagber, 2)} HUF')

# megszámlálás
nok_szama:int = 0
for d in dolgozok:
    if d.nem == False:
        nok_szama += 1
print(f'a cégnél dolgozó nők száma: {nok_szama} fő')
# => arány
nok_aranya:float = nok_szama / len(dolgozok) * 100
print(f'a cég dolgozóinak {round(nok_aranya, 2)}%-a nő')

# szélsőérték (max, min)
maxindex:int = 0
for index in range(1, len(dolgozok)):
    if dolgozok[index].ber > dolgozok[maxindex].ber:
        maxindex = index
print(f'A legjobban {dolgozok[maxindex].nev} keres ({dolgozok[maxindex].ber} HUF)')

# eldöntés
index:int = 0
while index < len(dolgozok) and not dolgozok[index].nev.startswith('Juhász'):
    index += 1
if index < len(dolgozok): print('VAN Juhász')
else: print('NINCS Juhász')

for d in dolgozok:
    if d.nev.startswith('Balogh'):
        print('VAN Balogh')
        break
else: print('NINCS Balogh')

# keresés
keresett_nev:str = input('írj be egy nevet: ')
for d in dolgozok:
    if d.nev == keresett_nev:
        print(f'van {d.nev} nevű dolgozó')
        print(f'a(z) {d.reszleg} részlegen dolgozik')
        print(f'a jövedelme {d.ber} HUF')
        break
else: print(f'NINCS {keresett_nev} nevű dolgozó')

# kiválogatás
beszerzok:list[str] = []
for d in dolgozok:
    if d.reszleg == 'beszerzés':
        beszerzok.append(d.nev)
print('a beszerzési részlegen dolgozik:')
for b in beszerzok:
    print(f'\t- {b}')

# ------------

# minimum + kiválogatás:
# kik vannak a cégnél legrégebb?
mini:int = 0
for i in range(1, len(dolgozok)):
    if dolgozok[i].belepes < dolgozok[mini].belepes:
        mini = i
boomerek:list[str] = []
for d  in dolgozok:
    if d.belepes == dolgozok[mini].belepes:
        boomerek.append(d.nev)
print(f'a legrégevven dolgoznak a cégnél ({dolgozok[mini].belepes} óta):')
for b in boomerek:
    print(f'\t- {b}')

# megszamlala + osszegzes
# nők átlagbére:
nok_szama:int = 0
nok_bertomege:int = 0
for d in dolgozok:
    if not d.nem:
        nok_szama += 1
        nok_bertomege += d.ber
nok_atlagbere:float = nok_bertomege / nok_szama
print(f'nők átlagbére a cégnél: {round(nok_atlagbere, 2)} HUF')

# kiválogatás + max
# legjobban kereső asztalos
asztalosok:list[Dolgozo] = []
for d in dolgozok:
    if d.reszleg == 'asztalosműhely':
        asztalosok.append(d)
maxi:int = 0
for i in range(1, len(asztalosok)):
    if asztalosok[i].ber > asztalosok[maxi].ber:
        maxi = i
print(f'a legjobban keresző asztalos: {asztalosok[maxi].nev}')

