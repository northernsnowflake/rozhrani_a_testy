"""
Dnešní úkoly budou asi povědomé. Vytvoříme totiž ... hru 1D piškvorky!

Dostaneš ale tentokrát hotový testovací soubor a s jeho použitím budeš postupně zkoušet znovu vytvářenou hru.

Máš-li Piškvorky už hotové z minula, doporučuji je udělat znovu. Ty původní můžeš mít vedle a postupně z nich kopírovat kousky kódu.

Stáhni si soubor s testy, test_piskvorky.py a dej ho do adresáře kde budeš tvořit Piškvorky.

Na ulehčení testování si s aktivním virtuálním prostředím nainstaluj modul pytest-level. Ten umožňuje pouštět jen určité testy – podle toho, jak jsi daleko:

(venv)$ python -m pip install pytest-level
Zkus spustit všechny testy. Asi ti neprojdou:

(venv)$ python -m pytest -v

Pak zkus spustit testy pro úroveň 0:

```console
(venv)$ python -m pytest -v --level 0
Teď se nepustí žádné testy – všechny se přeskočí. Výpis by měl končit nějak takto:

collected N items / N deselected
=== N deselected in 0.01 seconds ===
Zadáš-li v posledním příkazu --level 1, aktivuje se první z testů. Pravděpodobně neprojde – v dalším úkolu ho spravíš!

Tvůj postup vždycky bude:

Když nějaký test neprochází, sprav ho.
Když všechno zezelená, postup na další level/úkol.
0.
V modulu piskvorky (tj. v souboru piskvorky.py) napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:

"x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
"o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
"!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
"-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)
Například:

vyhodnot('--------------------') vrátí '-'
vyhodnot('--o--xxx---o--o-----') vrátí 'x'
vyhodnot('xoxoxoxoxoxoxoxoxoxo') vrátí '!'
Zatímco budeš psát tento úkol, průběžně ho kontroluj automatickými testy. Pusť příkaz python -m pytest -v --level N podle toho, jak jsi daleko:

--level 1: V modulu piskvorky je nějaká funkce vyhodnot.
--level 2: V případě výhry dává funkce správný výsledek, 'x' nebo 'o'
--level 3: V případě remízy dává funkce správný výsledek, '!'
--level 4: Když hra neskončila, funkce dává správný výsledek, '-'
Odevzdej celý soubor piskvorky.py.
"""

import util 
import ai

def vyhodnot(pole):
    # Vyhrál hráč s křížky
    if "xxx" in pole:
        #print('vyhrál hráč s křížky')
        return "x"
    # Vyhrál hráč s kolečky
    if "ooo" in pole:
        #print('vyhrál hráč s kolečky')
        return "o"
    if "-" not in pole:
        #print('remíza')
        return "!"
    else:
        #print('hra ještě neskončila')
        return '-'

"""
V modulu piskvorky (tj. v souboru piskvorky.py) napiš funkci tah_hrace(pole, symbol), která dostane řetězec s herním polem a symbol (x nebo o) a:

dostane řetězec s herním polem,
zeptá se hráče, na kterou pozici chce hrát,
pomocí funkce tah zjistí, jak vypadá herní pole se zaznamenaným tahem hráče
vrátí toto herní pole se zaznamenaným tahem hráče.
Pokud uživatel zadá špatný vstup (nečíslo, záporné číslo, obsazené políčko apod.), funkce mu vynadá a zeptá se znova.

Hlavička funkce by tedy měla vypadat nějak takhle:

def tah_hrace(pole, symbol):
    Zeptá se hráče na tah a vrátí nové herní pole

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    
    ...
Například zavolání print(tah_hrace('o-------------------', 'x')) by mohlo dopadnout takto:

Kam chceš hrát? nevím
Zadávej čísla!
Kam chceš hrát? 0
Tam nejde hrát!
Kam chceš hrát? -1
Tam nejde hrát!
Kam chceš hrát? 151
Tam nejde hrát!
Kam chceš hrát? 2
o-x-----------------
Nezapomeň, že ve vedlejším modulu máš funkci tah, kterou si můžeš naimportovat.

Funguje-li tahle funkce s příkladem výše, otestuj ji opět pomocí automatických testů. Tentokrát nastav level na 30 až 34. (Testuje se funkce, která volá input. Jak takový test napsat je nad rámec tohoto kurzu.)

Odevzdej celý soubor piskvorky.py (i s funkcí vyhodnot).
"""

def tah_hrace(pole, symbol):
    """Zeptá se hráče na tah a vrátí nové herní pole

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while True:
        pozice = input('Kam chceš hrát? ')
        try:
            pozice = int(pozice)
        except ValueError:
            print('Zadávej čísla')
            continue
        try:
            pole_s_tahem_hrace = util.tah(pole,pozice,symbol)
            return pole_s_tahem_hrace
        except ValueError:
            print('Tam nejde hrát ')

"""
V modulu piskvorky (tj. v souboru piskvorky.py) napiš funkci piskvorky1d, která:

Vytvoří řetězec s herním polem
Stále dokola:
zavolá volá funkci tah_hrace, a výsledek uloží jako nové pole
vypíše stav hry
zavolá volá funkci tah_pocitace, a výsledek uloží jako nové pole
vypíše stav hry
Zatím nemusíš řešite konec hry (pokud ho už nemáš z minula).

V modulu hra (tj. v souboru hra.py) přidej import a volání funkce piskvorky1d.

Původní testy by měly stále procházet. Automatické testy na celou hru ale nejsou – otestuj to ručně pomocí python hra.py!

Tady odevzdej pouze modul piskvorky.py.

"""

def piskvorky1d():
    pole = '--------------------'
    while '-' in pole:
        pole = tah_hrace(pole,'o')
        print(pole)
        hodnoceni = vyhodnot(pole)
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
            break
        pole = ai.tah_pocitace(pole,'x')
        print(pole)
        hodnoceni = vyhodnot(pole)
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
            break

"""
Pošéfuj konec hry. Když někdo vyhraje nebo dojde k remíze, cyklus se ukončí a vypíše se výsledek – třeba s gratulací nebo povzbuzující zpráva.

Stav hry kontroluj po každém tahu.

Nezapomeň, že máš k dispozici funkci vyhodnot!

Automatické testy na celou hru nejsou – otestuj to ručně! Nezapomeň zkontrolovat remízu.

Odevzdej celý soubor piskvorky.py.
"""
#sss