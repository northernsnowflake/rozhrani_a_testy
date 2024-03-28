"""
V modulu ai (tj. v souboru ai.py) napiš funkci tah_pocitace(pole, symbol), která dostane řetězec s herním polem a symbol, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

Nejde-li na dané pole hrát, funkce musí skončit s chybou ValueError.

Použij jednoduchou náhodnou „strategii”:

Vyber číslo od 0 do 19.
Pokud je dané políčko volné, hrej na něj.
Pokud ne, opakuj od bodu 1.
Navíc k tomu funkce nesmí „zamrznout“ (způsobit nekonečný cyklus), ať jí předáš jakékoli hodnoty argumentů. Kdyby strategie výše měla „zamrznout“, funkce ať místo toho způsobí ValueError.

Hlavička funkce by tedy měla vypadat nějak takhle:

def tah_pocitace(pole, symbol):
    Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    
    ...
Zavolání print(tah_pocitace('o-------------------', 'x')) by mohlo vypsat třeba o---------x---------.

Testy jsou v levelech 40 až 44.

Odevzdej celý soubor ai.py.
"""
"""
# Puvodní
import util
from random import randrange

def tah_pocitace(pole, symbol):
    Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    
    #while True:
    if '-' not in pole:
        raise ValueError("Všechny pozice v poli jsou obsazené")
    i = randrange(0,20)
    while pole[i] != '-':
        i = randrange(0,20)
    return util.tah(pole,i,symbol)

"""
# se strategií
#počáteční verze - funguje když je pole plnější, ale pokud není plnější, tak hraje ze začátku náhodně. To ještě vylepším, časem.

from random import randrange
import util

def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """

    if '-' not in pole:
        raise ValueError("Všechny pozice v poli jsou obsazené")
    i = randrange(0,20)
    print(i)
    #print("-")
    while pole[i] != '-':
        if symbol == 'x' and 'xx' in pole: # pro x dvě vedle sebe (umísťuje 3.)
            i = pole.index('xx') - 1
            #print(i)
            if pole[i] != '-':
                i = i + 3
        if symbol == 'o' and 'oo' in pole: # pro o dvě vedle sebe (umísťuje 3.)
            i = pole.index('oo') - 1
            if pole[i] != '-':
                i = i + 3
        if symbol == "x" and pole[i] == "x": # pro x vedle sebe (umísťuje 2.)
            #print(i)
            i = i + 1 # vpravo od původního
            if pole[i] != '-':
                i = i - 2 # vlevo od původního
                #print(i)
        if symbol == "o" and pole[i] == "o": # pro o vedle sebe (umísťuje 2.)
            #print(i)
            i = i + 1
            if pole[i] != '-':
                i = i - 2
                #print(i)
        else:
            i = randrange(0,20)
            #print(i)
    #print(pole)
    return util.tah(pole,i,symbol)
            #i = randrange(0,20)
