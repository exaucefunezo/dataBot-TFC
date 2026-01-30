# diagnostic.py
import sys
print("="*50)
print("DIAGNOSTIC DU SYSTÈME")
print("="*50)
print(f"Python: {sys.version}")
print(f"Chemin: {sys.executable}")

packages = ["langchain", "langchain_community", "pandas", "numpy", "langchain_mistralai"]

for package in packages:
    try:
        mod = __import__(package)
        version = getattr(mod, '__version__', 'Version inconnue')
        print(f"✅ {package}: {version}")
    except ImportError:
        print(f"❌ {package}: NON INSTALLÉ")
    except Exception as e:
        print(f"⚠️  {package}: Erreur - {e}")

print("="*50)