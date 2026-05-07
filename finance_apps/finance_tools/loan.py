# finance_tools/loan.py

def calculate_emi(principal: float, annual_rate: float, months: int) -> float:
    """Return monthly EMI for a loan.
    principal   : loan amount (₹)
    annual_rate : annual interest rate (%)
    months      : loan tenure in months
    """
    if annual_rate == 0:
        return principal / months
    r = (annual_rate / 100) / 12          # monthly rate
    emi = principal * r * (1 + r) ** months / ((1 + r) ** months - 1)
    return round(emi, 2)
