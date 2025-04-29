# 📸 Daily Capture

**Daily Capture** est une application web privée pour capturer et organiser les réalisations quotidiennes de moi et mes neveux.

Chaque jour, nous postons nos projets en photo, gardant une trace de notre productivité et de nos progrès.

---

## 🚀 Objectif

- Uploader une photo + une description rapide
- Classer automatiquement les photos par date
- Partager facilement les photos sur un salon Discord via webhook
- Créer une archive de nos réalisations

---

## 🛠️ Technologies utilisées

- Python 3
- Flask
- SQLite
- HTML / CSS (Vanilla)
- Webhooks Discord

---

## 🗂️ Structure du projet

photo-journey/
│
├── app/
│   ├── static/
│   │   └── uploads/      # Ici seront stockées les photos uploadées
│   ├── templates/
│   │   ├── index.html     # Page d'accueil pour voir les photos
│   │   ├── upload.html    # Page pour envoyer une photo
│   ├── __init__.py        # Démarrage de ton app Flask
│   ├── routes.py          # Tes routes principales (upload, affichage)
│   ├── models.py          # Ta base de données (Photo model)
│   └── utils.py           # (optionnel) pour gérer l'envoi sur Discord
│
├── config.py              # Configuration Flask (chemins, sécurité)
├── requirements.txt       # Les librairies Python à installer
├── README.md              # Explication de ton projet
└── run.py                 # Lancement de ton application


## 🧩 Installation

1. Clone le projet :

```bash
git clone https://github.com/ton-utilisateur/Daily-capture.git
cd Daily-capture

python3 -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
# Installation des dépendances
pip install -r requirements.txt
# Lancement
python run.py
```


🔗 Utilisation
Accéder à http://127.0.0.1:5000
Uploader vos photos et voir votre galerie
Partager vos réalisations sur Discord !
