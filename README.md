# API de Posts

Un projet d'API pour la gestion de posts, de commentaires et d'utilisateurs, développé avec Django REST Framework.

#   Fonctionnalités Clés

Gestion des Posts :

Création, lecture, mise à jour et suppression de posts (CRUD).

Gestion des Commentaires :

Ajout de commentaires sur un post spécifique.

Les utilisateurs ne peuvent modifier ou supprimer que leurs propres commentaires.

Gestion des Utilisateurs :

Création et lecture d'utilisateurs.

# Prérequis

Assure-toi d'avoir les logiciels suivants installés :

Python 3.8+

pip (le gestionnaire de paquets de Python)

PostgreSQL (le serveur de base de données)

# Configuration de l'Environnement Local

Suis ces étapes pour installer et lancer le projet :

1. Clone le dépôt

        git clone https://github.com/ton-nom-utilisateur/ton-nom-depot.git

        cd ton-nom-depot

2. Crée et active l'environnement virtuel

        python -m venv venv

# Sur Windows

    .\venv\Scripts\activate

# Sur macOS/Linux

    source venv/bin/activate

3. Installe les dépendances

    pip install -r requirements.txt

4. Configure la base de données

    Crée une base de données PostgreSQL pour le projet.

    À la racine du projet, crée un fichier .env et ajoute tes informations de connexion. Ce fichier ne doit jamais être committé sur Git.


# .env

    DB_NAME=le_nom_de_ta_base

    DB_USER=ton_utilisateur_bd

    DB_PASSWORD=ton_mot_de_passe

    DB_HOST=localhost

    DB_PORT=5432

5. Exécute les migrations
Ces commandes vont créer les tables de la base de données.

        python manage.py makemigrations

        python manage.py migrate

6. Lance le serveur de développement

        python manage.py runserver

Ton API sera accessible à l'adresse http://127.0.0.1:8000/