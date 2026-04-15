class Diak:
    def __init__(self, nev, osztaly, atlag):
        self.nev = nev
        self.osztaly = osztaly
        self.atlag = float(atlag)

diakok = []
fajl = open('diak.txt', 'r', encoding='utf-8')
for line in fajl:
    darabolas = line.strip().split(';')
    if len(darabolas) == 3:
        nev, osztaly, atlag_str = darabolas
        diak = Diak(nev.strip(), osztaly.strip(), atlag_str.strip())
        diakok.append(diak)
fajl.close()


print("A csoport", len(diakok), "fős.")

osszeg = sum(d.atlag for d in diakok)
atlag = osszeg / len(diakok)
print("A csoport átlaga:", atlag)

legjobb = max(diakok, key=lambda d: d.atlag)
print("A legjobb tanuló:", legjobb.nev, "átlaga:", legjobb.atlag)

evfolyamok = set()
for d in diakok:
    evfolyam = d.osztaly[0:2]
    evfolyamok.add(evfolyam)

minden = {'09', '10', '11', '12'}
hianyak = minden - evfolyamok
if not hianyak:
    print("Minden évfolyamról van tanuló.")
else:
    print("Hiányzó évfolyamok:", ', '.join(hianyak))