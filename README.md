# Projekt do předmětu Vědecké výpočty v Pythonu
## Téma – Planety

Tento projekt simuluje gravitační síly mezi různými tělesy a vykresluje jejich trajektorie.

## Obsah knihovny

- projekt
  - main.py – hlavní funkce pro běh simulace
  - planet.py – definice třídy Planet, výpočet gravitačních sil a updatování pozice planet
  - plotting.py – funkce pro vykreslování výsledků simulace
  - input_data – složka se soubory potřebnými pro inicializaci planet
    - SS8.json – celá sluneční soustava
    - SS4.json – pouze 4 Slunci nejbližší planety
    - B3.json – 3 tělesa
- examples.ipynb – příklady funkcionalit této knihovny

## Spuštění
Ke spuštění simulace je nutné mít nainstalované knihovny NumPy a Matplotlib.
V souboru examples.ipynb se program dá spustit příkazem například:
```     
%run projekt/main.py --input_file "projekt/input_data/B3.json" --n 5000 --timestep 86400 --print_mode 2 --random 1 --container 1
```
kde parametry jsou:
- input_file – cesta ke inicializačnímu souboru
- n – počet iterací
- timestep – čas pro každou iteraci v sekundách
- print_mode – způsob vykreslení (1 pro spojitou křivku, 2 pro vykreslení bodů, 3 pro animaci)
- random – 0 pro přesné parametry ze souboru, 1 pro částečnou nahodilost
- container – 0 pro neomezenou simulaci, 1 pro kontrolu simulace, jestli planety na sebe ještě vůbec nějak působí a nerozlétly se pryč

Výstup simulace může být vykreslen jako obrázek nebo video.
Vizualizace umožňuje zvolit způsob zobrazení trajektorií planet buď jako spojitou křivku s markery označující aktuální pozici planet, nebo jen body v prostoru, které mají určitou barevnou mapu a jde tedy vidět i rychlost planet v určitém úseku podle gradientu barvy.


Pro více příkladů o použití projektu nahlédněte do souboru examples.ipynb.
