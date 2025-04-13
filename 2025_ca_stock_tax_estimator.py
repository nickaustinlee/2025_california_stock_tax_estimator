import argparse

def calculate_taxes(salary, stock_sales):
    """
    Calculates federal and California state income taxes for 2025 based on salary and stock sales.
    Also calculates Net Investment Income Tax (NIIT).

    Args:
      salary: Annual salary.
      stock_sales: Proceeds from stock sales (assumes long-term capital gains for simplicity).

    Returns:
      A dictionary containing the following:
        - federal_income_tax: Estimated federal income tax.
        - federal_capital_gains_tax: Estimated federal capital gains tax.
        - total_federal_tax: Total estimated federal tax.
        - ca_income_tax: Estimated California state income tax.
        - ca_capital_gains_tax: Estimated California capital gains tax.
        - total_ca_tax: Total estimated California tax.
        - total_tax: Total estimated federal and state tax.
        - niit: Net Investment Income Tax
    """

    # --- Federal Tax Brackets and Rates (2025, Single Filer) ---
    federal_brackets = [
        (0, 11925, 0.10),
        (11925, 48475, 0.12),
        (48475, 103350, 0.22),
        (103350, 197300, 0.24),
        (197300, 250525, 0.32),
        (250525, 626350, 0.35),
        (626350, float('inf'), 0.37)
    ]

    # --- Federal Long-Term Capital Gains Tax Rates (2025, Single Filer) ---
    federal_capital_gains_brackets = [
        (0, 48350, 0.00),
        (48350, 533400, 0.15),
        (533400, float('inf'), 0.20)
    ]

    # --- California State Tax Brackets and Rates (2025, Single Filer) ---
    # Note: California taxes capital gains as ordinary income.
    ca_brackets = [
        (0, 10756, 0.01),
        (10756, 25499, 0.02),
        (10756, 25499, 0.04),
        (25499, 40245, 0.06),
        (40245, 55866, 0.08),
        (55866, 70606, 0.093),
        (70606, 360659, 0.103),
        (432787, 721314, 0.113),
        (721314, float('inf'), 0.123)
    ]

    # --- Standard Deduction (2025, Single Filer) ---
    federal_standard_deduction = 15000
    ca_standard_deduction = 5592  # Estimated based on inflation adjustment

    # --- Federal Income Tax Calculation ---
    federal_taxable_income = max(0, salary - federal_standard_deduction)
    federal_income_tax = 0
    for bracket_start, bracket_end, rate in federal_brackets:
        if federal_taxable_income > bracket_start:
            taxable_amount = min(federal_taxable_income, bracket_end) - bracket_start
            federal_income_tax += taxable_amount * rate

    # --- Federal Capital Gains Tax Calculation ---
    federal_capital_gains_tax = 0
    for bracket_start, bracket_end, rate in federal_capital_gains_brackets:
        if (federal_taxable_income + stock_sales) > bracket_start:
            taxable_amount = min((federal_taxable_income + stock_sales), bracket_end) - max(
                federal_taxable_income, bracket_start)
            if taxable_amount > 0:
                federal_capital_gains_tax += taxable_amount * rate

    # --- California Income Tax Calculation ---
    ca_taxable_income = max(0, salary + stock_sales - ca_standard_deduction)
    ca_income_tax = 0
    for bracket_start, bracket_end, rate in ca_brackets:
        if ca_taxable_income > bracket_start:
            taxable_amount = min(ca_taxable_income, bracket_end) - bracket_start
            ca_income_tax += taxable_amount * rate

    # CA does not separate out capital gains taxes, it's all under income tax
    ca_capital_gains_tax = 0

    # --- NIIT Calculation ---
    niit_threshold = 200000  # Threshold for NIIT for single filers in 2025
    magi_simplified = salary + stock_sales #I ignore bank interest or dividends; toss it into your salary
    investment_income = stock_sales  # Assuming only stock sales for now
    excess_magi = max(0, magi_simplified - niit_threshold)
    niit_base = min(investment_income, excess_magi)
    niit = niit_base * 0.038  # NIIT rate is 3.8%

    # --- Total Tax Calculation ---
    total_federal_tax = federal_income_tax + federal_capital_gains_tax + niit
    total_ca_tax = ca_income_tax + ca_capital_gains_tax
    total_tax = total_federal_tax + total_ca_tax
    effective_tax_rate = total_tax / (salary + stock_sales) * 100
    return {
        "federal_income_tax": federal_income_tax,
        "federal_capital_gains_tax": federal_capital_gains_tax,
        "total_federal_tax": total_federal_tax,
        "ca_income_tax": ca_income_tax,
        "ca_capital_gains_tax": ca_capital_gains_tax,
        "total_ca_tax": total_ca_tax,
        "total_tax": total_tax,
        "effective_tax_rate": effective_tax_rate,
        "take_home_pay": salary + stock_sales - total_tax,
        "niit": niit
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate federal and California state income taxes for 2025.")
    parser.add_argument("salary", type=float, help="Annual salary")
    parser.add_argument("stock_sales", type=float, help="Proceeds from stock sales (long-term capital gains)")

    args = parser.parse_args()

    tax_results = calculate_taxes(args.salary, args.stock_sales)

    print(f"Salary: ${args.salary:,.2f}")
    print(f"Stock Sales: ${args.stock_sales:,.2f}")
    print("-" * 20)
    print(f"Federal Income Tax: ${tax_results['federal_income_tax']:,.2f}")
    print(f"Federal Capital Gains Tax: ${tax_results['federal_capital_gains_tax']:,.2f}")
    print(f"NIIT: ${tax_results['niit']:,.2f}")
    print(f"Total Federal Tax: ${tax_results['total_federal_tax']:,.2f}")
    print("-" * 20)
    print(f"California Income Tax: ${tax_results['ca_income_tax']:,.2f}")
    print(f"California Capital Gains Tax: ${tax_results['ca_capital_gains_tax']:,.2f}")
    print(f"Total California Tax: ${tax_results['total_ca_tax']:,.2f}")
    print("-" * 20)
    print(f"Total Tax (Federal + CA): ${tax_results['total_tax']:,.2f}")
    print(f"Effective Tax Rate: {tax_results['effective_tax_rate']:,.2f}%")
    print(f"Pre-Tax Total: ${args.salary + args.stock_sales:,.2f}")
    print(f"Estimated Post-Tax Take Home Pay: ${tax_results['take_home_pay']:,.2f}")
