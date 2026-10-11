
portfolio = {}

while True:
    stock = input("Enter stock name (or 'done' to finish): ")

    if stock.lower() == "done":
        break

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter buying price: "))

    portfolio[stock] = quantity * price

print("\nStock Portfolio:")

total = 0

for stock, value in portfolio.items():
    print(stock, "=", value)
    total += value

print("Total Investment =", total)

