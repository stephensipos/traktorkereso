# Telepítés

## NodeJS és NPM telepítése
[NodeJS](https://nodejs.org/en/download/)

Az NPM a NodeJS csomagkezelője, a NodeJS-szel együtt települ.

## Traktorkereső frontend telepítése
1. Valamilyen CLI programból be kell lépni a frontend mappájába
2. A mappán belül a `npm install` parancsot kell kiadni


# Futtatás
## Development environment
1. Valamilyen CLI programból be kell lépni a frontend mappájába
2. A mappán belül a `npm run` parancsot kell kiadni. Ez a parancs indítani fog egy webszervert a 3000-es porton. Böngészőből ezen a porton keresztül elérhető a frontend (`http://localhost:3000`).

## Production environment
1. Valamilyen CLI programból be kell lépni a frontend mappájába
2. A mappán belül a `npm build` parancsot kell kiadni.
3. Létrejön a frontend mappájában egy `build` nevű mappa, ebbe kerülnek bele a forrásállományok statikusan, preprocessorok feldolgozása után. Ami ebben a mappában lesz build-elt anyag, az mind statikus, itt már nem fog kelleni webszerver, szimplán az `index.html`-t kell futtatni böngészőből.


# ENV fájl
Jelenleg még nincs, ha lesz, készül hozzá leírás.
