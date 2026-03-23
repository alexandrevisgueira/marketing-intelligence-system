# 📊 Marketing Performance Intelligence (MPI)

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/ui-streamlit-ff4b4b.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Sistema Inteligente de Atribuição e Otimização de Capital para Marketing de Performance.**

---

## 🎯 Visão Estratégica
Diferente de dashboards comuns que focam em métricas de vaidade (likes, cliques), o **MPI** foi desenhado para **Arquitetos de Growth**. Ele foca na **Eficiência do Capital**, identificando onde cada real investido gera o maior retorno marginal.

## 🧠 Arquitetura do Sistema
O projeto segue o modelo **ETL (Extract, Transform, Load)** modularizado:
1. **Extraction:** Coleta de dados via APIs (Google/Meta Ads) ou Mock Data para desenvolvimento.
2. **Transformation:** Motor de cálculo de KPIs (CAC, LTV, ROI, ROAS) com sanitização de dados.
3. **Loading:** Armazenamento em Data Warehouse (SQLite para Local / BigQuery para Cloud).
4. **Visualization:** Interface reativa em Streamlit com diagnóstico prescritivo.



## 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.10+
- **Processamento:** Pandas / NumPy
- **Interface:** Streamlit (UI/UX de Alta Conversão)
- **Banco de Dados:** SQLite (Dev) / Google BigQuery (Prod)
- **Segurança:** Protocolo de isolamento de credenciais via `.env`

## 🔒 Protocolo de Segurança (DevSecOps)
Este repositório aplica práticas rigorosas de segurança:
- **Zero Trust:** Nenhuma credencial é armazenada no código (Hardcoded).
- **Environment Isolation:** Arquivos sensíveis protegidos via `.gitignore`.
- **Input Validation:** Tratamento de `ZeroDivisionError` e dados corrompidos.

## 🚀 Como Executar
1. Clone o repositório: `git clone ...`
2. Crie o ambiente virtual: `python -m venv venv`
3. Ative a venv: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Win)
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure o seu arquivo `.env` baseado no `.env.example`
6. Execute o app: `streamlit run app/dashboard.py`

---
*Desenvolvido para operações de Marketing High Ticket.*