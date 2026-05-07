from finance_tools import calculate_tax, calculate_emi

def main():
    print("=== Finance App ===")

    # --- Tax section ---
    income   = float(input("\nEnter your income: "))
    tax_rate = float(input("Enter tax rate (%): "))
    tax      = calculate_tax(income, tax_rate)
    print(f"Tax amount : ₹{tax:,.2f}")
    print(f"Net income : ₹{income - tax:,.2f}")

    # --- EMI section ---
    principal   = float(input("\nEnter loan amount: "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    months      = int  (input("Enter tenure (months): "))
    emi = calculate_emi(principal, annual_rate, months)
    print(f"Monthly EMI: ₹{emi:,.2f}")

if __name__ == "__main__":
    main()