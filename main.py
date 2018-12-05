txt = open("test.txt", "r")
mapkaZPliku = txt.readlines();
iloscKolumn = int(mapkaZPliku[0].split()[0]);
iloscWierszy = int(mapkaZPliku[0].split()[1]);
tablicaPol = []
tablicaTablicObiektow = []
mapaPol = []
mapaNagrod = []
gamma = 0.5
tablicaPotencjalow = []
tablicaMozliwychAkcji = []
tablicaRuchu = []
tempTablicaAkcji = []
staraTablicaPotencjalow = []
#============================================================================================#============================================================================================
#============================================================================================#============================================================================================
class Pole(object):
    wiersz = 0
    kolumna = 0
    typ = 0
    potencjal = 0
    nagroda = 0

    def __init__(self, wierszArg, kolumnaArg, typArg, potencjalArg, nagrodaArg):
        self.wiersz = wierszArg
        self.kolumna = kolumnaArg
        self.typ = typArg
        self.potencjal = potencjalArg
        self.nagroda = nagrodaArg

class Akcja(object):
    wGore = 0
    wPrawo = 0
    wDol = 0
    wLewo = 0
    zostaje = 0
    wspolczynnik = 0

    def __init__(self, wGoreArg, wPrawoArg, wDolArg, wLewoArg, zostajeArg, wspolczynnikArg):
        self.wGore = wGoreArg
        self.wPrawo = wPrawoArg
        self.wDol = wDolArg
        self.wLewo = wLewoArg
        self.zostaje = zostajeArg
        self.wspolczynnik = wspolczynnikArg

#========================================================================================================================================================================================
#========================================================================================================================================================================================


def wGoreMetoda(pole, akcja):
    if int(pole.wiersz) == 0:
        akcja.zostaje = akcja.zostaje + 0.8
    else:
        if int(tablicaTablicObiektow[pole.wiersz - 1][pole.kolumna].typ) != 0:
            akcja.wGore = akcja.wGore + 0.8
        else:
            akcja.zostaje = akcja.zostaje + 0.8
    if int(pole.kolumna) == 0 or int(tablicaTablicObiektow[pole.wiersz][pole.kolumna - 1].typ) == 0:
         akcja.zostaje = akcja.zostaje + 0.1
    else:
         akcja.wLewo = akcja.wLewo + 0.1
    if int(pole.kolumna) == iloscKolumn - 1 or int(tablicaTablicObiektow[pole.wiersz][pole.kolumna + 1].typ) == 0:
        akcja.zostaje = akcja.zostaje + 0.1
    else:
        akcja.wPrawo = akcja.wPrawo + 0.1
    return akcja
pass


def wPrawoMetoda(pole, akcja):
    if int(pole.kolumna) == iloscKolumn - 1:
        akcja.zostaje = akcja.zostaje + 0.8
    else:
        if int(tablicaTablicObiektow[pole.wiersz][pole.kolumna + 1].typ) != 0:
            akcja.wPrawo = akcja.wPrawo + 0.8
        else:
            akcja.zostaje = akcja.zostaje + 0.8
    if int(pole.wiersz) == 0 or int(tablicaTablicObiektow[pole.wiersz - 1][pole.kolumna].typ) == 0:
        akcja.zostaje = akcja.zostaje + 0.1
    else:
        akcja.wGore = akcja.wGore + 0.1
    if int(pole.wiersz) == iloscWierszy - 1 or int(tablicaTablicObiektow[pole.wiersz + 1][pole.kolumna].typ) == 0:
        akcja.zostaje = akcja.zostaje + 0.1
    else:
        akcja.wDol = akcja.wDol + 0.1
    return akcja
pass


def wDolMetoda(pole, akcja):
    if int(pole.wiersz) == iloscWierszy - 1:
        akcja.zostaje = akcja.zostaje + 0.8
    else:
        if int(tablicaTablicObiektow[pole.wiersz + 1][pole.kolumna].typ) != 0:
            akcja.wDol = akcja.wDol + 0.8
        else:
            akcja.zostaje = akcja.zostaje + 0.8
    if int(pole.kolumna) == 0 or int(tablicaTablicObiektow[pole.wiersz][pole.kolumna - 1].typ) == 0:
         akcja.zostaje = akcja.zostaje + 0.1
    else:
         akcja.wLewo = akcja.wLewo + 0.1
    if int(pole.kolumna) == iloscKolumn - 1 or int(tablicaTablicObiektow[pole.wiersz][pole.kolumna + 1].typ) == 0:
        akcja.zostaje = akcja.zostaje + 0.1
    else:
        akcja.wPrawo = akcja.wPrawo + 0.1
    return akcja
pass


def wLewoMetoda(pole, akcja):
    if int(pole.kolumna) == 0:
        akcja.zostaje = akcja.zostaje + 0.8
    else:
        if int(tablicaTablicObiektow[pole.wiersz][pole.kolumna - 1].typ) != 0:
            akcja.wLewo = akcja.wLewo + 0.8
        else:
            akcja.zostaje = akcja.zostaje + 0.8
    if int(pole.wiersz) == 0 or int(tablicaTablicObiektow[pole.wiersz - 1][pole.kolumna].typ) == 0:
        akcja.zostaje = akcja.zostaje + 0.1
    else:
        akcja.wGore = akcja.wGore + 0.1
    if int(pole.wiersz) == iloscWierszy - 1 or int(tablicaTablicObiektow[pole.wiersz + 1][pole.kolumna].typ) == 0:
        akcja.zostaje = akcja.zostaje + 0.1
    else:
        akcja.wDol = akcja.wDol + 0.1
    return akcja
pass

#============================================================================================#============================================================================================
#============================================================================================#============================================================================================

