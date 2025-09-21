# Logiciel de Vente

Application full-stack avec Django (backend) et React (frontend) pour la gestion des ventes.

## 🚀 Technologies utilisées

### Backend
- Django
- Django REST Framework
- Django REST Framework SimpleJWT (authentification)
- django-cors-headers

### Frontend
- React
- React Router
- Axios
- JWT Authentication

## 📋 Prérequis

- Python 3.8+
- Node.js 14+
- npm ou yarn

## ⚙️ Installation

### Backend (Django)

1. Naviguer vers le dossier backend :
```bash
cd backend
```

2. Créer un environnement virtuel :
```bash
python -m venv virtuel
```

3. Activer l'environnement virtuel :
```bash
# Windows
virtuel\Scripts\activate

# macOS/Linux
source virtuel/bin/activate
```

4. Installer les dépendances :
```bash
pip install -r requirements.txt
```

5. Effectuer les migrations :
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Créer un superutilisateur :
```bash
python manage.py createsuperuser
```

7. Démarrer le serveur :
```bash
python manage.py runserver
```

Le backend sera accessible sur `http://127.0.0.1:8000/`

### Frontend (React)

1. Naviguer vers le dossier frontend :
```bash
cd frontend
```

2. Installer les dépendances :
```bash
npm install
```

3. Démarrer le serveur de développement :
```bash
npm start
```

Le frontend sera accessible sur `http://localhost:3000/`

## 🔧 Configuration

### Variables d'environnement Backend

Créer un fichier `.env` dans le dossier `backend` :
```env
SECRET_KEY=votre-cle-secrete-django
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### Variables d'environnement Frontend

Créer un fichier `.env` dans le dossier `frontend` :
```env
REACT_APP_API_BASE_URL=http://127.0.0.1:8000/api/
```

## 📚 Utilisation

1. Démarrer le backend Django sur le port 8000
2. Démarrer le frontend React sur le port 3000
3. Accéder à l'application via `http://localhost:3000`
4. Se connecter avec les identifiants créés

## 🐛 Problèmes connus

- Assurez-vous que CORS est correctement configuré
- Vérifiez que les utilisateurs sont actifs dans l'admin Django
- Les tokens JWT expirent après 1 heure par défaut

## 📝 API Endpoints

- `POST /api/token/` - Obtenir un token d'accès
- `POST /api/token/refresh/` - Rafraîchir le token
- Plus d'endpoints à documenter...

## 🤝 Contribution

1. Forker le projet
2. Créer une branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committer les changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Pusher vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Créer une Pull Request

## 📄 Licence

Ce projet est sous licence MIT.