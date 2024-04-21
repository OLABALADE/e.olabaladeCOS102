import tkinter as tk

grade_dict = {}

def submit():
    window = tk.Toplevel(root)
    window.geometry("500x500")
    count_grade = 0

    label_1 = tk.Label(window)
    label_1.pack()
    label_1.configure(bg="white")


    # Checks if the applicant meets the 5 credits requirement
    for grade in grade_dict.values():

        if grade.get() in ["A", "B", "C"]:
            count_grade += 1

    name = (surname_entry.get().lower(), first_name_entry.get().lower(), course_var.get())

    if count_grade == 5:

        admitted.append(name)
        label_1.config(text=f"Your form has been submitted {name[0].upper()} {name[1].upper()}. We will get back to you")
    else:
        not_admitted.append(name)
        label_1.config(text=f"Your form has been submitted {name[0]} {name[1]}. We will get back to you")
    


admitted = []
not_admitted = []
subjects = ["Mathematics", "English", "Physics", "Chemistry", "Literature in English", "Government", "Biology"]

root = tk.Tk()
root.geometry("600x600")
root.title("Admission")
root.config(bg="white")


# Labels and Entries
first_name_label = tk.Label(text="First Name: ", bg="white").grid(row=0, column=0)
first_name_entry = tk.Entry()
first_name_entry.grid(row=0, column=1)

surname_label = tk.Label(text="Surname: ", bg="white").grid(row=1, column=0)
surname_entry = tk.Entry()
surname_entry.grid(row=1, column=1)

course_label = tk.Label(text="Course of Study: ", bg="white").grid(row=2, column=0)
course_var = tk.StringVar()
courses = ["Computer Science", "Mass Communication"]
course_menu = tk.OptionMenu(root, course_var, *courses)
course_menu.grid(row=2, column=1)

label = tk.Label(text = "Select 5 O level Subjects and Input your Grade", bg="white").grid(row=3, column=1)

for i in range(4,8):
    subject_label = tk.Label(text="subject: ", bg="white")
    subject_label.grid(row=i, column=0)
    subject_var = tk.StringVar()
    subject_menu = tk.OptionMenu(root, subject_var, *subjects)
    subject_menu.grid(row=i, column=1)

    grade_label = tk.Label(text="grade: ", bg="white")
    grade_label.grid(row=i, column=2)
    grade_var = tk.StringVar()
    grades = ["A", "B", "C", "D", "E", "F"]
    grade_menu = tk.OptionMenu(root, grade_var, *grades)
    grade_menu.grid(row=i, column=3)


    grade_dict[i-2] = grade_var



submit_button = tk.Button(root, text="Submit", bg="white", command=submit)
submit_button.grid(row=10, column=1)


root.mainloop()
