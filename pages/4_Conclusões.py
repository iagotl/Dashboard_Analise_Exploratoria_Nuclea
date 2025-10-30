import streamlit as st

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Título principal ---
st.markdown("<h1 style='text-align: center; color: #3f796c;'>📚 Conclusões — Análise Exploratória de Boletos</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='intro-box'>
Esta seção apresenta as principais conclusões obtidas na análise exploratória dos boletos.  
As observações abaixo sintetizam os principais achados e direcionam os indicadores que serão levados ao dashboard final.
</div>
""", unsafe_allow_html=True)

# ============================================================
# 📆 ANÁLISES TEMPORAIS
# ============================================================
st.header("📆 Análises Temporais")

st.markdown("""
- **Contagem de boletos por ano/mês de emissão**
  - As emissões iniciam em **jan/2021**, mas **não são consistentes ao longo do tempo**, apresentando lacunas.
  - Há uma concentração de emissões em **mar/2024 e abr/2024**, muito acima da média histórica.
  - As emissões **encerram em mai/2024**.

- **Contagem de boletos por ano/mês de vencimento**
  - Todos os boletos têm **vencimento em mai/2024** — inclusive os emitidos em anos anteriores.
  - Não há concentração relevante por dia específico, apenas uma leve redução em finais de semana (esperado).
  - Essa homogeneidade de vencimentos merece destaque no dashboard, pois pode indicar **padronização ou algum tipo de peculiaridade do fundo**.

- **Contagem de boletos por ano/mês de pagamento**
  - Aproximadamente **87% dos boletos** foram pagos no mesmo mês de vencimento (05/2024).
  - Há um **pico atípico em jul/2024**, com concentração de pagamentos em um único dia.
    - Mesmo sem causa clara, o evento é relevante e será destacado visualmente.
""")

# ============================================================
# 💰 ANÁLISES FINANCEIRAS
# ============================================================
st.header("💰 Análises Financeiras")

st.markdown("""
- **Valores gerais**.
  - A **média e a mediana** do valor nominal são **muito diferentes**, sugerindo **alta dispersão e presença de outliers**.
  - O **desvio padrão** é elevado e, portanto, pouco representativo — optou-se por observar a **distância interquartil (IQR)** como medida robusta para a análise de dispersão:
    - Distância interquartil: **R$ 8.971,00**
    - Quantil 90: 47.026,45 → 90% dos boletos estão abaixo de R$ 47 mil.
  - Existem boletos variando de **7,00** a **3.000.000,00**, evidenciando **amplitude extrema** nos valores nominais.

- **Distribuição por tipo de espécie**
  - Mais de **90%** dos boletos pertencem a duas categorias:
    - *DM — Duplicata Mercantil (85%)*
    - *DMI — Duplicata Mercantil Indicação (11%)*
  - A distribuição por **valor nominal** segue o mesmo padrão da **quantidade**, reforçando a necessidade de foco nessas espécies de boletos.

- **Atrasos e Multas**
  - Aproximadamente **29,3% dos boletos** foram pagos com atraso (**2087 casos**):
    - Atraso médio: **16 dias**
    - Mediana de atraso: **3 dias**
    - Maior atraso: **219 dias**
    - Valor total arrecadado em multas: **R$ 124.261,61**

- **Inadimplência**
  - Valor total inadimplente: **R$ 2.085.711.07**
  - Quantidade de boletos inadimplentes: **70**
  - Valor mediano dos boletos inadimplentes: **R$ 4.925,25**
  - O maior boleto inadimplente é no valor de **R$ 400.000,00**.
  - **Taxas de inadimplência:**
    - Por valor / quantidade: **1%**
  - Um ponto interessante de observar é que temos mais de 50% do total de inadimplência concentrado em apenas 2 pagadores.
""")