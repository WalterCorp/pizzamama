# 🍕 Pizza Mama — Site vitrine Django

## 📌 Présentation du projet

Pizza Mama est un site vitrine développé avec Django permettant de présenter une carte de pizzas de manière moderne, claire et responsive.

L’objectif du projet est de démontrer la capacité à concevoir une application web complète, en structurant à la fois :

* le back-end (modèles, logique métier, administration)
* le front-end (templates, styles, expérience utilisateur)
* la gestion des données (CRUD via interface admin)

---

## 🎯 Objectifs

* Concevoir une application web avec Django
* Mettre en place une architecture claire et maintenable
* Gérer un catalogue de produits dynamiques (pizzas)
* Proposer une interface utilisateur fluide et responsive
* Implémenter des fonctionnalités de filtrage et de tri

---

## ⚙️ Stack technique

* **Backend** : Django (Python)
* **Frontend** : HTML / CSS (custom)
* **Base de données** : SQLite (par défaut Django)
* **Templates** : Django Template Language (DTL)
* **Gestion des assets** : fichiers statiques (images locales, CSS)

---

## 🚀 Fonctionnalités principales

### 📋 Catalogue de pizzas

* Affichage dynamique des pizzas
* Catégorisation (classique, signature, etc.)
* Mise en avant des pizzas signatures

### 🔍 Filtres et recherche

* Recherche par mot-clé
* Filtre par catégorie
* Filtre végétarien
* Tri par prix ou nom

### 📄 Page détail

* Affichage complet d’une pizza
* Ingrédients
* Prix
* Disponibilité
* Suggestions de pizzas similaires

### 🛠️ Interface d’administration

* Ajout / modification / suppression des pizzas
* Gestion des images via chemins statiques
* Gestion des catégories et attributs

---

## 🧱 Structure du projet

```bash
PizzaMama/
│
├── manage.py
├── db.sqlite3
│
├── menu/                # Application principale
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── main/
│   └── menu/
│
├── static/
│   ├── global.css
│   ├── favicon.ico
│   └── menu/images/pizzas/
│
└── venv/ (non versionné)
```

---

## ▶️ Lancer le projet en local

```bash
python3 -m venv venv
source venv/bin/activate
pip install django

python3 manage.py migrate
python3 manage.py runserver
```

Accès :

* Site : http://127.0.0.1:8000/
* Admin : http://127.0.0.1:8000/admin/

---

## 🧠 Choix techniques

### Django

Choisi pour :

* rapidité de développement
* structure MVC claire
* interface admin intégrée
* gestion simple des données

### Templates Django

Permettent :

* séparation logique / affichage
* rendu dynamique simple
* bonne lisibilité du code

### Images locales

* meilleure maîtrise du rendu
* pas de dépendance externe
* cohérence visuelle du projet

---

## 🎨 Expérience utilisateur

* Design moderne et épuré
* Navigation simple et intuitive
* Responsive (mobile / desktop)
* Mise en avant visuelle des produits

---

## 📈 Axes d’amélioration

* Intégration d’un système de commande en ligne
* Authentification utilisateur
* API REST (Django REST Framework)
* Upload d’images via l’admin
* Déploiement (Vercel / Railway / Render)

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre d’une formation Python
Objectif : démonstration de compétences en développement web fullstack avec Django

---
