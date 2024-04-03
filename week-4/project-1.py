# A python program that prints the name, age, height and scores of students

# This function creates dictionary for each student by mapping their names, age, score, and height
def mapping(names, ages, heights, scores, data):
    for i in range(len(names)):
        info = [ages[i], heights[i], scores[i]]
        person = {names[i]: info}
        data.append(person)

# This function prints the data of each student in a table format
def printer(data):
    print("Names    | Age    | Height    | Scores")
    for element in data:
        for key, value in element.items():
            print(f"{key} | {value[0]} | {value[1]} | {value[2]}")
    print("\n")


"""Girls"""
girls_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girls_heights = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girls_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

girls_data = []
mapping(names= girls_names, ages= girls_ages, heights= girls_heights, scores= girls_scores, data= girls_data)


"""Boys"""
boys_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boys_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boys_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

boys_data = []
mapping(names= boys_names, ages= boys_ages, heights= boys_heights, scores= boys_scores, data=boys_data)

printer(girls_data)
printer(boys_data)
