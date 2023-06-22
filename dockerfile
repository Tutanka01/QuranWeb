# Utilisez une image de base contenant Apache et Python
FROM tiangolo/uwsgi-nginx-flask:python3.7

# Copiez les fichiers de votre application dans le conteneur
COPY ./Source /app

#update pip
RUN pip install Flask-Cors
RUN pip install deep-translator
RUN pip install Jinja2

# Définissez le répertoire de travail
WORKDIR /app

# Exposez le port 80 pour la communication avec le conteneur Apache
EXPOSE 80

# Commande pour démarrer l'application
CMD ["python", "main_web.py"]
