# Input values
monthly_investment = 100  # Amount invested each month
monthly_interest_rate = 0.01  # 1% monthly interest
months_to_invest = 12  # Total number of months to invest

# Initial future value
future_value = 0

month_counter = 1
while month_counter <= months_to_invest:
    future_value = (future_value + monthly_investment) * (1 + monthly_interest_rate)
    month_counter += 1