def compute_total_price(pizza_quantity, requires_delivery, is_tuesday, app_used):
    base_pizza_price = 12.0
    delivery_fee = 2.5
    tuesday_discount = 0.5
    app_discount = 0.25

    # Ensure a valid pizza quantity is entered
    while True:
        try:
            pizza_quantity = int(pizza_quantity)
            if pizza_quantity < 0:
                raise ValueError("Please enter a positive integer for pizza quantity!")
            break
        except ValueError:
            print("Please enter a valid number for pizza quantity!")
            pizza_quantity = input("How many pizzas are being ordered? ")

    # Validate delivery preference
    while requires_delivery.lower() not in ('y', 'n'):
        print('Please answer "Y" or "N" for delivery preference.')
        requires_delivery = input("Is delivery required? ")

    # Confirm if it's Tuesday
    while is_tuesday.lower() not in ('y', 'n'):
        print('Please answer "Y" or "N" for whether it is Tuesday.')
        is_tuesday = input("Is today Tuesday? ")

    # Confirm app usage
    while app_used.lower() not in ('y', 'n'):
        print('Please answer "Y" or "N" for app usage.')
        app_used = input("Did the customer use the app? ")

    # Apply applicable discounts and calculate the total price
    total_price = pizza_quantity * base_pizza_price
    if is_tuesday.lower() == 'y':
        total_price *= (1 - tuesday_discount)
    if requires_delivery.lower() == 'y' and pizza_quantity < 5:
        total_price += delivery_fee
    if app_used.lower() == 'y':
        total_price *= (1 - app_discount)

    return total_price


def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    pizza_quantity = input("How many pizzas are being ordered? ")
    requires_delivery = input("Is delivery required? ")
    is_tuesday = input("Is today Tuesday? ")
    app_used = input("Did the customer use the app? ")

    total_price = compute_total_price(pizza_quantity, requires_delivery, is_tuesday, app_used)

    print(f"\nTotal Price: £{total_price:.2f}.")


if __name__ == "__main__":
    main()
