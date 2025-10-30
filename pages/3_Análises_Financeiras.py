import streamlit as st
import pandas as pd
import plotly.express as px

# --- Importar CSS ---
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Estilo extra específico para os cards ---
st.markdown("""
<style>
.kpi-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    margin-top: 25px;
}

.kpi-card {
    background-color: #f8faf9;
    border-left: 8px solid #3f796c;
    border-radius: 15px;
    padding: 25px 35px;
    width: 250px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    text-align: center;
}
.kpi-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.kpi-value {
    font-size: 1.4rem;
    font-weight: bold;
    color: #002873;
    margin-bottom: 8px;
}
.kpi-label {
    font-size: 0.9rem;
    color: #3f796c;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}
</style>
""", unsafe_allow_html=True)

# --- Título principal ---
st.markdown("<h1 style='text-align: center; color: #3f796c;'>📈 Análises Financeiras</h1>", unsafe_allow_html=True)

# ============================================================
# 📊 CARREGA BASE
# ============================================================
df = pd.read_csv("data/base_tratada_nuclea.csv", low_memory=False)
df["vlr_nominal"] = pd.to_numeric(df["vlr_nominal"], errors="coerce")
df["vlr_baixa"] = pd.to_numeric(df["vlr_baixa"], errors="coerce")

# ============================================================
# 🧮 MÉTRICAS PRINCIPAIS
# ============================================================

valor_inadimplente = df[df["inadimplente"] == 1]["vlr_nominal"].sum()
valor_total_emitido = df["vlr_nominal"].sum()
valor_total_baixas = df["vlr_baixa"].sum()
mediana_nominal = df["vlr_nominal"].median()
valor_maximo_nominal = df["vlr_nominal"].max()
valor_minimo_nominal = df["vlr_nominal"].min()
total_boletos = len(df)
boletos_pagos = df["vlr_baixa"].notna().sum()
pct_pagos = (boletos_pagos / total_boletos) * 100 if total_boletos > 0 else 0

