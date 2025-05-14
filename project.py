import pandas as pd
import matplotlib.pyplot as plt

# Read the simulated Bitcoin data
data = pd.read_csv("btc_data.csv", parse_dates=["Date"], index_col="Date")

# Add a column for the day of the week (0=Monday, ..., 6=Sunday)
data["day"] = data.index.weekday

# Initial capital and Bitcoin balance
money = 1000.0
btc = 0.0
values = []
dates = []

# Buy on Wednesday (day 2) and sell on Friday (day 4)
for i in range(len(data) - 1):
    today = data.iloc[i]
    tomorrow = data.iloc[i + 1]

    if today["day"] == 2:  # Wednesday: Buy
        if money > 0:
            btc = money / today["Open"]
            money = 0.0

    elif today["day"] == 4:  # Friday: Sell
        if btc > 0:
            money = btc * today["Close"]
            btc = 0.0

    # Calculate the current portfolio value
    today_price = today["Close"]
    total_value = money + (btc * today_price)
    values.append(total_value)
    dates.append(today.name)

# Calculate the final portfolio value
final_value = money + (btc * data.iloc[-1]["Close"])

# Plot the portfolio value over time
plt.figure(figsize=(12, 6))
plt.plot(dates, values, label="Portfolio Value", color="green")
plt.title("Portfolio Value Over Time (Buy on Wednesday, Sell on Friday)")
plt.xlabel("Date")
plt.ylabel("Value (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
