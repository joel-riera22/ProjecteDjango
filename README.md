# Projecte Django Joel Riera - MP03 Bloc 6

## 1. Introducció
   Aquest projecte és un blog personal creat amb Django que permet mostrar posts, autors i etiquetes. Està pensat per practicar models relacionats, vistes dinàmiques, gestió de dades i ús de l'admin de Django.  
   L'objectiu principal és tenir una aplicació funcional amb interfície web per gestionar i visualitzar articles relacionats amb autors i tags.

## 2. Instal·lació ràpida
## 2.1. Clonar el repositori
  ```bash
  git clone https://github.com/joel-riera22/ProjecteDjango.git
  cd ProjecteDjango

## 2.2. Crear i activar entorn virtual
  python -m venv venv
  source venv/bin/activate

## 2.3. Instal·lar dependències
  pip install django
  python -m pip install --upgrade pip
  python -m pip install Pillow
  pip install -r requirements.txt

## 2.4. Executar migracions
  python manage.py makemigrations
  python manage.py migrate

## 3. Execució del projecte
## 3.1. Executar el servidor localment
  python manage.py runserver

# 3.2. URL per accedir al projecte
  http://127.0.0.1:8000/
