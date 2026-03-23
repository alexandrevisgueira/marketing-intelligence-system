def format_currency_brl(value: float) -> str:
    """Formata valores para o padrão de moeda brasileiro R$."""
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def format_percent(value: float) -> str:
    """Formata valores decimais para percentual (0.05 -> 5.00%)."""
    return f"{value:.2%}"