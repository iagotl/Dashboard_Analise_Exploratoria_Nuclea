import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="FIDC Dashboard - Boletos",
    page_icon="💰",
    layout="wide"
)

# --- Importar CSS ---
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.success("Selecione uma página acima 👆")

# --- Título Principal ---
st.markdown("<h1 style='text-align: center; color: #3f796c;'>💰 Dashboard FIDC - Análise de Boletos</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
Bem-vindo ao painel interativo de **Análise de Boletos em FIDC’s**.  
Aqui você poderá explorar dados financeiros de boletos cedidos, avaliando **pagamentos, atrasos e séries temporais**.

Use o menu lateral para navegar entre as seções do dashboard.
""")
