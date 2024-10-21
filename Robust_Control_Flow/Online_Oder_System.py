#import all functions from Order_Functions.py using *
from Order_Functions import *

def main():
    while True:
        print("\nWelcome to the Online Store!")
        print("1. View Inventory")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Apply Discount")
        print("6. Checkout")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            display_inventory(inventory)
        
        elif choice == "2":
            item = input("Enter the item name: ").lower()
            quantity = int(input("Enter the quantity: "))
            add_to_cart(item, quantity)
        
        elif choice == "3":
            item = input("Enter the item name: ").lower()
            quantity = int(input("Enter the quantity: "))
            remove_from_cart(item, quantity)
        
        elif choice == "4":
            print("Your Cart:")
            if not cart:
                print("Your cart is empty.")
            else:
                for cart_item in cart:
                    print(f"{cart_item['quantity']} units of {cart_item['item']} at ${cart_item['price']} each")
            print(f"Total: ${calculate_cart_total():.2f}")
        
        elif choice == "5":
            discount_code = input("Enter your discount code: ").upper()
            apply_discount_to_cart(discount_code)
        
        elif choice == "6":
            payment_method = input("Enter payment method (credit/paypal): ").lower()
            process_order(payment_method)
        
        elif choice == "7":
            print("Exiting the store. Thank you for shopping!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
