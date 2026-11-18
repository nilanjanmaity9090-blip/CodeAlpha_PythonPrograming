# Example stock prices (in the same currency unit used for your calculation).
# These are sample hardcoded values for this internship task, not live market prices.
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

def track_portfolio():
    print("\n=== Stock Portfolio Tracker ===")
    print("Available stocks and sample prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"{stock}: {price}")

    portfolio = {}
    total_investment = 0

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not available. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid whole number for quantity.")
            continue

        investment = STOCK_PRICES[stock] * quantity
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += investment
        print(f"{stock}: {quantity} share(s) = {investment}")

    print("\n=== Portfolio Summary ===")
    if not portfolio:
        print("No stocks were added.")
    else:
        for stock, quantity in portfolio.items():
            value = STOCK_PRICES[stock] * quantity
            print(f"{stock}: {quantity} share(s) x {STOCK_PRICES[stock]} = {value}")
        print(f"Total Investment: {total_investment}")

        save = input("Save this summary to portfolio.txt? (yes/no): ").lower().strip()
        if save == "yes":
            with open("portfolio.txt", "w", encoding="utf-8") as file:
                file.write("Stock Portfolio Summary\n")
                for stock, quantity in portfolio.items():
                    value = STOCK_PRICES[stock] * quantity
                    file.write(
                        f"{stock}: {quantity} share(s) x {STOCK_PRICES[stock]} = {value}\n"
                    )
                file.write(f"Total Investment: {total_investment}\n")
            print("Summary saved successfully in portfolio.txt.")

if __name__ == "__main__":
    track_portfolio()
