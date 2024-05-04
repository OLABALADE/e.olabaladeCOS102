from tkinter import *
from tkinter import messagebox


menu_items = {
    "Rice/Pasta": {
    "Jollof Rice": 350,
    "Coconut Fried Rice": 350,
    "Jollof Spaghetti": 350,
    },

    "Proteins": {
        "Sweet Chili Chicken": 1100,
        "Grilled Chicken Wings": 400,
        "Fried Beef": 400,
        "Fried Fish": 500,
        "Boiled Egg": 200,
    "   Sauteed  Sausages": 200
    },

    "Side Dishes" : {
        "Savoury Beans": 350,
        "Roasted Sweet Potatoes": 300,
        "Fried Plantains": 150,
        "Mixed Vegetables Salad": 150,
        "Boiled Yam": 150
    },

    "Soup & Swallow" : {
        "Eba": 100,
        "Poundo Yam": 100,
        "Semo": 100,
        "Atarna Soup": 450,
        "Egusi Soup": 480
    },

    "Beverages" :{
        "Water": 200,
        "Glass Drink(35cl)" : 150,
        "PET Drink(35cl)": 300,
        "PET Drink(50cl)": 350,
        "Glass/Canned Malt": 500,
        "Fresh Yo": 600,
        "Pineapple Juice": 350,
        "Mango Juice": 350,
        "Zobo Drink": 350
    }


}


#List of  meals irrespective of category
food_items = []
for category, items in menu_items.items():
    food_items.extend(items.keys())



def order():
    # Stores the order as strings to be display to the user
    order_text_list = []
    
    # adds current item to the user order
    def add_to_order():
        item = selected_item.get()

        #Checks if the value for quantity is an integer else show an error message
        try:
            quantity = int(quantity_entry.get())
        except ValueError:
            messagebox.showerror("Error", " Please input a number for quantity ")

        order_dict[item] = quantity
        #
        order_text_list.append(f"{quantity} {item}")
        order_text.set(f"Current Order: {', '.join(order_text_list)}\n")

    # Sumbits the user order
    def submit_order():
        if order_dict:
            order_summary = ", ".join(order_dict)

            total = 0
            discount = 0

            #Calculates total cost
            for food_type, items in  menu_items.items():
                for item in items:
                    if item in order_dict:
                        total+= items[item] * order_dict[item]

            #Adds discount
            if total < 2500 and total > 1000:
                total *= 0.1
                discount = 10
            elif total > 2500 and total < 5000:
                total *= 0.15
                discount = 15
            elif total > 5000:
                total *= 0.25
                discount = 25


            surname, firstname = surname_name_entry.get(), first_name_entry.get()
            message_text = f" {surname} {firstname} Your order: {order_summary}\n Total price: N{total} " + (f" .You got {discount} %discount" if discount!=0 else "")
            messagebox.showinfo("Order Submitted", message_text)
            order_dict.clear()
            order_text.set("Current Order: None")

        else:
            messagebox.showwarning("No Items", "No items in the order to submit.")


    order_window = Toplevel(root, bg="white")
    order_window.geometry("500x500")    
    order_window.title("order_window")



    # Labels and Entries
    Label(order_window, text="Personal Information", font=("Arial", 30, "bold", "underline", "italic"), bg="white", fg="black").place(x=60, y=0)

    surname_name = Label(order_window, text="Surname Name:", bg="white", fg="black").place(x=100, y=70)
    surname_name_entry = Entry(order_window)
    surname_name_entry.place(x= 80, y= 100)

    first_name = Label(order_window, text="First Name:", bg="white", fg="black").place(x= 270, y=70)
    first_name_entry = Entry(order_window)
    first_name_entry.place(x=250, y= 100)


    Label(order_window, text="Orders", font=("Arial", 30, "bold", "underline", "italic", ), bg="white", fg="black").place(x=190, y=130)
    Label(order_window, text="Quantity", bg="white", fg="black").place(x=330, y= 190)
    quantity_entry = Entry(order_window)
    quantity_entry.place(x= 300, y=210)
    
    #Stores user order
    order_dict = {}

    selected_item = StringVar(value=food_items[0])
    option_menu = OptionMenu(order_window, selected_item, *food_items)
    option_menu.config(bg="white", fg="black")
    option_menu.place(x=50, y=200)

    add_button = Button(order_window, text="Add to Order", command=add_to_order,bg="black", fg="white")
    add_button.place(x= 200, y= 250)

    submit_button = Button(order_window, text="Submit Order", command=submit_order, bg="black", fg="white")
    submit_button.place(x= 200, y= 300)

    #Shows current order
    order_text = StringVar(value="Current Order: None")
    order_label = Label(order_window, textvariable=order_text, bg="white", fg="black")
    order_label.place(x= 0, y= 350)





def menu():

    #Displays Items under the given meal category
    def display_items(dict, x, y):
        y += 20
        for item in dict:
            label = Label(menu, text = f"{item}: N{dict[item]}",bg="black", font=("Arial", 8), fg="white")
            label.place(x=x, y=y)
            y+=20

    def take_order():
        order()

    menu = Toplevel(root)
    menu.geometry("500x500")
    menu.title("Menu")
    menu.config(bg="white")


    bg_img = PhotoImage(file= "menu.png")
    Label(menu, image=bg_img).place(x=0, y=20)

    Label(menu, text="MENU", font=("Arial", 20, "underline", "bold"), bg="black", fg="white").place(x= 200, y=0)

    positions = [(30, 30), (30, 130), (30, 290), (340, 40), (340, 230)]
    
    #Displays menu 
    for (food_type, items), i in zip(menu_items.items(), range(5)):

        x_cor, y_cor= positions[i]
        Label(menu, text=f"{food_type}", font=("Arial", 10, "underline", "bold"), bg="black", fg="white").place(x=x_cor, y=y_cor)

        for item in items:
            display_items(items, x_cor, y_cor+10)


    order_button = Button(menu, text="Make an Order", command=take_order, bg="black", fg="white")
    order_button.place(x=200, y=410)

    menu.mainloop()




root = Tk()
root.geometry("500x500")
root.title("Pan-Atlantic University Cafeteria")
root.config(bg="white")

bg_img = PhotoImage(file= "menu.png")
bg_label = Label(root, image=bg_img).place(x=0, y=20)

welcome_text = Label(root, text= "Welcome to Pan-Atlantic University\n Cafeteria",justify="center", font=("Agatha", 15, "bold"), fg="white", bg="black")
welcome_text.place(x=50, y= 220)

menu_button = Button(root, text= "View Menu", bg="black", fg="white", command=menu)
menu_button.place(x=100, y=400)

order_button = Button(root, text= "Make an order", bg="black", fg="white", command=order)
order_button.place(x=300, y=400)



root.mainloop()