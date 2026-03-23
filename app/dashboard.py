import sys
import os
from pathlib import Path
import streamlit as st
import pandas as pd

# 1. Configuração de Path Absoluto
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
    # 3. Setup de UI Premium
    st.set_page_config(page_title="Marketing Intelligence Pro", layout="wide")
    apply_custom_styles()

    st.title("🚀 Sistema de Inteligência de Marketing")
    st.caption("Arquitetura de Atribuição Blindada e Otimização de Capital")
    st.markdown("---")

    engine = MarketingEngine()

    # 4. Sidebar de Controle
    st.sidebar.header("⚙️ Painel de Controle")
    if st.sidebar.button("🔄 Sincronizar Dados da API"):
        with st.spinner("Conectando à API Segura..."):
            raw_df = extract_marketing_data()
            if not raw_df.empty:
                save_to_database(raw_df)
                st.sidebar.success("Dados Atualizados!")
                st.rerun()
            else:
                st.sidebar.error("Erro de Autenticação nos Secrets.")

    # 5. Fluxo de Dados (Fallback Memory/DB)
    df_raw = engine.get_raw_data()
    if df_raw.empty:
        df_raw = extract_marketing_data()

    if df_raw.empty:
        st.warning("⚠️ Aguardando conexão com a API de Marketing.")
        st.stop()

    # 6. Processamento de Core Business
    df_processed = engine.process_metrics(df_raw)

    # 7. Layout de KPIs (Executive Summary)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Receita Total", format_currency_brl(df_processed["revenue"].sum()))
    with col2:
        st.metric("Investimento", format_currency_brl(df_processed["cost"].sum()))
    with col3:
        st.metric("ROI Médio", f"{df_processed['ROI'].mean():.2f}x", delta="Market Leader")
    with col4:
        st.metric("Payback Médio", f"{df_processed['payback_months'].mean():.1f} meses")

    st.markdown("---")

    # 8. Gráficos e Insights
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        st.subheader("🧠 Insights de Growth")
        rec = engine.generate_recommendations(df_processed)
        st.success(f"**Escalar:** {rec['best_campaign']['campaign']}")
        st.error(f"**Revisar:** {rec['worst_campaign']['campaign']}")
        st.info(f"**Otimização:** +{rec['potential_gain_pct']:.1f}% de eficiência marginal.")
        
        # Botão de Exportação para Relatório
        csv = df_processed.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📄 Exportar Relatório para Cliente (CSV)",
            data=csv,
            file_name='relatorio_performance_growth.csv',
            mime='text/csv',
        )

    with col_right:
        st.subheader("📊 Performance por Campanha (ROI)")
        st.bar_chart(df_processed.set_index("campaign")["ROI"])

    # 9. Tabela de Dados Brutos com Formatação de Elite
    st.subheader("📋 Auditoria de Dados Brutos")
    
    # Criamos uma cópia apenas para exibição visual
    df_display = df_processed.copy()
    
    # Formatação das colunas para o usuário final
    format_mapping = {
        "cost": "R$ {:,.2f}",
        "revenue": "R$ {:,.2f}",
        "CPA": "R$ {:,.2f}",
        "CTR": "{:.2%}",
        "ROI": "{:.2f}x",
        "payback_months": "{:.1f} meses"
    }
    
    st.dataframe(
        df_display.style.format(format_mapping),
        use_container_width=True,
        hide_index=True
    )

if __name__ == "__main__":
    main()