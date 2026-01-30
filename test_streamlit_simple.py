# test_streamlit_simple.py - TEST ULTRA SIMPLE
import streamlit as st

st.title("🎯 TEST STREAMLIT - DataBot")
st.write("Si vous voyez ce texte, Streamlit fonctionne !")

# Test bouton
if st.button("Cliquez-moi"):
    st.success("✅ Streamlit fonctionne parfaitement !")

# Test slider
valeur = st.slider("Choisissez une valeur", 0, 100, 50)
st.write(f"Valeur sélectionnée : {valeur}")

st.info("""
**Prochaines étapes :**
1. Si ce test fonctionne, copiez le code dans webapp/app_streamlit.py
2. Exécutez : streamlit run webapp/app_streamlit.py
""")