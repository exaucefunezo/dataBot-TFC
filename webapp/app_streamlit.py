# webapp/app_streamlit.py - VERSION GARANTIE
import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURATION DE BASE
st.set_page_config(
    page_title="DataBot - Assistant Commercial",
    page_icon="🤖",
    layout="wide"
)

# TITRE PRINCIPAL - S'AFFICHE TOUJOURS
st.title("🤖 DataBot - Assistant Commercial IA")
st.markdown("**Projet de Fin d'Études - Analyse de Données par Intelligence Artificielle**")
st.markdown("---")

# SECTION 1 : DONNÉES DE DÉMO (TOUJOURS VISIBLE)
st.header("📊 Données de Démonstration")

# Création de données garanties
data = {
    'Produit': ['Laptop Pro', 'Souris Gaming', 'Clavier Méca', 'Écran 27"', 'Casque Bluetooth'],
    'Catégorie': ['Informatique', 'Périphérique', 'Périphérique', 'Informatique', 'Audio'],
    'Ventes': [150, 320, 180, 85, 210],
    'Prix (€)': [1299.99, 79.99, 149.99, 449.99, 199.99],
    'Stock': [42, 115, 78, 28, 55]
}

df = pd.DataFrame(data)

# Afficher le tableau TOUJOURS visible
st.subheader("Tableau des Produits")
st.dataframe(df, use_container_width=True)

# SECTION 2 : MÉTRIQUES (TOUJOURS VISIBLE)
st.header("📈 Métriques Clés")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_ventes = df['Ventes'].sum()
    st.metric("Ventes Total", f"{total_ventes:,}", "+12.5%")

with col2:
    ca_total = (df['Ventes'] * df['Prix (€)']).sum()
    st.metric("Chiffre d'Affaires", f"{ca_total:,.0f} €", "+8.2%")

with col3:
    stock_faible = len(df[df['Stock'] < 50])
    st.metric("Stock Critique", stock_faible, "⚠️" if stock_faible > 0 else "✅")

with col4:
    prix_moyen = df['Prix (€)'].mean()
    st.metric("Prix Moyen", f"{prix_moyen:.0f} €", "-2.1%")

# SECTION 3 : VISUALISATIONS (TOUJOURS VISIBLE)
st.header("📊 Visualisations")

# Tab 1 : Graphique à barres
tab1, tab2, tab3 = st.tabs(["📦 Ventes", "💰 Prix", "📈 Relation"])

with tab1:
    fig1 = px.bar(
        df,
        x='Produit',
        y='Ventes',
        color='Catégorie',
        title="Ventes par Produit"
    )
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    fig2 = px.pie(
        df,
        values='Prix (€)',
        names='Produit',
        title="Répartition des Prix"
    )
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    fig3 = px.scatter(
        df,
        x='Prix (€)',
        y='Ventes',
        size='Stock',
        color='Catégorie',
        hover_name='Produit',
        title="Relation Prix-Ventes-Stock"
    )
    st.plotly_chart(fig3, use_container_width=True)

# SECTION 4 : SIMULATEUR D'IA (TOUJOURS VISIBLE)
st.header("💬 Assistant IA - Simulation")

# Initialisation session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Bonjour ! Je suis DataBot. Posez-moi des questions sur vos données commerciales."}
    ]

# Afficher historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input utilisateur
prompt = st.chat_input("Ex: 'Quel produit a les meilleures ventes ?'")

