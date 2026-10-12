def calculate_total(price, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    total = price * quantity
    return total