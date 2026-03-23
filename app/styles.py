import streamlit as st

def apply_custom_styles():
    """Aplica identidade visual de Dashboard Corporativo High-Ticket."""
    st.markdown("""
        <style>
        /* Fundo principal */
        .main { background-color: #0e1117; }
        
        /* Customização de Métricas */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            color: #00d4ff;
            font-weight: 700;
        }
        
        /* Cartões customizados via markdown */
        .growth-card {
            background-color: #1e2130;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #00d4ff;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)