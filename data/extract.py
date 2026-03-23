import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np

# Carrega as variáveis do .env
load_dotenv()

def extract_marketing_data():
    """
    Simula a extração de dados de uma API (Google/Meta Ads).
    Em um cenário real, aqui usaríamos requests.get() com Auth Header.
    """
    api_key = os.getenv("MARKETING_API_KEY")
    
    if not api_key:
        print("🚨 ERRO: API Key não encontrada no arquivo .env")
        return pd.DataFrame()

    print(f"📡 Conectando à API com a chave: {api_key[:5]}***")

    # Simulando dados brutos vindos da API
    data = {
        "campaign": ["Google Ads - Search", "Meta Ads - Lookalike", "YouTube Ads - Awareness", "TikTok Ads - Video"],
        "clicks": [1200, 950, 2100, 1500],
        "impressions": [15000, 22000, 50000, 30000],
        "cost": [850.00, 640.00, 700.00, 900.00],
        "conversions": [96, 72, 21, 45]
    }
    
    return pd.DataFrame(data)