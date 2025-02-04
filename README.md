# 2025 California Stock Tax Estimator

**Disclaimer:** This program is for **entertainment purposes only** and does not constitute professional tax advice. Use it at your own risk. Tax laws are complex and subject to change. Consult a qualified tax professional for personalized advice.

## Description

This Python program provides an **estimated** calculation of federal and California state income taxes for a single filer in 2025, considering salary and long-term capital gains from stock sales.

**Key Features:**

* Calculates federal income tax, federal capital gains tax, and California income tax using tax brackets.
* Includes the Net Investment Income Tax (surprise, you might owe more tax!)
* Provides an estimated overall tax rate and post-tax take-home pay.

**Limitations:**

* **California-specific:** This program is configured for California tax brackets. You can customize the code for your own state if you wish.
* **Single Filers Only:** It only calculates taxes for single filers.
* **Simplified Assumptions:**
    * Assumes standard deduction (not itemized).
    * Assumes all stock sales qualify for long-term capital gains.
    * Does not consider:
        * Social Security, Medicare, or other extra taxes
        * Charitable donations
        * 401K or IRA contributions
        * Other sources of income (e.g., interest, dividends); just include it in your salary number.
        * Dependents, or other characteristics that affect overall tax liability
        * Itemized deductions

This is a simple calculator for simple estimations.

## How to Use

1. **Prerequisites:** Make sure you have Python installed on your system.
2. **Run the script:**

  ```bash
  python 2025_ca_stock_tax_estimator.py <salary> <stock_sales>
  ```
  Example: 
  ```bash
  python 2025_ca_stock_tax_estimator.py 1000000 1000000
  ```
  Output: 
  ```bash
  Salary: $1,000,000.00
  Stock Sales: $1,000,000.00
  --------------------
  Federal Income Tax: $321,470.25
  Federal Capital Gains Tax: $200,000.00
  Total Federal Tax: $549,970.25
  --------------------
  California Income Tax: $223,566.97
  California Capital Gains Tax: $0.00
  Total California Tax: $223,566.97
  --------------------
  Total Tax (Federal + CA): $773,537.22
  Effective Tax Rate: 38.68%
  NIIT: $28,500.00
  Estimated Post-Tax Take Home Pay: $1,226,462.78
