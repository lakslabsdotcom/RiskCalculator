# Risk Calculator with Risk-to-Reward Ratio

# Input section
account_balance = float(input("Enter your account balance ($): "))
risk_percent = float(input("Enter risk % per trade: "))
entry_price = float(input("Enter entry price: "))
stop_loss = float(input("Enter stop loss price: "))
target_price = float(input("Enter target price: "))

# Calculations
risk_amount = account_balance * (risk_percent / 100)
stop_loss_points = abs(entry_price - stop_loss)
position_size = round(risk_amount / stop_loss_points, 2)

# Risk-to-reward calculations
reward = abs(target_price - entry_price)
risk_to_reward = round(reward / stop_loss_points, 2)

# Output
print("\n📊 Risk Summary")
print(f"Account Balance: ${account_balance}")
print(f"Risk %: {risk_percent}%")
print(f"Risk Amount: ${risk_amount}")
print(f"Stop Loss Points: {stop_loss_points}")
print(f"Position Size: {position_size}")
print(f"Target Price: {target_price}")
print(f"Reward: {reward}")
print(f"🎯 Risk-to-Reward Ratio: {risk_to_reward} : 1")

