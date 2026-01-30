# final_diagnostic.py
import sys
print("="*70)
print("🎯 DIAGNOSTIC FINAL - PRÊT POUR L'AGENT IA")
print("="*70)

# Vérification Python
print(f"🐍 Python: {sys.version.split()[0]}")
print(f"📁 Environnement: {sys.executable}")

# Vérification packages critiques
packages = {
    "numpy": "NumPy (calcul scientifique)",
    "pandas": "Pandas (analyse données)", 
    "langchain": "LangChain (framework IA)",
    "langchain_community": "LangChain Community",
    "langchain_mistralai": "Intégration Mistral AI"
}

print("\n📦 PACKAGES INSTALLÉS :")
print("-" * 50)

all_ok = True
for package, description in packages.items():
    try:
        __import__(package)
        print(f"✅ {package:25} -> {description}")
    except ImportError:
        print(f"❌ {package:25} -> MANQUANT: {description}")
        all_ok = False

print("-" * 50)

if all_ok:
    print("🎉 TOUT EST PRÊT ! L'agent IA peut être créé.")
else:
    print("⚠️  Certains packages manquent.")

print("="*70)