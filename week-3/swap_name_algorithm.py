first_name = input("Input first person's name \n")
first_age = input("Input first person's age \n")

second_name = input("Input second person's name \n")
second_age = input("Input second person's age \n")

age_holder = first_age
first_age = second_age
second_age = age_holder

print(f"{first_name}'s new age is {first_age} and {second_name}'s new age is {second_age} ")
