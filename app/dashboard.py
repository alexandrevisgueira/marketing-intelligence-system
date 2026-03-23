import sys
import os
from pathlib import Path
import streamlit as st
import pandas as pd

# 1. Configuração de Path Absoluto para Nuvem (Linux/Windows)
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

# 2. Imports Modulares
from core.engine import MarketingEngine
from app.styles import apply_custom_styles
from utils.formatters import format_currency_brl
from data.extract import extract_marketing_data
from data.loader import save_to_database

def main():
    # 3. Setup de UI
    st.set_page_config(page_title="Marketing Intelligence", layout="wide")
    apply_custom_styles()

    st.title("🚀 Sistema de Inteligência de Marketing")
    st.markdown("---")

    engine = MarketingEngine()

    # 4. Sidebar e Lógica de Sincronização
    st.sidebar.header("Painel de Controle")
    
    if st.sidebar.button("🔄 Sincronizar Dados da API"):
        with st.spinner("Conectando à API..."):
            raw_df = extract_marketing_data()
            if not raw_df.empty:
                save_to_database(raw_df)
                st.sidebar.success("Dados Sincronizados!")
                st.rerun()
            else:
                st.sidebar.error("Erro: Chave de API não encontrada nos Secrets.")

    # 5. Tentativa de Carregamento (Banco ou Memória)
    df_raw = engine.get_raw_data()

    # Se o banco estiver vazio, tentamos carregar direto da extração para o teste real
    if df_raw.empty:
        st.info("💡 O banco de dados está vazio. Tentando carregar dados em tempo real para o teste...")
        df_raw = extract_marketing_data()

    if df_raw.empty:
        st.warning("⚠️ Sem dados disponíveis. Verifique o arquivo .env ou os Secrets do Streamlit.")
        st.stop()

    # 6. Processamento e Visualização
    df_processed = engine.process_metrics(df_raw)

    # KPIs Principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Receita Total", format_currency_brl(df_processed["revenue"].sum()))
    col2.metric("Investimento", format_currency_brl(df_processed["cost"].sum()))
    col3.metric("ROI Médio", f"{df_processed['ROI'].mean():.2f}x")
    col4.metric("Payback Médio", f"{df_processed['payback_months'].mean():.1f} meses")

    st.markdown("---")

    # Insights e Gráfico
    col_a, col_b = st.columns([1, 2])
    
    with col_a:
        st.subheader("🧠 Insights de Growth")
        rec = engine.generate_recommendations(df_processed)
        st.success(f"**Melhor Performance:** {rec['best_campaign']['campaign']}")
        st.error(f"**Alerta de Risco:** {rec['worst_campaign']['campaign']}")
        st.info(f"**Otimização:** +{rec['potential_gain_pct']:.1f}% de eficiência marginal disponível.")

    with col_b:
        st.subheader("📊 Performance por Campanha (ROI)")
        st.bar_chart(df_processed.set_index("campaign")["ROI"])

    st.subheader("📋 Tabela de Dados Brutos")
    st.dataframe(df_processed, use_container_width=True)

if __name__ == "__main__":
    main()