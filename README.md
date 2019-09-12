pytest -vv -p no:warnings

# Fake It Before You Make It
* Object qu'on peut controler

## Mock
* Un objet de substitut dans le système, qui décide si un test unitaire passe ou échoue.

## Stub
* On stub une dépendance (fonction, API, Route, …) => Je m’intéresse à ce que cette dépendance retourne


## Fixture
* Partager des ressources entre différentes fonctions
- Loads all the images only one time
- # 4.29s -> 2.45s
