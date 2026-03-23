import sqlite3
import pandas as pd
from pathlib import Path

# Define o caminho do banco de dados na raiz
DB_PATH = Path(__file__).resolve().parent.parent / "marketing_api_platform.db"

def save_to_database(df: pd.DataFrame, table_name: str = "raw_campaign_data"):
    """Salva o DataFrame no banco de dados SQLite."""
    if df.empty:
        print("⚠️ DataFrame vazio. Nada para salvar.")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        print(f"✅ Dados salvos com sucesso na tabela '{table_name}'")
    except Exception as e:
        print(f"❌ Erro ao salvar no banco: {e}")