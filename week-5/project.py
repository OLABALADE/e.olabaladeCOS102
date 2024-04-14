import tkinter as tk
from tkinter import messagebox
import pandas as pd



def welcomeMessage(firstname, surname,department, file):
    window = tk.Toplevel(root)
    window.title("Welcome")
    window.geometry("500x500")
    window.configure(bg="white")

    label_1 = tk.Label(window, text=f"Welcome {surname.upper()} {firstname.upper()}\n")
    label_1.pack()
    label_1.configure(bg="white")

    label_2 = tk.Label(window, text=f"These are your other department members of the {department} department:")
    label_2.pack()
    label_2.configure(bg="white")

    #Finds other members of the same department as the user
    department_memebers = file.loc[(file.DEPARTMENT.str.lower() == department) & 
                                   (file.SURNAME.str.lower() != surname) & 
                                   (file["FIRST NAME"].str.lower() != firstname)]
    
    department_memebers = department_memebers.values.tolist()
    
    #Displays the members 
    for member in department_memebers:
        
        label = tk.Label(window, text=f"{member[1].upper()} {member[2].upper()}\n")
        label.pack()
        label.configure(bg="white")



def submit():
    file = pd.read_csv("GIG-logistics.csv")

    surname = surname_entry.get().lower()
    first_name = first_name_entry.get().lower()
    department = department_entry.get().lower()

    #If row containing the user surname, first name and department exist
    if not file.loc[(file.SURNAME.str.lower() == surname) & 
                    (file["FIRST NAME"].str.lower() == first_name) & 
                    (file.DEPARTMENT.str.lower() == department)].empty:

        welcomeMessage(first_name, surname, department, file)

    else:
        messagebox.showerror("Sorry", "This employee in not in our database")


#Create root window
root = tk.Tk()
root.title("GIG-Logistics Login")
root.geometry("500x500")
root.configure(bg="white")


#Surname label
surname_label = tk.Label(root, text="Surname: ")
surname_label.grid(row=0, column=0)
surname_label.configure(bg="yellow")
surname_entry = tk.Entry(root)
surname_entry.grid(row=0, column=1)

#First name label
first_name_label = tk.Label(root, text="First Name: ")
first_name_label.grid(row=1, column=0)
first_name_label.configure(bg="yellow")
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=1, column=1)

#Department label
department_label = tk.Label(root, text="Department: ")
department_label.grid(row=2, column=0)
department_label.configure(bg="yellow")
department_entry = tk.Entry(root)
department_entry.grid(row=2, column=1)

#Submit button
submit_button = tk.Button(root, text="Sumbit", command=submit)
submit_button.grid(row=3, column=1)
submit_button.configure(bg="Yellow")


root.mainloop()