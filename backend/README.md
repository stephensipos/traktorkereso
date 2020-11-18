# Traktorkeresö Backend

## Python telepítése
Innen: [Python.org](https://www.python.org/)

## Traktorkeresö backend telepítése

Valamilyen CLI programból be kell lépni a backend mappájába, és létrehozni egy izolált Python környezetet
```
~/traktorkereso/backend > python -m venv venv
```

Aktiváljuk a virtuális környezetet:

_Linux_
```
~/traktorkereso/backend > source venv/bin/activate
```

_Windows_
```
~\traktorkereso\backend > venv\Scripts\activate.bat
```

Telepítsük fel a szükséges függöségeket:
```
(venv) ~/traktorkereso/backend > python -m pip install -r requirements.txt
```

Másoljuk át a példa _.env_ file-t a _/backend_ mappába
```
(venv) ~/traktorkereso/backend > cp resources/.env.example .env
```

Inicializáljuk az adatbázist:
```
(venv) ~/traktorkereso/backend > python manage.py migrate
....
(venv) ~/traktorkereso/backend > python manage.py loaddata fixtures/tractors_base.json
....
```

Hozzunk létre egy adminisztrátor felhasználót:
```
(venv) ~/traktorkereso/backend > python manage.py createsuperuser
```

### Traktorok letöltése Használtautó.hu-ról

Opcionálisan, a traktorlistát fel lehet tölteni a [Használtautó.hu](https://hasznaltauto.hu)-n megjelenö hirdetésekkel.
```
(venv) ~/traktorkereso/backend > mkdir data
(venv) ~/traktorkereso/backend > python utils/tractorspider.py data
(venv) ~/traktorkereso/backend > python manage.py importtractors data
```


# Futtatás
Aktivált virtuális környezetben:
```
(venv) ~/traktorkereso/backend > python manage.py runserver
```

Ez a parancs indítani fog egy webszervert a 8000-es porton. Böngészőből itt érhető el az admin felület (`http://localhost:8000/admin`).

# ENV fájl
Lásd a _/resources/.env.example_ file-ban
