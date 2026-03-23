import sys
from pathlib import Path
import streamlit as st

# 1. Configuração de Path (Garante que o Python encontre 'core', 'data' e 'utils')
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.append(str(root_path))

# 2. Imports Modulares (Clean Architecture)
from core.engine import MarketingEngine
from app.styles import apply_custom_styles
from utils.formatters import format_currency_brl, format_percent
from data.extract import extract_marketing_data
from data.loader import save_to_database

def main():
    # 3. Setup de UI e Design
    st.set_page_config(page_title="Marketing Intelligence System", layout="wide")
    apply_custom_styles()

    st.title("🚀 Marketing Intelligence System")
    st.markdown("---")

    # 4. Inicialização do Motor
    engine = MarketingEngine()

# Botão de Atualização (Simula o Pipeline ETL)
    if st.sidebar.button("🔄 Sincronizar Dados da API"):
        with st.spinner("Extraindo e Carregando dados..."):
            raw_data = extract_marketing_data()
            save_to_database(raw_data)
            st.sidebar.success("Dados Sincronizados!")
            st.rerun()  # <--- ADICIONE ESTA LINHA AQUI

    # 5. Processamento de Dados
    df_raw = engine.get_raw_data()

    if df_raw.empty:
        st.warning("⚠️ O banco de dados está vazio. Clique em 'Sincronizar Dados' na barra lateral.")
        st.stop()

    df_processed = engine.process_metrics(df_raw)
    
    # Filtro de Campanhas
    st.sidebar.subheader("🎯 Filtros")
    selected_campaigns = st.sidebar.multiselect(
        "Selecione Campanhas:",
        options=df_processed["campaign"].unique(),
        default=df_processed["campaign"].unique()
    )
    df_filtered = df_processed[df_processed["campaign"].isin(selected_campaigns)]

    # 6. Visão Geral Executiva (KPIs)
    col1, col2, col3, col4 = st.columns(4)
    
    total_revenue = df_filtered["revenue"].sum()
    total_cost = df_filtered["cost"].sum()
    avg_roi = df_filtered["ROI"].mean()
    avg_payback = df_filtered["payback_months"].mean()

    col1.metric("Receita Total", format_currency_brl(total_revenue))
    col2.metric("Investimento", format_currency_brl(total_cost))
    col3.metric("ROI Médio", f"{avg_roi:.2f}x")
    col4.metric("Payback Médio", f"{avg_payback:.1f} meses")

    st.markdown("---")

    # 7. Diagnóstico Prescritivo (A Cérebro do Sistema)
    st.subheader("🧠 Recomendações de Growth")
    
    if len(df_filtered) > 1:
        insights = engine.generate_recommendations(df_filtered)
        best = insights["best_campaign"]
        worst = insights["worst_campaign"]

        col_left, col_right = st.columns(2)
        
        with col_left:
            st.info(f"💰 **Ação:** Escalar `{best['campaign']}` e cortar verba de `{worst['campaign']}`.")
            st.success(f"📈 **Ganho Potencial:** +{insights['potential_gain_pct']:.1f}% de eficiência marginal.")
        
        with col_right:
            st.error(f"💸 **Alerta de Risco:** `{worst['campaign']}` apresenta ROI crítico de {worst['ROI']:.2f}x.")
            st.warning(f"⏳ **Payback:** O investimento em `{worst['campaign']}` leva {worst['payback_months']} meses para retornar.")

    # 8. Visualização de Dados
    st.subheader("📊 Performance por Campanha (ROI)")
    st.bar_chart(df_filtered.set_index("campaign")["ROI"])

    st.subheader("📋 Detalhamento Técnico")
    st.dataframe(df_filtered, use_container_width=True, hide_index=True)

if __name__ == "__main__":
    main()