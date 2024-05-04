

# all_food = ['Jollof Rice', 'Coconut Fried Rice', 'Jollof Spaghetti',
#              'Eba', 'Poundo Yam', 'Semo', 'Atarna Soup', 'Egusi Soup',
#                'Sweet Chili Chicken', 'Grilled Chicken Wings', 'Fried Beef',
#                  'Fried Fish', 'Boiled Egg', 'Sauteed  Sausages',
#                    'Water', 'Glass Drink(35cl)', 'PET Drink(35cl)', 'PET Drink(50cl)', 'Glass/Canned Malt', 'Fresh Yo', 'Pineapple Juice', 'Mango Juice', 'Zobo Drink']


# import tkinter as tk
# from tkinter import messagebox

# # List of food and drink items
# food_items = ['Jollof Rice', 'Coconut Fried Rice', 'Jollof Spaghetti',
#               'Eba', 'Poundo Yam', 'Semo', 'Atarna Soup', 'Egusi Soup',
#               'Sweet Chili Chicken', 'Grilled Chicken Wings', 'Fried Beef',
#               'Fried Fish', 'Boiled Egg', 'Sauteed Sausages',
#               'Water', 'Glass Drink(35cl)', 'PET Drink(35cl)', 'PET Drink(50cl)',
#               'Glass/Canned Malt', 'Fresh Yo', 'Pineapple Juice', 'Mango Juice', 'Zobo Drink']

# # Create the root window
# root = tk.Tk()
# root.title("Purchase Order")

# # Variable to store the selected item
# selected_item = tk.StringVar(value=food_items[0])

# # List to store ordered items
# order_list = []

# # Function to add an item to the order list
# def add_to_order():
#     item = selected_item.get()
#     order_list.append(item)
#     order_text.set(f"Current Order: {', '.join(order_list)}")

# # Function to submit the entire order
# def submit_order():
#     if order_list:
#         order_summary = ", ".join(order_list)
#         messagebox.showinfo("Order Submitted", f"Your order: {order_summary}")
#         order_list.clear()
#         order_text.set("Current Order: None")
#     else:
#         messagebox.showwarning("No Items", "No items in the order to submit.")

# # Create an OptionMenu with the food items
# option_menu = tk.OptionMenu(root, selected_item, *food_items)
# option_menu.pack(pady=10)

# # Create a button to add an item to the order
# add_button = tk.Button(root, text="Add to Order", command=add_to_order)
# add_button.pack(pady=5)

# # Create a button to submit the entire order
# submit_button = tk.Button(root, text="Submit Order", command=submit_order)
# submit_button.pack(pady=5)

# # Label to display the current order
# order_text = tk.StringVar(value="Current Order: None")
# order_label = tk.Label(root, textvariable=order_text)
# order_label.pack(pady=5)

# # Run the Tkinter event loop
# root.mainloop()


