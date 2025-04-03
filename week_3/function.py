def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price: float, the original price of the item.
    - discount_percent: float, the discount percentage to apply.
    
    Returns:
    - float: the final price after applying the discount if discount_percent is 20 or higher;
             otherwise, returns the original price.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

# Prompt the user for input and display the result.
def main():
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount = float(input("Enter the discount percentage: "))
        
        final_price = calculate_discount(original_price, discount)
        
        if discount >= 20:
            print(f"Final price after discount: {final_price}")
        else:
            print(f"No discount applied. Original price: {original_price}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
