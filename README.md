# Projekt do předmětu Vědecké výpočty v Pythonu
## Téma – Planety

Tento projekt simuluje gravitační síly mezi různými tělesy a vykresluje jejich trajektorie.

## Obsah knihovny

- projekt
  - main.py – hlavní funkce pro běh simulace a její vykreslení, všechno ve třídě "Simulation"
  - planet.py – definice třídy "Planet", výpočet gravitačních sil a updatování pozice planet
  - input_data – složka se soubory potřebnými pro inicializaci planet
    - SS8.json – celá sluneční soustava
    - SS4.json – pouze 4 Slunci nejbližší planety
    - B3.json – 3 tělesa
- examples.ipynb – příklady funkcionalit této knihovny

## Spuštění
Ke spuštění simulace je nutné mít nainstalované knihovny NumPy a Matplotlib.
V souboru examples.ipynb se program dá spustit například:
```     
sim = Simulation(10000, 86400)
sim.read_from_file("projekt/input_data/B3.json", False)
sim.simulate(False)
sim.plot_image(1)
```
Je tedy třeba vytvořit simulaci s počtem iterací a časovým intervalem
```Simulation(počet iterací(100), časový interval(86400))```
Pak načíst vstupní data ze souboru
```read_from_file(vstupní JSON soubor, náhodné parametry?(False))```
A nyní až můžeme simulovat
```simulate(bude program kontrolovat pohyb planet?(False))```
A pak simulaci vykreslit do grafu (1 je mód vykreslení pro spojité křivky, 2 pro body)
```sim.plot_image(1 nebo 2)```
Nebo ji naanimovat
```sim.plot_video(výstupní gif soubor("animation.gif")```


## Funkcionality

Výstup simulace může být vykreslen jako obrázek nebo video.
Vizualizace umožňuje zvolit způsob zobrazení trajektorií planet buď jako spojitou křivku s markery označující aktuální pozici planet, nebo jen body v prostoru, které mají určitou barevnou mapu a jde tedy vidět i rychlost planet v určitém úseku podle gradientu barvy.

Pro více příkladů o použití projektu nahlédněte do souboru examples.ipynb.
