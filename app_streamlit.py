# app_streamlit.py - Interface Web pour votre DataBot
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="DataBot - Assistant Commercial IA",
    page_icon="🤖",
    layout="wide"
)

# Titre principal
st.title("🤖 DataBot - Assistant Commercial IA")
st.markdown("---")

# Sidebar avec configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Upload de fichiers
    uploaded_file = st.file_uploader(
        "📂 Importer des données CSV",
        type=['csv'],
        help="Importez vos propres données de vente"
    )
    
    # Sélection du modèle
    mode_analyse = st.selectbox(
        "Mode d'analyse",
        ["Standard", "Avancé", "Prédictif"]
    )
    
    # Paramètres
    avec_ia = st.checkbox("Activer l'IA", value=True)
    st.info("L'IA permet des analyses avancées et des recommandations")

# Section 1 : Tableau de bord
st.header("📊 Tableau de Bord")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Produits", "10", "+2")
with col2:
    st.metric("Ventes Totales", "2,156", "12%")
with col3:
    st.metric("CA Total", "452,899€", "8%")
with col4:
    st.metric("Satisfaction", "94%", "3%")

# Section 2 : Visualisations
st.header("📈 Visualisations")

# Données d'exemple
donnees = {
    'Produit': ['Laptop', 'Souris', 'Clavier', 'Écran', 'Casque'],
    'Ventes': [156, 342, 198, 87, 231],
    'CA': [202,799, 27,359, 29,698, 39,189, 46,199],
    'Croissance': [12, 25, 8, -3, 18]
}
df_viz = pd.DataFrame(donnees)

tab1, tab2, tab3 = st.tabs(["📦 Ventes", "💰 Revenus", "📈 Tendences"])

with tab1:
    fig = px.bar(df_viz, x='Produit', y='Ventes', title="Ventes par Produit")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.pie(df_viz, values='CA', names='Produit', title="Répartition du CA")
    st.plotly_chart(fig, use_container_width=True)

# Section 3 : Interface Question/Réponse
st.header("💬 Assistant IA")

# Historique des questions
if 'historique' not in st.session_state:
    st.session_state.historique = []

# Input utilisateur
question = st.text_input(
    "Posez votre question à DataBot :",
    placeholder="Ex: Quel est notre produit le plus rentable ?"
)

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    if st.button("🚀 Analyser", type="primary"):
        if question:
            # Simulation de réponse
            reponse = f"**Analyse de :** {question}\n\n"
            reponse += "✅ **Produit le plus rentable :** Laptop Elite\n"
            reponse += "   • Ventes : 156 unités\n"
            reponse += "   • CA : 202,799 €\n"
            reponse += "   • Marge : 35%\n\n"
            reponse += "💡 **Recommandation :** Augmenter le stock de 20%"
            
            st.session_state.historique.append({
                'question': question,
                'reponse': reponse,
                'timestamp': datetime.now().strftime("%H:%M")
            })
            
            st.success("Analyse terminée !")
            st.markdown(reponse)

with col_btn2:
    if st.button("📊 Générer Rapport"):
        with st.spinner("Génération du rapport..."):
            rapport = """
            ## 📋 Rapport Commercial Complet
            
            ### 1. Performance Globale
            - CA Total : 452,899 €
            - Ventes : 2,156 unités
            - Croissance : +15% vs période précédente
            
            ### 2. Top Performers
            1. **Souris Pro** : 342 unités (+25%)
            2. **Laptop Elite** : 156 unités (+12%)
            3. **Casque Audio** : 231 unités (+18%)
            
            ### 3. Recommandations
            - 🔼 Augmenter production Souris Pro
            - 📊 Lancer promotion Clavier Mech
            - ⚠️ Surveiller stock Écran 4K
            """
            st.markdown(rapport)

# Historique
if st.session_state.historique:
    st.subheader("📝 Historique des Analyses")
    for i, echange in enumerate(reversed(st.session_state.historique[-5:])):
        with st.expander(f"{echange['timestamp']} - {echange['question'][:50]}..."):
            st.markdown(echange['reponse'])

# Section 4 : Export
st.header("📤 Export des Données")

col_exp1, col_exp2, col_exp3 = st.columns(3)
with col_exp1:
    if st.button("📄 Exporter en CSV"):
        st.success("Données exportées : analyse.csv")
with col_exp2:
    if st.button("📊 Exporter Graphiques"):
        st.success("Graphiques exportés")
with col_exp3:
    if st.button("📋 Rapport PDF"):
        st.success("PDF généré")

# Footer
st.markdown("---")
st.caption("DataBot v1.0 • Projet de Fin d'Études • Génie Informatique")