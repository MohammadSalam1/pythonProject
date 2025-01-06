def calculate_loan_payment(loan_amount, annual_interest_rate, loan_years):
    # Calculate monthly interest rate
    r = annual_interest_rate / (12 * 100)
    # Calculate total number of payments
    n = loan_years * 12
    # Calculate monthly payment using the amortization formula
    monthly_payment = (loan_amount * r * (1 + r)**n) / ((1 + r)**n - 1)
    # Calculate total amount repaid
    total_repaid = monthly_payment * n
    # Return both monthly payment and total repaid
    return monthly_payment, total_repaid

# Test cases
print(calculate_loan_payment(100000, 5, 10))  # Expected Output: (~1060.66, ~127279.12)
print(calculate_loan_payment(200000, 3.5, 15))  # Expected Output: (~1428.43, ~257117.66)
print(calculate_loan_payment(50000, 7, 5))  # Expected Output: (~990.06, ~59403.36)
