# Soča dessine

[Base](https://docs.docker.com/compose/django/#create-a-django-project)


### Referance

[Ref 1](https://mmorejon.github.io/en/blog/start-django-project-with-docker/)

### Composant:
 * Docker
 * Django
 * Postgres


### Commande:

- [ ] Pour runner ```docker-compose up```

- [ ] Pour éteindre :warning: dans un autre terminal ```docker-compose down```

- [ ] Nouvelle app ```docker-compose run web python manage.py startapp new_app_name```


- [ ] Crée super utilisateur ```docker-compose run web python manage.py createsuperuser```

- [ ] Pour passer tout les sous dossier en user local ```sudo chown -R $USER:$USER .```
