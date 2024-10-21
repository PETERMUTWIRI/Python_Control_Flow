#Inventory data
inventory = {
    "laptop": {"price": 1000, "stock": 5},
    "phone": {"price": 500, "stock": 10},
    "tablet": {"price": 300, "stock": 7},
    "headphones": {"price": 100, "stock": 20}
}


#User cart initialization
cart = []

##Helper Funtions
### Funtions to display Available Inventory
def display_inventory(inventory):
    print("Available items:")
    for item, details in inventory.items():
        print(f"{item.title()}: ${details['price']} (Stock: {details['stock']})")



#Funtion to add Items to the cart
#This function handles adding items to the cart, checking if they are in stock, and validating the quantity requested by the user.

def add_to_cart(item, quantity):
    if item not in inventory:
        print(f"Error: {item} is not available in the inventory.")
        return
    if quantity >inventory[item]["stock"]:
        print(f"Error: Only {inventory[item]["stock"]} units of {item} available.")
        return
    if quantity <= 0:
        print(f"Error: You must add at least 1 unit of {item}.")
        return
    
    cart.append({"item": item, "quantity": quantity, "price": inventory[item]["price"]})
    inventory[item]["stock"] -= quantity
    print(f"Added {quantity} units of {item} to your cart.")   

#Funtion to remove items from the cart
#This funtion allows the user to remove items from the cart,update the stock accodingly.

def remove_from_cart(item, quantity):
    for cart_item in cart:
        if cart_item["item"] == item:
            if quantity > cart_item["quantity"]:
                print(f"Error: You only have {cart_item['quantity']} units of {item} in your cart.")
                return
            cart_item["quantity"] -= quantity
            if cart_item["quantity"] == 0:
                cart.remove(cart_item)
            inventory[item]["stock"] += quantity
            print(f"Removed {quantity} units of {item} from your cart.")
            return
    print(f"Error: {item} is not in your cart.")

#cart Calculation
#This function calculates the total price of the items in the cart.
def calculate_cart_total():
    total = 0
    for item in cart:
        total += item["quantity"] * item["price"]
    return total




#Discoount System
#This system checks the validity of discount codes and applies them to the total cart value.
valid_discounts = {"SAVE10": 10, "SAVE20": 20}

def apply_discount_to_cart(discount_code):
    if discount_code not in valid_discounts:
        print(f"Error: {discount_code} is not a valid discount code.")
        return 0
    
    discount_percentage = valid_discounts[discount_code]
    total_price = calculate_cart_total()
    discount_amount = total_price * discount_percentage / 100
    final_price = total_price - discount_amount
    
    print(f"Discount of {discount_percentage}% applied. Total price after discount: ${final_price:.2f}")
    return final_price

#Order Processing
#This funtion checks if the cart has items , and confirms the order ,and simulates the payment process
def process_order(payment_method):
    if not cart:
        print("Error: Your cart is empty. Add items before processing your order.")
        return
    
    total_price = calculate_cart_total()
    print(f"Processing your order... Total price: ${total_price:.2f}")
    
    if payment_method == "credit":
        print("Payment processed successfully using credit card.")
    elif payment_method == "paypal":
        print("Payment processed successfully using PayPal.")
    else:
        print(f"Error: {payment_method} is not a valid payment method.")
        return
    
    print("Order confirmed! Your items will be shipped shortly.")
    cart.clear()  # Empty the cart after order confirmation
