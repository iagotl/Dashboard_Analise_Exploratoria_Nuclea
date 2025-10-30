# 💰 Dashboard de Análise Exploratória - FIDC Boletos

Dashboard interativo desenvolvido em Streamlit para análise exploratória de boletos em Fundos de Investimento em Direitos Creditórios (FIDC's), desenvolvido em parceria com a **Núclea**.

## 📋 Sobre o Projeto

Este dashboard permite explorar dados financeiros de boletos cedidos ao fundo, avaliando **pagamentos, atrasos, séries temporais e métricas de inadimplência**. A aplicação foi desenvolvida para fornecer insights visuais e análises estatísticas sobre o comportamento da carteira de crédito.

## 🎯 Funcionalidades

### 1. 📘 Dicionário de Dados
- Documentação completa das bases de dados utilizadas
- Base de Boletos (principal)
- Base Auxiliar (liquidez e materialidade)
- Visualização das estruturas de dados

### 2. 📆 Análises Temporais
- Contagem de boletos por ano/mês de emissão
- Valor nominal emitido ao longo do tempo
- Distribuição de boletos por dia de vencimento
- Análise de pagamentos mensais com curva acumulada
- Visualização de padrões temporais e picos atípicos

### 3. 📈 Análises Financeiras
- **KPIs Principais:**
  - Valor total emitido
  - Valor total de baixas
  - Valor inadimplente
  - Mediana, máximo e mínimo do valor nominal
  - Percentual de boletos pagos

- **Distribuições:**
  - Por tipo de baixa
  - Por tipo de espécie
  - Concentração por pagadores (Top 10)

- **Análise de Risco:**
  - Maiores inadimplentes (Top 10)
  - Análise de atrasos e multas
  - Distribuição de dias de atraso

### 4. 📚 Conclusões
- Síntese dos principais achados da análise exploratória
- Indicadores relevantes para o dashboard final
- Insights sobre padrões de comportamento da carteira

## 🛠️ Tecnologias Utilizadas

- **Streamlit** 1.39.0 - Framework para criação do dashboard interativo
- **Pandas** 2.2.2 - Manipulação e análise de dados
- **NumPy** 1.26.4 - Operações numéricas
- **Plotly** 5.24.1 - Visualizações interativas
- **Statsmodels** 0.14.2 - Análises estatísticas
- **Pillow** 10.4.0 - Manipulação de imagens
- **Openpyxl** 3.1.5 - Suporte para arquivos Excel

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip ou conda

### Passos para Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/Dashboard_Analise_Exploratoria_Nuclea.git
cd Dashboard_Analise_Exploratoria_Nuclea
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

Execute o seguinte comando na raiz do projeto:

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no navegador padrão em `http://localhost:8501`.

## 📁 Estrutura do Projeto

```
Dashboard_Analise_Exploratoria_Nuclea/
├── app.py                      # Aplicação principal Streamlit
├── requirements.txt            # Dependências do projeto
├── README.md                   # Documentação do projeto
├── data/
│   └── base_tratada_nuclea.csv # Base de dados tratada
├── pages/
│   ├── 1_Dicionário.py        # Página do dicionário de dados
│   ├── 2_Análises_Temporais.py # Página de análises temporais
│   ├── 3_Análises_Financeiras.py # Página de análises financeiras
│   └── 4_Conclusões.py         # Página de conclusões
├── assets/
│   ├── base_auxiliar.PNG       # Imagem do dicionário da base auxiliar
│   ├── base_boletos.PNG        # Imagem do dicionário da base de boletos
│   ├── logo_empresa.png        # Logo da empresa
│   └── NOME_RAIZ.png          # Logo/identidade visual
└── styles/
    └── style.css              # Estilos customizados do dashboard
```

**⚠️ Nota:** Os dados utilizados são sensíveis e não devem ser compartilhados publicamente.

## 👥 Desenvolvimento

Dashboard desenvolvido para análise exploratória de dados financeiros de FIDC's, com foco em boletos e análise de risco creditício.

---