for x in range(len(mapkaZPliku)):
    if x > int(0) and x <= int(iloscWierszy) :
        mapaPol.append(mapkaZPliku[x].split())
    if x > int(iloscWierszy) + 1:
        mapaNagrod.append(mapkaZPliku[x].split())
for numerWiersza in range(iloscWierszy):
    tablicaMozliwychAkcji.append([])
    tablicaPotencjalow.append([])
    staraTablicaPotencjalow.append([])
    for numerKolumny in range(iloscKolumn):
        tablicaPotencjalow[numerWiersza].append(float(0))
        staraTablicaPotencjalow[numerWiersza].append(float(0))
        tablicaMozliwychAkcji[numerWiersza].append([])
        tablicaPol.append(Pole(numerWiersza, numerKolumny, mapaPol[numerWiersza][numerKolumny], mapaNagrod[numerWiersza][numerKolumny], mapaNagrod[numerWiersza][numerKolumny]))
        tablicaPotencjalow[numerWiersza][numerKolumny] = mapaNagrod[numerWiersza][numerKolumny]
        staraTablicaPotencjalow[numerWiersza][numerKolumny] = mapaNagrod[numerWiersza][numerKolumny]
    tablicaTablicObiektow.append(tablicaPol)
    tablicaPol = []
for numerWiersza in range(iloscWierszy):
    tablicaRuchu.append([])
    for numerKolumny in range(iloscKolumn):
        akcjaWGore = Akcja(0, 0, 0, 0, 0,0)
        akcjaWPrawo = Akcja(0, 0, 0, 0, 0, 0)
        akcjaWDol = Akcja(0, 0, 0, 0, 0, 0)
        akcjaWLewo = Akcja(0, 0, 0, 0, 0, 0)
        if int(tablicaTablicObiektow[numerWiersza][numerKolumny].typ) == 1:
            tablicaRuchu[numerWiersza].append(int(1))
            tablicaMozliwychAkcji[numerWiersza][numerKolumny].append(wGoreMetoda(tablicaTablicObiektow[numerWiersza][numerKolumny], akcjaWGore))
            tablicaMozliwychAkcji[numerWiersza][numerKolumny].append(wPrawoMetoda(tablicaTablicObiektow[numerWiersza][numerKolumny], akcjaWPrawo))
            tablicaMozliwychAkcji[numerWiersza][numerKolumny].append(wDolMetoda(tablicaTablicObiektow[numerWiersza][numerKolumny], akcjaWDol))
            tablicaMozliwychAkcji[numerWiersza][numerKolumny].append(wLewoMetoda(tablicaTablicObiektow[numerWiersza][numerKolumny], akcjaWLewo))
        else:
            tablicaRuchu[numerWiersza].append(int(0))
for x in range(1000):
    for numerWiersza in range(iloscWierszy):
        for numerKolumny in range(iloscKolumn):
            if float(tablicaTablicObiektow[numerWiersza][numerKolumny].typ) == float(1):
                najlepszaAkcja = float(0)
                for numerAkcji in range(len(tablicaMozliwychAkcji[numerWiersza][numerKolumny])):
                    tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wspolczynnik = float(0)
                    if float(tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wGore) != float(0):
                        tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wspolczynnik += float(
                            tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wGore) * float(
                            tablicaPotencjalow[numerWiersza - 1][numerKolumny])
                    if float(tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wPrawo) != float(0):
                        tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wspolczynnik += float(
                            tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wPrawo) * float(
                            tablicaPotencjalow[numerWiersza][numerKolumny + 1])
                    if float(tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wDol) != float(0):
                        tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wspolczynnik += float(
                            tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wDol) * float(
                            tablicaPotencjalow[numerWiersza + 1][numerKolumny])
                    if float(tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wLewo) != float(0):
                        tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wspolczynnik += float(
                            tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wLewo) * float(
                            tablicaPotencjalow[numerWiersza][numerKolumny - 1])
                    if float(tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].zostaje) != float(0):
                        tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wspolczynnik += float(
                            tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].zostaje) * float(
                            tablicaPotencjalow[numerWiersza][numerKolumny])
                    tempTablicaAkcji.append(float(tablicaMozliwychAkcji[numerWiersza][numerKolumny][numerAkcji].wspolczynnik))
                najlepszaAkcja = float(max(tempTablicaAkcji))
                for y in range(len(tempTablicaAkcji)):
                    if tempTablicaAkcji[y] == najlepszaAkcja:
                        numerAkcji = y + 1
                        break
                tablicaRuchu[numerWiersza][numerKolumny] = numerAkcji;
                staraTablicaPotencjalow[numerWiersza][numerKolumny] = tablicaPotencjalow[numerWiersza][numerKolumny]
                tablicaPotencjalow[numerWiersza][numerKolumny] = float(
                mapaNagrod[numerWiersza][numerKolumny]) + float(gamma) * float(najlepszaAkcja)
                tempTablicaAkcji = []
    zmiany = int(0)
    for numerWiersza in range(iloscWierszy):
        for numerKolumny in range(iloscKolumn):
            if float(tablicaPotencjalow[numerWiersza][numerKolumny]) - float(staraTablicaPotencjalow[numerWiersza][numerKolumny]) > float(0.0001):
                zmiany += int(1)
    if zmiany == 0:
        print(x)
        break

print('====== TABLICA RUCHU==========')
print(tablicaRuchu[0])
print(tablicaRuchu[1])
print(tablicaRuchu[2])
print('====== TABLICA POTENCJAŁÓW==========')
print(tablicaPotencjalow[0])
print(tablicaPotencjalow[1])
print(tablicaPotencjalow[2])
