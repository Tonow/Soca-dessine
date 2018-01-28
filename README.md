# Soča dessine

[Base](https://docs.docker.com/compose/django/#create-a-django-project)


### Référence

[Ref 1](https://mmorejon.github.io/en/blog/start-django-project-with-docker/)

[Utilisation de Django](https://docs.djangoproject.com/fr/2.0/topics/)

[Création et utilisation de packet django](https://docs.djangoproject.com/fr/2.0/intro/reusable-apps/)

[Tuto Django officiel](https://docs.djangoproject.com/fr/2.0/intro/tutorial01/)

### Composant:
 * Docker
 * Django >= 2.0
 * Postgres

----

### Commande:

- [ ] Pour runner ```docker-compose up```

- [ ] Pour éteindre :warning: dans un autre terminal ```docker-compose down```

- [ ] Nouvelle app ```docker-compose run web python manage.py startapp [new_app_name]```

----

#### Maintenance


- [ ] Crée super utilisateur ```docker-compose run web python manage.py createsuperuser```

- [ ] Pour passer tout les sous dossier en user local ```sudo chown -R $USER:$USER .```


##### Database modif

- Modifiez les modèles (dans models.py).

:arrow_down:
- Exécutez python manage.py makemigrations pour créer des migrations correspondant à ces changements.

:arrow_down:
- Exécutez python manage.py migrate pour appliquer ces modifications à la base de données.
et :pray: les commande sont la :arrow_down:


> - [ ] Effectué des changements dans les modèles  ```docker-compose run web python manage.py makemigrations [new_app_name]```

> - [ ] Création d'un table dans la batabase ```docker-compose run web python manage.py migrate```


si pb dans la Database :scream: liens de secours !!

> [lien 1](http://tech.agilitynerd.com/django-migrate-abstract-concrete-base-class.html)

> [lien 2](https://stackoverflow.com/questions/323763/foreign-key-from-one-app-into-another-in-django)

> [lien 3](https://stackoverflow.com/questions/11871221/python-typeerror-str-returned-non-string-but-still-prints-to-output)


##### Shell

> - [ ] Si besoin de rentrer dans le shell ```docker-compose run web python manage.py shell```
