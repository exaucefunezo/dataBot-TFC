# test_complet.py - VÉRIFICATION DU PROJET
import os
import sys

print("🔍 VÉRIFICATION COMPLÈTE DU PROJET DATABOT")
print("="*60)

# Liste des fichiers requis
required_files = [
    ('webapp/app_streamlit.py', 'Interface web'),
    ('src/main.py', 'Point d\'entrée'),
    ('src/agent.py', 'Agent IA'),
    ('requirements.txt', 'Dépendances'),
    ('.env.example', 'Configuration exemple'),
    ('data/', 'Dossier données'),
    ('docs/', 'Documentation')
]

print("\n📁 STRUCTURE DU PROJET:")
print("-" * 40)

all_ok = True
for file_path, description in required_files:
    exists = os.path.exists(file_path)
    status = "✅" if exists else "❌"
    print(f"{status} {file_path:30} - {description}")
    if not exists:
        all_ok = False

# Vérification Python
print("\n🐍 ENVIRONNEMENT PYTHON:")
print("-" * 40)
print(f"Version: {sys.version.split()[0]}")
print(f"Chemin: {sys.executable}")

# Vérification packages
print("\n📦 PACKAGES INSTALLÉS:")
print("-" * 40)

packages_to_check = ['streamlit', 'pandas', 'plotly', 'langchain']
try:
    import importlib
    for package in packages_to_check:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NON INSTALLÉ")
            all_ok = False
except:
    print("⚠️  Impossible de vérifier les packages")

print("\n" + "="*60)
if all_ok:
    print("🎉 PROJET PRÊT À FONCTIONNER !")
    print("\n🚀 COMMANDES À EXÉCUTER:")
    print("1. streamlit run webapp/app_streamlit.py")
    print("2. python src/main.py")
else:
    print("⚠️  PROBLÈMES DÉTECTÉS")
    print("💡 Créez les fichiers manquants")

print("="*60)