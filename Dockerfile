
# Holt sich ein bestehendes Image aus einem Container => Holt sich Dockerimage von Python
FROM python:3.13  
 
# durchlaufen vom Erstellen von einem Ordner mit dem Namen app
RUN mkdir /app

# Er steigt in /app ein 
WORKDIR /app
 
# Set environment variables
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Er tut sofrot auf die Konsolle schreiben
ENV PYTHONUNBUFFERED=1
 
# Upgrade pip
RUN pip install --upgrade pip
 
# Copy the Django project and install alles was in den requirements.txt steht
COPY requirements.txt  /app/
 
# run this command to install all dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the Django project to the container in den ordner app, da es als standardverzeichnis weiter oben ausgewählt wurde
COPY . /app/
 
# Expose the Django port, es wird nur der Port 8000 freigegeben
EXPOSE 8000
 
# Run Django’s development server, führt den Befehl aus, damit wir es nicht händisch machen müssen
CMD ["sh", "docker-entrypoint.sh"]
