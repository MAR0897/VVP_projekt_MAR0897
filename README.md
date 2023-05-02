# Projekt do předmětu Vědecké výpočty v Pythonu
## Téma – Planety

Tento projekt simuluje gravitační síly mezi různými tělesy a vykresluje jejich trajektorie.

## Obsah knihovny

- projekt
  - main.py – hlavní funkce pro běh simulace
  - planet.py – definice třídy Planet a výpočet gravitačních sil
  - plotting.py – funkce pro vykreslování výsledků simulace
  - input_data – složka se soubory potřebnými pro inicializaci planet
    - SS8.json – celá sluneční soustava
    - SS4.json – pouze 4 Slunci nejbližsí planety
    - B3.json – 3 tělesa
- examples.ipynb – příklady funkcionalit této knihovny

## Spuštění
Ke spuštění simulace je nutné mít nainstalované knihovny NumPy a Matplotlib.
V souboru examples.ipynb se program dá spustit příkazem například:
```     
%run projekt/main.py --input_file "projekt/input_data/B3.json" --n 5000 --timestep 86400 --print_mode 2 --random 1
```
kde parametry jsou:
- input_file – cesta ke inicializačnímu souboru
- n – počet iterací
- timestamp – čas pro každou iteraci v sekundách
- print_mode – způsob vykreslení (0 pro spojitou křivku, 1 pro sluneční soustavu, 2 pro vykreslení bodů, 3 pro animaci)
- random – 0 pro přesné parametry ze souboru, 1 pro částečnou nahodilost

Výstup simulace může být vykreslen jako obrázek nebo video.
Vizualizace umožňuje zvolit způsob zobrazení trajektorií planet buď jako spojitou křivku nebo jen body v prostoru, které mají určitou barevnou mapu.
Je také možnost zvolit mód vykreslování pro sluneční soustavu (aby Slunce, které se skoro nepohybuje, bylo vůbec vidět).

Pro více příkladů o použití projektu nahlédněte do souboru examples.ipynb.
