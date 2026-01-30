# 📖 Guide d'Installation Détaillée

## Table des Matières
- [Prérequis Système](#prérequis-système)
- [Installation Rapide](#installation-rapide)
- [Installation Manuelle](#installation-manuelle)
- [Configuration](#configuration)
- [Dépannage](#dépannage)
- [Mise à Jour](#mise-à-jour)

## Prérequis Système

### 🖥️ Configuration minimale
- **Processeur** : 2 cores minimum (4 recommandés)
- **Mémoire RAM** : 4 GB minimum (8 GB recommandés)
- **Espace disque** : 1 GB libre
- **Système d'exploitation** :
  - Windows 10/11 (64-bit)
  - macOS 10.14+
  - Linux (Ubuntu 20.04+, Fedora, CentOS)

### 📦 Logiciels requis
- **Python 3.8+** - [Télécharger Python](https://www.python.org/downloads/)
- **Git** - [Télécharger Git](https://git-scm.com/)
- **Éditeur de code** (optionnel) :
  - [VS Code](https://code.visualstudio.com/)
  - [PyCharm](https://www.jetbrains.com/pycharm/)

### 🌐 Connexion Internet
- Requise pour l'installation des packages
- Requise pour l'API Mistral AI (analyse en ligne)

## Installation Rapide

### 🚀 Installation en 5 minutes (Windows)
```powershell
# 1. Ouvrir PowerShell en administrateur
# 2. Exécuter ces commandes :

# Cloner le projet
git clone https://github.com/votre-username/DataBot-TFC.git
cd DataBot-TFC

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement
.\venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer l'environnement
copy .env.example .env

# Lancer l'application
streamlit run webapp/app_streamlit.py