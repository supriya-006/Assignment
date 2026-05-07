# finance_tools/tax.py

def calculate_tax(income: float, tax_rate: float) -> float:
    """Return tax amount for given income and rate (%)."""
    return income * (tax_rate / 100)
