# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.

    Returns:
    float: The final price after applying the discount (if applicable).
    """
    if discount_percent >= 20:  # Apply discount only if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return the original price if the discount is less than 20%
    
    # Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"After applying a {discount_percent}% discount, the final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")