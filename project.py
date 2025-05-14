
import pandas as pd
import matplotlib.pyplot as plt

# Load the simulated BTC data
df = pd.read_csv("simulated_btc.csv", parse_dates=["Date"], index_col="Date")

# Add WeekDay column
df["WeekDay"] = df.index.weekday

# Initialize capital and BTC balance
capital = 1000.0
btc_balance = 0.0
portfolio_values = []
dates = []

# Simulate buying on Wednesdays (weekday 2) and selling on Fridays (weekday 4)
for i in range(len(df) - 1):
    row = df.iloc[i]
    next_row = df.iloc[i + 1]

    if row["WeekDay"] == 2:  # Wednesday: Buy at Open
        if capital > 0:
            btc_balance = capital / row["Open"]
            capital = 0.0

    elif row["WeekDay"] == 4:  # Friday: Sell at Close
        if btc_balance > 0:
            capital = btc_balance * row["Close"]
            btc_balance = 0.0

    # Calculate current portfolio value
    current_price = row["Close"]
    portfolio_value = capital + (btc_balance * current_price)
    portfolio_values.append(portfolio_value)
    dates.append(row.name)

# Final portfolio value
final_value = capital + (btc_balance * df.iloc[-1]["Close"])

# Plot the portfolio value over time
plt.figure(figsize=(12, 6))
plt.plot(dates, portfolio_values, label="Portfolio Value", color="green")
plt.title("Portfolio Value Over Time (Buy on Wed, Sell on Fri)")
plt.xlabel("Date")
plt.ylabel("Value (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

