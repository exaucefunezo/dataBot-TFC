# databot_agent.py - VERSION SIMPLIFIÉE et GARANTIE
import pandas as pd
from datetime import datetime
from modules.db_connector import DatabaseConnector
from modules.chart_generator import ChartGenerator
from modules.memory_manager import MemoryManager

print("="*70)
print("🤖 DATABOT - Assistant Commercial Intelligent")
print("="*70)

# ==================== PARTIE 1 : LES DONNÉES ====================
print("\n📊 PHASE 1 : Préparation des données...")

donnees_commerciales = {
    'Produit': ['Laptop Elite', 'Souris Pro', 'Clavier Mech', 'Écran 4K'],
    'Catégorie': ['Informatique', 'Périphérique', 'Périphérique', 'Informatique'],
    'Ventes_Q1': [156, 342, 198, 87],
    'Ventes_Q2': [142, 367, 213, 92],
    'Prix': [1299.99, 79.99, 149.99, 449.99],
    'Stock': [45, 120, 85, 32]
}

df = pd.DataFrame(donnees_commerciales)
df.to_csv('ventes.csv', index=False)

print(f"✅ Données créées : {len(df)} produits")
print("📁 Fichier : 'ventes.csv'")

# ==================== PARTIE 2 : FONCTIONS D'ANALYSE ====================
print("\n🛠️  PHASE 2 : Création des fonctions d'analyse...")

def analyse_rapide(question):
    """Analyse simple des données"""
    df = pd.read_csv('ventes.csv')
    
    if "plus vendu" in question.lower():
        meilleur = df.loc[(df['Ventes_Q1'] + df['Ventes_Q2']).idxmax()]
        return f"Produit le plus vendu : {meilleur['Produit']} ({meilleur['Ventes_Q1']+meilleur['Ventes_Q2']} unités)"
    
    elif "chiffre" in question.lower() or "ca" in question.lower():
        total = sum((df['Ventes_Q1'] + df['Ventes_Q2']) * df['Prix'])
        return f"Chiffre d'affaires : {total:.2f} €"
    
    elif "liste" in question.lower():
        return f"Produits : {', '.join(df['Produit'].tolist())}"
    
    elif "stock" in question.lower():
        faible = df[df['Stock'] < 50]
        if len(faible) > 0:
            return f"Stock faible : {', '.join(faible['Produit'].tolist())}"
        return "Stock OK pour tous les produits"
    
    return f"Données disponibles : {len(df)} produits, {df['Ventes_Q1'].sum()+df['Ventes_Q2'].sum()} ventes totales"

def rapport_complet():
    """Génère un rapport complet"""
    df = pd.read_csv('ventes.csv')
    df['Ventes_Total'] = df['Ventes_Q1'] + df['Ventes_Q2']
    
    rapport = f"""📊 RAPPORT COMMERCIAL - {datetime.now().strftime('%d/%m/%Y')}
    
Produits analysés : {len(df)}
Ventes totales : {df['Ventes_Total'].sum()} unités
CA total : {(df['Ventes_Total'] * df['Prix']).sum():.2f} €
Stock total : {df['Stock'].sum()} unités

Top produits :
"""
    top = df.nlargest(2, 'Ventes_Total')
    for _, row in top.iterrows():
        rapport += f"• {row['Produit']} : {row['Ventes_Total']} ventes\n"
    
    return rapport

# ==================== PARTIE 3 : VERSION AVEC ou SANS LANGCHAIN ====================
print("\n🧠 PHASE 3 : Configuration de l'assistant...")

try:
    # Essai d'utiliser LangChain si disponible
    from langchain.agents import initialize_agent, AgentType
    from langchain.tools import Tool
    from langchain_mistralai import ChatMistralAI
    
    print("✅ LangChain détecté - mode IA activé")
    
    # Configuration LLM (METTEZ VOTRE CLÉ ICI)
    llm = ChatMistralAI(
        model="mistral-small-latest",
        temperature=0.1,
        mistral_api_key="IsnRG8fdQhCI4OKXZ9U8OO4H7dMIVFgL"  # ← À MODIFIER
    )
    
    # Création des outils
    outils = [
        Tool(name="Analyse", func=analyse_rapide, 
             description="Analyse ventes, CA, stocks, produits"),
        Tool(name="Rapport", func=rapport_complet,
             description="Génère un rapport commercial complet")
    ]
    
    # Création agent
    agent = initialize_agent(
        tools=outils,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=3
    )
    
    mode_ia = True
    print("🤖 Agent IA créé avec succès")
    
except ImportError:
    print("⚠️  LangChain non disponible - mode simple activé")
    mode_ia = False
except Exception as e:
    print(f"⚠️  Erreur configuration IA: {e}")
    print("🔄 Passage en mode simple")
    mode_ia = False

# ==================== PARTIE 4 : DÉMONSTRATION ====================
print("\n" + "="*70)
print("🎯 DÉMONSTRATION")
print("="*70)

questions = [
    "Quel est le produit le plus vendu ?",
    "Donne le chiffre d'affaires",
    "Quels produits en stock faible ?"
]

for i, q in enumerate(questions, 1):
    print(f"\n{i}. ❓ {q}")
    print("-" * 40)
    
    if mode_ia:
        try:
            reponse = agent.run(q)
            print(f"🤖 {reponse}")
        except:
            print(f"📊 {analyse_rapide(q)}")
    else:
        print(f"📊 {analyse_rapide(q)}")
    
    print("-" * 40)

# ==================== PARTIE 5 : INTERFACE UTILISATEUR ====================
print("\n" + "="*70)
print("💬 MODE INTERACTIF")
print("="*70)

if mode_ia:
    print("Mode : 🤖 IA (LangChain + Mistral)")
else:
    print("Mode : 📊 Analyse simple (sans IA)")

print("\nCommandes : quit, rapport, donnees, aide")

while True:
    question = input("\n👤 Question : ").strip()
    
    if question.lower() in ['quit', 'exit', 'q']:
        print("\n👋 Au revoir !")
        break
    
    elif question.lower() == 'aide':
        print("\n💡 Questions possibles :")
        print("• 'plus vendu' - Produit le plus vendu")
        print("• 'chiffre affaires' - CA total")
        print("• 'stock faible' - Produits à réapprovisionner")
        print("• 'liste' - Tous les produits")
        print("• 'rapport' - Rapport complet")
        continue
    
    elif question.lower() == 'rapport':
        print("\n" + rapport_complet())
        continue
    
    elif question.lower() == 'donnees':
        print(f"\n📋 {len(df)} PRODUITS :")
        print(df.to_string())
        continue
    
    if not question:
        continue
    
    print("\n" + "="*30)
    
    if mode_ia:
        try:
            reponse = agent.run(question)
            print(f"🤖 {reponse}")
        except Exception as e:
            print(f"⚠️  Erreur IA: {e}")
            print(f"📊 {analyse_rapide(question)}")
    else:
        print(f"📊 {analyse_rapide(question)}")
    
    print("="*30)

print("\n" + "="*70)
print("📈 ANALYSE TERMINÉE")
print("="*70)
print(f"• Produits analysés : {len(df)}")
print(f"• Données sauvegardées : ventes.csv")
print(f"• Mode utilisé : {'IA 🤖' if mode_ia else 'Simple 📊'}")
print("="*70)