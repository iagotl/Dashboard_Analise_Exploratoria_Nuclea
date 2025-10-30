import streamlit as st
from PIL import Image
from pathlib import Path

# --- Importar CSS ---
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #3f796c;'>📘 Dicionário de Dados</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='intro-box'>
Nessa primeira aba temos a documentação das bases que utilizamos para realizar as análises.
As duas bases foram cedidas pela Núclea e que balizaram todas as análises realizadas no dashboard
</div>
""", unsafe_allow_html=True)

st.header("📄 Base de Boletos")

st.markdown("""
A **Base de Boletos** é o principal conjunto de dados utilizado neste projeto, servindo como fonte para todas as análises de comportamento financeiro e risco de crédito no contexto das operações de FIDC’s.

Cada linha da tabela representa um **boleto individual** cedido ao fundo, contendo informações desde a sua **emissão** até o **pagamento ou baixa financeira**.
""")

# Pega o diretório raiz do projeto
BASE_DIR = Path(__file__).parent.parent
image = Image.open(BASE_DIR / "assets" / "base_boletos.PNG")
st.image(image, caption="Dicionário de dados da base de boletos")


# --- BASE 2: Base Auxiliar ---
st.header("📊 Base Auxiliar — Liquidez e Materialidade")

st.markdown("""
A **base auxiliar** contém indicadores financeiros calculados a partir dos **CNPJs** relacionados aos boletos da base principal.  
Esses indicadores foram utilizados para enriquecer as análises de risco e consistência dos cedentes.
""")

image_aux = Image.open("assets/base_auxiliar.PNG")  # substitua pelo nome correto do arquivo
st.image(image_aux, caption="Dicionário de dados da base auxiliar", use_container_width=True)


# --- Conclusão da aba ---
st.markdown("""
<div class='intro-box'>
Com essas duas bases, foi possível construir análises abrangentes sobre:<br>
- O comportamento de pagamento dos boletos;<br>
- A saúde financeira dos cedentes;<br>
- E os fatores de risco associados à carteira cedida ao fundo.
</div>
""", unsafe_allow_html=True)
