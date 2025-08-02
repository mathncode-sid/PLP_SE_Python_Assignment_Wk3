# Discount Calculator Script

This Python script calculates the final price of an item based on a user-provided percentage discount. It only applies the discount if it is **20% or higher**; otherwise, the original price remains unchanged.

---

## Features

- Takes user input for:
  - Initial item price
  - Discount percentage
- Applies discount only if it's **20% or more**
- Handles invalid inputs gracefully using `try-except`
- Outputs the final price with or without discount

---

## How It Works

1. The user is prompted to enter the item's price and the percentage discount.
2. The `calculate_discount()` function:
   - Checks if the discount is greater than or equal to 20%
   - If yes, calculates and returns the discounted price
   - If not, returns the original price
3. The result is printed to the user with appropriate messaging.

---

## Example

**Input:**
```
Enter the initial price of the item: 1000
Enter the percentage discount: 25
```

**Output:**
```
The final price of the item after the 25.0% discount is 750.00
```

---

**Input:**
```
Enter the initial price of the item: 1000
Enter the percentage discount: 10
```

**Output:**
```
No discount has been applied. The final price of the product is 1000.00
```

---

## Error Handling

- If the user enters a non-numeric value (e.g. letters instead of numbers), the script will display:
```
Please enter valid values for the item price and percentage discount
```

---

## Requirements

- Python 3.x

No external libraries are needed.

---

## How to Run

Save the script to a `.py` file (e.g., `discount_calculator.py`) and run it in your terminal:

```bash
python discount_calculator.py
```

---

## License

This project is provided for learning purposes and is free to use or modify.
