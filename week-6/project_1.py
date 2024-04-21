import tkinter as tk
from tkinter import messagebox




def calculate_price():
    price = 0
    weight = int(weight_entry.get())
    location = location_var.get()

    if location == "Ibeju Lekki" and weight >= 10:
        price = 5000
    elif location == "Ibeju Lekki" and weight < 10:
        price = 3500
    elif location == "Epe" and weight >= 10:
        price = 10000
    elif location == "Epe" and weight < 10:
        price = 5000
    else:
        messagebox.showerror("Error", "Invalid Input")



    price_label.config(text=f"Total price is N{price}")


root = tk.Tk()
root.geometry("500x500")
root.title("Simi Services")

weight = tk.Label(text="Weight of package(kg): ", font="Arial").grid(row=0, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

location_label = tk.Label(text= "Location:").grid(row=1, column=0)


location_var = tk.StringVar()
locations = ["Ibeju Lekki", "Epe"]
location_menu = tk.OptionMenu(root, location_var, *locations)
location_menu.grid(row=1, column=1)

button = tk.Button(text="Calculate Price", command=calculate_price).grid(row=2, column=1)

price_label = tk.Label(text=f"Total price is N0", font="Arial")
price_label.grid(row=3, column=0)

root.mainloop()