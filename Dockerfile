# Utilisez une image de base avec Python (qui inclut pip)
FROM python:3.8

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY . /app

# Installez les dépendances
RUN pip install -r Source/requirements.txt

# Exposez le port 80 pour les requêtes HTTP
EXPOSE 80

# Démarrez l'application Flask
CMD ["python", "Source/main_web.py"]