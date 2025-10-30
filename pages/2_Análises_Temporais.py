import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# --- Importar CSS ---
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Título principal ---
st.markdown("<h1 style='text-align: center; color: #3f796c;'>📆 Análises Temporais</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='intro-box'>
Esta seção traz uma análise temporal da base de boletos, explorando as emissões, vencimentos e pagamentos ao longo do tempo.
A partir dessas informações, é possível entender a evolução das operações, identificar períodos com volume atípico de emissões 
e observar padrões de comportamento no fluxo de pagamento.
</div>
""", unsafe_allow_html=True)

# ============================================================
# 🔹 Carrega a base (apenas uma vez)
# ============================================================
df = pd.read_csv("data/base_tratada_nuclea.csv", low_memory=False)
df["dt_emissao"] = pd.to_datetime(df["dt_emissao"], errors="coerce")
df = df.dropna(subset=["dt_emissao"])
df["ano_mes_emissao"] = df["dt_emissao"].dt.to_period("M").astype(str)

# ============================================================
# 📊 CONTAGEM DE BOLETOS POR ANO/MÊS
# ============================================================
st.subheader("📊 Contagem de Boletos por Ano/Mês de Emissão")

contagem_emissao = (
    df.groupby("ano_mes_emissao", as_index=False)
      .size()
      .rename(columns={"size": "qtd_boletos"})
      .sort_values("ano_mes_emissao")
)

fig_contagem = px.bar(
    contagem_emissao,
    x="ano_mes_emissao",
    y="qtd_boletos",
    text="qtd_boletos",
    title="Contagem de Boletos por Ano/Mês de Emissão",
    color_discrete_sequence=["#3f796c"]
)

fig_contagem.update_traces(
    hovertemplate="<b>Período:</b> %{x}<br><b>Boletos:</b> %{y}<extra></extra>",
    textposition="outside"
)

fig_contagem.update_layout(
    title_x=0.5,
    xaxis_title="Ano/Mês de Emissão",
    yaxis_title="Quantidade de Boletos",
    title_font=dict(color="#3f796c", size=18),
    font=dict(color="#002873", size=13),
    plot_bgcolor="white",
    paper_bgcolor="white",
    hoverlabel=dict(bgcolor="white", font_size=13, font_color="#002873"),
    margin=dict(l=40, r=40, t=80, b=40)
)

st.plotly_chart(fig_contagem, use_container_width=True)

# ============================================================
# 💵 VALOR NOMINAL TOTAL POR ANO/MÊS
# ============================================================
st.subheader("💵 Valor Nominal Emitido por Ano/Mês de Emissão")

valor_emissao = (
    df.dropna(subset=["vlr_nominal"])
      .groupby("ano_mes_emissao", as_index=False)["vlr_nominal"]
      .sum()
      .sort_values("ano_mes_emissao")
)

fig_valor = px.bar(
    valor_emissao,
    x="ano_mes_emissao",
    y="vlr_nominal",
    text_auto=".2s",
    title="Valor Nominal Total Emitido por Ano/Mês de Emissão",
    color_discrete_sequence=["#3f796c"]
)

fig_valor.update_traces(
    hovertemplate="<b>Período:</b> %{x}<br><b>Valor Emitido:</b> R$ %{y:,.2f}<extra></extra>",
    textposition="outside"
)

fig_valor.update_layout(
    title_x=0.5,
    xaxis_title="Ano/Mês de Emissão",
    yaxis_title="Valor Nominal Emitido (R$)",
    title_font=dict(color="#3f796c", size=18),
    font=dict(color="#002873", size=13),
    plot_bgcolor="white",
    paper_bgcolor="white",
    hoverlabel=dict(bgcolor="white", font_size=13, font_color="#002873"),
    margin=dict(l=40, r=40, t=80, b=40)
)

st.plotly_chart(fig_valor, use_container_width=True)

# ============================================================
# ⏰ QUANTIDADE DE BOLETOS POR DIA DE VENCIMENTO (GRÁFICO DE LINHA)
# ============================================================
st.subheader("⏰ Quantidade de Boletos por Dia de Vencimento")

# 3️⃣ Agrupa por dia de vencimento
contagem_vencimento = (
    df.groupby("dt_vencimento", as_index=False)
      .size()
      .rename(columns={"size": "qtd_boletos"})
      .sort_values("dt_vencimento")
)

# 4️⃣ Cria o gráfico interativo de linha
fig_venc = px.line(
    contagem_vencimento,
    x="dt_vencimento",
    y="qtd_boletos",
    title="Quantidade de Boletos por Dia de Vencimento",
    markers=True,  # adiciona marcadores nos pontos
)

# 5️⃣ Ajusta o estilo visual
fig_venc.update_traces(
    line=dict(color="#3f796c", width=3),
    marker=dict(size=6, color="#002873"),
    showlegend=True, 
    hovertemplate="<b>Data de Vencimento:</b> %{x|%d/%m/%Y}<br><b>Boletos:</b> %{y}<extra></extra>",
)

fig_venc.update_layout(
    title_x=0.5,
    xaxis_title="Data de Vencimento",
    yaxis_title="Quantidade de Boletos",
    title_font=dict(color="#3f796c", size=18),
    font=dict(color="#002873", size=13),
    plot_bgcolor="white",
    paper_bgcolor="white",
    hoverlabel=dict(bgcolor="white", font_size=13, font_color="#002873"),
    margin=dict(l=40, r=40, t=80, b=40),
    xaxis=dict(showgrid=True, gridcolor="rgba(0,0,0,0.05)"),
    yaxis=dict(showgrid=True, gridcolor="rgba(0,0,0,0.05)"),
)

# 6️⃣ Exibe o gráfico no dashboard
st.plotly_chart(fig_venc, use_container_width=True)


# ============================================================
# 💳 QUANTIDADE DE BOLETOS PAGOS POR MÊS + CURVA ACUMULADA
# ============================================================
st.subheader("💳 Quantidade de Boletos Pagos por Mês")

# 1️⃣ Garantir formato datetime
df["dt_pagamento"] = pd.to_datetime(df["dt_pagamento"], errors="coerce")

# 2️⃣ Filtrar apenas registros com pagamento
df_pag = df.dropna(subset=["dt_pagamento"]).copy()

# 3️⃣ Criar coluna de Ano/Mês de pagamento
df_pag["ano_mes_pagamento"] = df_pag["dt_pagamento"].dt.to_period("M").astype(str)

# 4️⃣ Agrupar por mês e calcular total e acumulado
pag_mes = (
    df_pag.groupby("ano_mes_pagamento", as_index=False)
          .agg(qtd_boletos=("dt_pagamento", "count"))
          .sort_values("ano_mes_pagamento")
)
pag_mes["pct_acumulado"] = (pag_mes["qtd_boletos"].cumsum() / pag_mes["qtd_boletos"].sum()) * 100

# 5️⃣ Gráfico combinado (barras + linha acumulada)
import plotly.graph_objects as go

fig_pagamentos = go.Figure()

# Barras — quantidade de boletos pagos por mês
fig_pagamentos.add_trace(
    go.Bar(
        x=pag_mes["ano_mes_pagamento"],
        y=pag_mes["qtd_boletos"],
        name="Boletos Pagos (Qtd)",
        marker_color="#3f796c",
        hovertemplate="<b>Mês:</b> %{x}<br><b>Pagamentos:</b> %{y}<extra></extra>"
    )
)

# Linha — porcentagem acumulada
fig_pagamentos.add_trace(
    go.Scatter(
        x=pag_mes["ano_mes_pagamento"],
        y=pag_mes["pct_acumulado"],
        name="Percentual Acumulado (%)",
        mode="lines+markers",
        line=dict(color="#002873", width=3),
        marker=dict(size=6),
        yaxis="y2",
        hovertemplate="<b>Mês:</b> %{x}<br><b>Acumulado:</b> %{y:.1f}%<extra></extra>"
    )
)

# Layout com eixo duplo
fig_pagamentos.update_layout(
    title="Pagamentos Mensais e Percentual Acumulado",
    title_x=0.5,
    xaxis=dict(title="Ano/Mês de Pagamento"),
    yaxis=dict(title="Quantidade de Boletos Pagos"),
    yaxis2=dict(
        title="Percentual Acumulado (%)",
        overlaying="y",
        side="right",
        showgrid=False
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.25,
        xanchor="center",
        x=0.5
    ),
    title_font=dict(color="#3f796c", size=18),
    font=dict(color="#002873", size=13),
    plot_bgcolor="white",
    paper_bgcolor="white",
    hoverlabel=dict(bgcolor="white", font_size=13, font_color="#002873"),
    margin=dict(l=60, r=60, t=80, b=60)
)

st.plotly_chart(fig_pagamentos, use_container_width=True, key="grafico_pagamentos_mes")


# ============================================================
# 📊 TABELA DE APOIO (EXPANSÍVEL)
# ============================================================
with st.expander("📅 Ver Totais de Pagamento por Dia", expanded=False):
    st.markdown("""
    Esta tabela detalha o total de boletos pagos por dia, permitindo análise granular de picos de pagamento.
    """)
    
    contagem_pagamento_dia = (
        df_pag.groupby("dt_pagamento", as_index=False)
              .agg(qtd_boletos=("dt_pagamento", "count"))
              .sort_values("dt_pagamento", ascending=False)
    )

    contagem_pagamento_dia["Data de Pagamento"] = contagem_pagamento_dia["dt_pagamento"].dt.strftime("%d/%m/%Y")
    contagem_pagamento_dia = contagem_pagamento_dia.rename(columns={"qtd_boletos": "Quantidade de Boletos Pagos"})
    contagem_pagamento_dia = contagem_pagamento_dia[["Data de Pagamento", "Quantidade de Boletos Pagos"]]

    st.dataframe(
        contagem_pagamento_dia,
        use_container_width=True,
        hide_index=True
    )