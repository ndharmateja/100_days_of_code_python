def run():
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    persons = int(input("How many people to split the bill? "))
    share = bill * (1 + tip/100) / persons
    print(f"Each person should pay: ${share:.2f}")


if __name__ == "__main__":
    run()