if prompt:
    # Ajouter message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Simuler réponse IA
    with st.chat_message("assistant"):
        with st.spinner("DataBot analyse..."):
            # Logique de réponse simple
            if "ventes" in prompt.lower() and "meilleur" in prompt.lower():
                meilleur = df.loc[df['Ventes'].idxmax()]
                reponse = f"**Produit avec les meilleures ventes** : {meilleur['Produit']} ({meilleur['Ventes']} unités)"
            
            elif "stock" in prompt.lower() and "faible" in prompt.lower():
                faibles = df[df['Stock'] < 50]
                if len(faibles) > 0:
                    liste = ", ".join(faibles['Produit'].tolist())
                    reponse = f"⚠️ **Produits en stock faible** : {liste}"
                else:
                    reponse = "✅ **Tous les produits ont un stock suffisant**"
            
            elif "prix" in prompt.lower() and "moyen" in prompt.lower():
                reponse = f"**Prix moyen des produits** : {prix_moyen:.2f} €"
            
            elif "bonjour" in prompt.lower() or "salut" in prompt.lower():
                reponse = "Bonjour ! Je suis DataBot, votre assistant commercial IA. Posez-moi des questions sur vos ventes, stocks ou performances."
            
            else:
                reponse = f"**Analyse de votre demande** : '{prompt}'\n\n"
                reponse += f"Basé sur nos données ({len(df)} produits) :\n"
                reponse += f"- Ventes totales : {total_ventes} unités\n"
                reponse += f"- CA généré : {ca_total:,.0f} €\n"
                reponse += f"- {stock_faible} produit(s) nécessite(nt) réapprovisionnement"
            
            st.write(reponse)
    
    # Ajouter à l'historique
    st.session_state.messages.append({"role": "assistant", "content": reponse})

# SECTION 5 : RAPPORTS (TOUJOURS VISIBLE)
st.header("📋 Génération de Rapports")

if st.button("📄 Générer Rapport Complet", type="primary", use_container_width=True):
    with st.expander("📊 RAPPORT COMMERCIAL DATABOT", expanded=True):
        st.markdown(f"""
        ### 🏢 Rapport Commercial - DataBot Analysis
        
        **Période d'analyse** : Données actuelles
        **Nombre de produits** : {len(df)}
        
        #### 📈 Performance Commerciale
        - **Ventes totales** : {total_ventes:,} unités
        - **Chiffre d'affaires** : {ca_total:,.0f} €
        - **Valeur moyenne par vente** : {ca_total/total_ventes:.2f} €
        
        #### 🏆 Classement des Produits
        1. **{df.loc[df['Ventes'].idxmax()]['Produit']}** : {df['Ventes'].max()} ventes
        2. **{df.loc[df['Prix (€)'].idxmax()]['Produit']}** : {df['Prix (€)'].max():.0f} € (plus cher)
        3. **{df.loc[df['Stock'].idxmax()]['Produit']}** : {df['Stock'].max()} unités en stock
        
        #### ⚠️ Points de Vigilance
        - **Produits à réapprovisionner** : {stock_faible}
        - **Prix moyen** : {prix_moyen:.2f} €
        - **Ratio stock/ventes** : {df['Stock'].sum()/total_ventes:.2f}
        
        #### 💡 Recommandations DataBot
        1. Surveiller le stock des produits critiques
        2. Analyser la demande par catégorie
        3. Optimiser les prix basé sur la demande
        """)

# SECTION 6 : EXPORT (TOUJOURS VISIBLE)
st.header("📤 Export des Données")

col_exp1, col_exp2, col_exp3 = st.columns(3)

with col_exp1:
    if st.button("💾 Exporter CSV", use_container_width=True):
        df.to_csv("export_databot.csv", index=False)
        st.success("✅ export_databot.csv créé")

with col_exp2:
    if st.button("📊 Exporter Graphiques", use_container_width=True):
        fig1.write_image("ventes_par_produit.png")
        st.success("✅ Graphiques exportés")

with col_exp3:
    if st.button("🖨️ Copier Rapport", use_container_width=True):
        st.info("Utilisez Ctrl+C pour copier l'écran")

# PIED DE PAGE (TOUJOURS VISIBLE)
st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p><b>🤖 DataBot v1.0</b> - Projet de Fin d'Études en Informatique</p>
    <p><small>Assistant IA d'analyse commerciale | Développé avec Python, Streamlit et Plotly</small></p>
</div>
""", unsafe_allow_html=True)

# MESSAGE DE DÉBOGAGE (visible en bas)
st.sidebar.markdown("---")
st.sidebar.caption(f"Debug : {len(df)} lignes | Streamlit OK")