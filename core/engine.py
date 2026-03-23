import pandas as pd
import sqlite3
from pathlib import Path

# Versão universal para Local (Windows) e Cloud (Linux)
DB_PATH = Path.cwd() / "marketing_api_platform.db"

class MarketingEngine:
    """Motor de Inteligência para análise de ROI e Otimização de Budget."""

    def __init__(self):
        self.ticket_medio = 50.0  # Pode ser movido para o .env futuramente

    def get_raw_data(self):
        """Lê os dados brutos do SQLite para processamento."""
        try:
            conn = sqlite3.connect(DB_PATH)
            df = pd.read_sql("SELECT * FROM raw_campaign_data", conn)
            conn.close()
            return df
        except Exception as e:
            print(f"❌ Erro ao ler banco de dados: {e}")
            return pd.DataFrame()

    def process_metrics(self, df: pd.DataFrame):
        """Aplica as fórmulas de Business Intelligence nos dados brutos."""
        if df.empty:
            return df

        # Cálculos de Performance
        df["CTR"] = (df["clicks"] / df["impressions"])
        df["CPA"] = (df["cost"] / df["conversions"])
        
        # Cálculo de Receita e ROI
        df["revenue"] = df["conversions"] * self.ticket_medio
        df["ROI"] = (df["revenue"] / df["cost"])
        
        # Inteligência Avançada: Payback (Meses para recuperar o custo da campanha)
        # Consideramos aqui uma métrica hipotética de margem sobre o faturamento
        df["payback_months"] = (df["cost"] / (df["revenue"] / 12)).round(1)

        return df

    def generate_recommendations(self, df: pd.DataFrame):
        """Lógica Prescritiva: O que o gestor deve fazer?"""
        avg_roi = df["ROI"].mean()
        
        # Identifica a melhor e a pior campanha para o Dashboard
        best = df.loc[df["ROI"].idxmax()]
        worst = df.loc[df["ROI"].idxmin()]
        
        return {
            "best_campaign": best,
            "worst_campaign": worst,
            "potential_gain_pct": ((best["ROI"] / worst["ROI"]) - 1) * 100
        }