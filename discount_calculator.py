def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent /100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
try:
    price = float(input("Enter the initial price of the item: "))
    discount_percent = float(input("Enter the percentage discount: "))

    final_price = calculate_discount(price, discount_percent)

    if final_price == price:
        print(f"No discount has been applied. The final price of the product is {final_price:.2f}")
    else:
        print(f"The final price of the item after the {discount_percent}% discount is {final_price:.2f}")

except ValueError:
    print("Please enter valid values for the item price and percentage discount")