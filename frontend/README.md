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
2. A mappán belül a `npm start` parancsot kell kiadni. Ez a parancs indítani fog egy webszervert a 3000-es porton. Böngészőből ezen a porton keresztül elérhető a frontend (`http://localhost:3000`).

## Production environment
1. Valamilyen CLI programból be kell lépni a frontend mappájába
2. A mappán belül a `npm run build` parancsot kell kiadni.
3. Létrejön a frontend mappájában egy `build` nevű mappa, ebbe kerülnek bele a forrásállományok statikusan, preprocessorok feldolgozása után. Ami ebben a mappában lesz build-elt anyag, az mind statikus, itt már nem fog kelleni webszerver, szimplán az `index.html`-t kell futtatni böngészőből.


# ENV fájl
Az example env fájl (`env.example`) alapján készíteni kell egy saját env fájlt `.env` néven a frontend gyökerében.

## Változók:
- `BROWSER`: nyíljon-e meg a böngésző a frontend indításakor vagy sem (dev env)
- `PORT`: milyen porton fusson a frontend (dev env)
- `REACT_APP_API_BASE_URL`: Mi a backend api base url-je (beleértve a `/api` előtagot is)
