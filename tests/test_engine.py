import pandas as pd
import sys
from pathlib import Path

# Adiciona a raiz ao path para encontrar o core
sys.path.append(str(Path(__file__).resolve().parent.parent))
from core.engine import MarketingEngine

def test_marketing_calculations():
    engine = MarketingEngine()
    
    # Criamos um dado de teste (Mock Data)
    mock_data = pd.DataFrame({
        "campaign": ["Test"],
        "clicks": [100],
        "impressions": [1000],
        "cost": [100.00],
        "conversions": [10]
    })
    
    # Processamos
    processed = engine.process_metrics(mock_data)
    
    # Validações (Asserts)
    # Se o custo é 100 e conversões são 10, o CPA deve ser 10
    assert processed.loc[0, "CPA"] == 10.0
    
    # Se o ticket médio é 50 e conversões são 10, receita é 500. ROI = 500/100 = 5.0
    assert processed.loc[0, "ROI"] == 5.0
    
    print("✅ Testes de Cálculos de Marketing: PASSOU")

if __name__ == "__main__":
    test_marketing_calculations()