# ============================================================
# 💡 CARDS GERENCIAIS PERSONALIZADOS
# ============================================================
st.markdown(f"""
<div class="kpi-container">
    <div class="kpi-card">
        <div class="kpi-value">R$ {valor_total_emitido:,.2f}</div>
        <div class="kpi-label">Valor Total Emitido</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">R$ {valor_total_baixas:,.2f}</div>
        <div class="kpi-label">Valor Total de Baixas</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">R$ {valor_inadimplente:,.2f}</div>
        <div class="kpi-label">Valor Inadimplente</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">R$ {mediana_nominal:,.2f}</div>
        <div class="kpi-label">Mediana do Valor Nominal</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">R$ {valor_maximo_nominal:,.2f}</div>
        <div class="kpi-label">Valor Máximo Nominal</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">R$ {valor_minimo_nominal:,.2f}</div>
        <div class="kpi-label">Valor Mínimo Nominal</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">{pct_pagos:.1f}%</div>
        <div class="kpi-label">Percentual de Boletos Pagos</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 🔸 ESPAÇAMENTO VISUAL
# ============================================================
st.markdown("<br><br><hr style='border: 1px solid #eaeaea'><br>", unsafe_allow_html=True)

# ============================================================
# 💰 DISTRIBUIÇÃO DO VALOR NOMINAL POR TIPO DE BAIXA
# ============================================================
st.subheader("💰 Distribuição do Valor Nominal por Tipo de Baixa")

df_tipo_baixa = df.dropna(subset=["tipo_baixa"])
baixa_agg = (
    df_tipo_baixa.groupby("tipo_baixa", as_index=False)["vlr_nominal"]
    .sum()
    .sort_values("vlr_nominal", ascending=False)
)

fig_baixa = px.bar(
    baixa_agg,
    x="tipo_baixa",
    y="vlr_nominal",
    text_auto=".2s",
    title="Valor Total Emitido por Tipo de Baixa",
    color_discrete_sequence=["#3f796c"]
)

fig_baixa.update_traces(
    hovertemplate="<b>Tipo de Baixa:</b> %{x}<br><b>Valor:</b> R$ %{y:,.2f}<extra></extra>",
    textposition="outside"
)
fig_baixa.update_layout(
    title_x=0.5,
    xaxis_title="Tipo de Baixa",
    yaxis_title="Valor Nominal (R$)",
    title_font=dict(color="#3f796c", size=18),
    font=dict(color="#002873", size=13),
    plot_bgcolor="white",
    paper_bgcolor="white",
)
st.plotly_chart(fig_baixa, use_container_width=True, key="grafico_tipo_baixa")

# ============================================================
# 🔸 ESPAÇAMENTO VISUAL
# ============================================================
st.markdown("<br><br><hr style='border: 1px solid #eaeaea'><br>", unsafe_allow_html=True)

# ============================================================
# 🧾 DISTRIBUIÇÃO DO VALOR NOMINAL POR TIPO DE ESPÉCIE
# ============================================================
st.subheader("🧾 Distribuição do Valor Nominal por Tipo de Espécie")

df_especie = df.dropna(subset=["tipo_especie"])
especie_agg = (
    df_especie.groupby("tipo_especie", as_index=False)["vlr_nominal"]
    .sum()
    .sort_values("vlr_nominal", ascending=False)
)

fig_especie = px.bar(
    especie_agg,
    x="vlr_nominal",
    y="tipo_especie",
    orientation="h",
    text_auto=".2s",
    title="Valor Total Emitido por Tipo de Espécie",
    color_discrete_sequence=["#3f796c"]
)

fig_especie.update_traces(
    hovertemplate="<b>Espécie:</b> %{y}<br><b>Valor:</b> R$ %{x:,.2f}<extra></extra>",
    textposition="outside"
)
fig_especie.update_layout(
    title_x=0.5,
    xaxis_title="Valor Nominal (R$)",
    yaxis_title="Tipo de Espécie",
    title_font=dict(color="#3f796c", size=18),
    font=dict(color="#002873", size=13),
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=100, r=40, t=80, b=40)
)
st.plotly_chart(fig_especie, use_container_width=True, key="grafico_especie")

# ============================================================
# 🔸 ESPAÇAMENTO VISUAL
# ============================================================
st.markdown("<br><br><hr style='border: 1px solid #eaeaea'><br>", unsafe_allow_html=True)

# ============================================================
# 🏦 CONCENTRAÇÃO DE EMISSÕES — TOP 10 PAGADORES
# ============================================================
st.subheader("🏦 Concentração de Emissões — Top 10 Pagadores")

col_pagador = "id_pagador"

tabela_pagadores = (
    df.groupby(col_pagador, as_index=False)["vlr_nominal"]
      .sum()
      .sort_values("vlr_nominal", ascending=False)
)

tabela_pagadores["pct_carteira"] = (
    tabela_pagadores["vlr_nominal"] / tabela_pagadores["vlr_nominal"].sum() * 100
)
tabela_pagadores["pct_acumulado"] = tabela_pagadores["pct_carteira"].cumsum()

tabela_top10 = tabela_pagadores.head(10).copy()
tabela_top10["rank"] = range(1, len(tabela_top10) + 1)

tabela_top10["Valor Emitido (R$)"] = tabela_top10["vlr_nominal"].apply(lambda x: f"R$ {x:,.2f}")
tabela_top10["% Carteira"] = tabela_top10["pct_carteira"].apply(lambda x: f"{x:.1f}%")
tabela_top10["% Acumulado"] = tabela_top10["pct_acumulado"].apply(lambda x: f"{x:.1f}%")

tabela_final = tabela_top10[["rank", col_pagador, "Valor Emitido (R$)", "% Carteira", "% Acumulado"]]
tabela_final = tabela_final.rename(columns={"rank": "Rank", col_pagador: "ID Pagador"})

st.markdown("""
<style>
table {
    font-size: 0.95rem !important;
}
thead tr th {
    background-color: #3f796c !important;
    color: white !important;
    text-align: center !important;
    font-weight: 600 !important;
}
tbody tr:nth-child(even) {
    background-color: #f2f6f5 !important;
}
tbody tr:hover {
    background-color: #e6efed !important;
}
</style>
""", unsafe_allow_html=True)

st.dataframe(tabela_final, use_container_width=True, hide_index=True)

total_top10 = tabela_top10["vlr_nominal"].sum()
pct_top10 = tabela_top10["pct_carteira"].sum()

st.markdown(f"""
<div class='intro-box'>
💡 Os **10 principais pagadores** concentram **R$ {total_top10:,.2f}**, 
equivalente a **{pct_top10:.1f}%** de todo o valor emitido na carteira.
</div>
""", unsafe_allow_html=True)

# ============================================================
# 🔸 ESPAÇAMENTO VISUAL
# ============================================================
st.markdown("<br><br><hr style='border: 1px solid #eaeaea'><br>", unsafe_allow_html=True)

# ============================================================
# ⚠️ MAIORES INADIMPLENTES — TOP 10 PAGADORES
# ============================================================
st.subheader("⚠️ Maiores Inadimplentes — Top 10 Pagadores")

# Filtra apenas os boletos inadimplentes
df_inadimplentes = df[df["inadimplente"] == 1].copy()

col_pagador = "id_pagador"

# Agrupa por pagador e calcula as métricas
tabela_inadimplentes = (
    df_inadimplentes.groupby(col_pagador, as_index=False)
      .agg(qtd_boletos=("inadimplente", "count"),
           valor_devido=("vlr_nominal", "sum"))
      .sort_values("valor_devido", ascending=False)
)

# Percentual sobre o total devido
total_devido = tabela_inadimplentes["valor_devido"].sum()
tabela_inadimplentes["pct_total"] = (
    tabela_inadimplentes["valor_devido"] / total_devido * 100
)

# Seleciona Top 10
tabela_inad_top10 = tabela_inadimplentes.head(10).copy()
tabela_inad_top10["rank"] = range(1, len(tabela_inad_top10) + 1)

# Formata valores
tabela_inad_top10["Valor Devido (R$)"] = tabela_inad_top10["valor_devido"].apply(lambda x: f"R$ {x:,.2f}")
tabela_inad_top10["% Total Devido"] = tabela_inad_top10["pct_total"].apply(lambda x: f"{x:.1f}%")

# Reorganiza colunas
tabela_final_inad = tabela_inad_top10[
    ["rank", col_pagador, "qtd_boletos", "Valor Devido (R$)", "% Total Devido"]
].rename(columns={
    "rank": "Rank",
    col_pagador: "ID Pagador",
    "qtd_boletos": "Qtd. Boletos em Aberto"
})

# Estiliza a tabela
st.markdown("""
<style>
table {
    font-size: 0.95rem !important;
}
thead tr th {
    background-color: #b33a3a !important;  /* vermelho suave */
    color: white !important;
    text-align: center !important;
    font-weight: 600 !important;
}
tbody tr:nth-child(even) {
    background-color: #f9f2f2 !important;
}
tbody tr:hover {
    background-color: #f1dddd !important;
}
</style>
""", unsafe_allow_html=True)

# Exibe a tabela
st.dataframe(tabela_final_inad, use_container_width=True, hide_index=True)

# Comentário explicativo
total_top10_inad = tabela_inad_top10["valor_devido"].sum()
pct_top10_inad = tabela_inad_top10["pct_total"].sum()

st.markdown(f"""
<div class='intro-box'>
🚨 Os **10 principais inadimplentes** somam **R$ {total_top10_inad:,.2f}**, 
equivalente a **{pct_top10_inad:.1f}%** de todo o valor em aberto da carteira.
</div>
""", unsafe_allow_html=True)

# ============================================================
# 🔸 ESPAÇAMENTO VISUAL
# ============================================================
st.markdown("<br><br><hr style='border: 1px solid #eaeaea'><br>", unsafe_allow_html=True)

# ============================================================
# ⏰ ANÁLISE DE ATRASOS E MULTAS
# ============================================================
st.subheader("⏰ Análise de Atrasos e Multas")

# Garante que as colunas de data estão no formato correto
df["dt_pagamento"] = pd.to_datetime(df["dt_pagamento"], errors="coerce")
df["dt_vencimento"] = pd.to_datetime(df["dt_vencimento"], errors="coerce")

# Filtra apenas boletos pagos com atraso
df_atraso_pagamento = df.loc[
    (df["dt_pagamento"] > df["dt_vencimento"]) & (df["vlr_baixa"].notna())
].copy()

# Calcula dias de atraso e valor de multa
df_atraso_pagamento["dias_atraso"] = (df_atraso_pagamento["dt_pagamento"] - df_atraso_pagamento["dt_vencimento"]).dt.days
df_atraso_pagamento["valor_multa"] = df_atraso_pagamento["vlr_nominal"] - df_atraso_pagamento["vlr_baixa"]

# ============================================================
# 📊 INDICADORES DE DESEMPENHO
# ============================================================
media_atraso = df_atraso_pagamento["dias_atraso"].mean()
mediana_atraso = df_atraso_pagamento["dias_atraso"].median()
max_atraso = df_atraso_pagamento["dias_atraso"].max()
valor_total_multas = -1 * (df_atraso_pagamento["valor_multa"].sum())

st.markdown(f"""
<div class="kpi-container">
    <div class="kpi-card">
        <div class="kpi-value">{media_atraso:.1f} dias</div>
        <div class="kpi-label">Atraso Médio</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">{mediana_atraso} dias</div>
        <div class="kpi-label">Mediana de Atraso</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">{max_atraso} dias</div>
        <div class="kpi-label">Maior Atraso</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-value">R$ {valor_total_multas:,.2f}</div>
        <div class="kpi-label">Valor Arrecadado em Multas</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 📈 DISTRIBUIÇÃO DOS DIAS DE ATRASO
# ============================================================
st.markdown("<br>", unsafe_allow_html=True)
st.write("📊 **Distribuição de Boletos por Dias de Atraso**")

fig_hist = px.histogram(
    df_atraso_pagamento,
    x="dias_atraso",
    nbins=40,
    title="Distribuição dos Dias de Atraso no Pagamento",
    color_discrete_sequence=["#3f796c"]
)
fig_hist.update_traces(hovertemplate="<b>Dias de Atraso:</b> %{x}<br><b>Qtd Boletos:</b> %{y}<extra></extra>")
fig_hist.update_layout(
    title_x=0.5,
    xaxis_title="Dias de Atraso",
    yaxis_title="Quantidade de Boletos",
    title_font=dict(color="#3f796c", size=18),
    font=dict(color="#002873", size=13),
    plot_bgcolor="white",
    paper_bgcolor="white"
)
st.plotly_chart(fig_hist, use_container_width=True, key="grafico_distribuicao_atraso")

# ============================================================
# 📝 AVISO SOBRE O INTERVALO DOS BINS
# ============================================================
st.markdown("""
<div class='intro-box'>
ℹ️ **Observação:** Os intervalos do histograma estão definidos automaticamente (aproximadamente de 9 em 9 dias).  
Isso significa que cada barra representa a quantidade de boletos com atraso dentro de uma faixa de ~9 dias.
</div>
""", unsafe_allow_html=True)