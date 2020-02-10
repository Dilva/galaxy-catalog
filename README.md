# API Catalogue de Messier

Une API en Python qui permet d'accéder à l'ensemble des objets du catalogue de Messier et à leurs caractéristiques.

L'API est disponible ici : 

http://dilvelinegalaxycatalog.pythonanywhere.com/



## Installation

Cloner le dépôt suivant :

git clone https://github.com/Dilva/galaxy-catalog.git


## Utilisation

Créer la base de données : 
```bash
python database_init.py
```
***La base est déjà créee, et existe dans l'application.***


Lancer l'application :
```bash
python api.py
```


## Requêtes

**Récupérer le catalogue entier :**
```python
api.py/catalog
```

ou bien cliquer sur le lien "➤ Discover the whole Messier Catalog" de l'interface.

------


**Récupérer des objets particuliers :**
```python
api.py/objects?type=Galaxy&season=Autumn
```
ou bien remplir le formulaire de l'interface.
