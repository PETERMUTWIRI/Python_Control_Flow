#This code helps you calculate the total price of items in a shopping cart after applying discounts to each item.\n
#  If a discount is invalid (e.g., more than 100% or less than 0%), it handles the error and continues to calculate the total.
def apply_discount(price, discount):
    try:
        if discount > 100 or discount <0:
            raise ValueError("Discount must be between 0 and 100")
        final_price =price - (price*discount /100)
        return final_price
    except Exception as e:
        return f"Error applying discount: {e}"
    return 0
    
def calculate_cart(items):
    total =0
    for item in items:
        price,discount =item
        total += apply_discount(price,discount)
        return total


cart_items = [(100, 10), (200, 20), (50, 5)]
print(f"Total cart price: {calculate_cart(cart_items)}")   


