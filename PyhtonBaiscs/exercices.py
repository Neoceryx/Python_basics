sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

lemonade_price = 1.5
new_value = input("Enter new sold")

sales_w2.append(int(new_value))
print(sales_w2)

sales = sales_w1+sales_w2
print(f"List combined: {sales}")

best_day = max(sales)
best_day_earnings = best_day * lemonade_price
print(f"You'r best day was: {best_day} and you sold: {best_day_earnings} ")

worst_day = min(sales)
worst_day_earnings = worst_day * lemonade_price
print(f" your worst day was: {worst_day} and you earning: {worst_day_earnings}")

total_earnings = best_day_earnings + worst_day_earnings
print(f"Total Earning was: {total_earnings}")