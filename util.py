""" V modulu util (tj. v souboru util.py) napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.

Hlavička funkce by tedy měla vypadat nějak takhle:

def tah(pole, pozice, symbol):
    Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    
    ...
Například:

tah('--------------------', 0, 'x') vrátí 'x-------------------'
tah('--------------------', 19, 'o') vrátí '-------------------o'
tah('x-o-x-o-x-o-x-o-x-o-', 5, 'x') vrátí 'x-o-xxo-x-o-x-o-x-o-'
Můžeš využít nějakou funkci, kterou už máš napsanou?

Zatímco funkci budeš psát, průběžně ji kontroluj automatickými testy. Pusť příkaz python -m pytest -v --level N podle toho, jak jsi daleko:

--level 10: V modulu util je nějaká funkce tah.

--level 11: Funkce dává na prázdné pole x nebo o na dané místo

--level 20: Hra na pozici, která není v poli, např. tah('--------------------', -1, 'x')

--level 22: Hra na obsazené políčko, např. tah('x-------------------', 0, 'o')

--level 24: Hra jiným symbolem než 'x' nebo 'o', např. tah('--------------------', 0, 'řeřicha')

Odevzdej celý soubor util.py.
"""

from random import randrange


def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    """
    
    if pozice not in range(0,20):
        raise ValueError(f"Zadaná pozice {pozice} je mimo herní pole 0-19")
    if pole[pozice] != '-':
        raise ValueError(f"Pozice {pozice} v poli je již obsazena")
    if symbol != 'x' and symbol != 'o':
        raise ValueError(f"Symbol {symbol} není hrací symbol x ani o")
    else:
        nove_pole = pole[:pozice] + symbol + pole[pozice+1:]
        return nove_pole