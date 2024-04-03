# A python program that takes as input the age and experience of a staff and tells
# them their Annual Tax Revenue(ATR)

experience = float(input("Input your years of experience:\n"))
age = float(input("Input your age:\n"))


if age >= 55 and experience > 25:
    print("Your ATR is N5,600,000")
elif age >= 45 and experience > 20:
    print("Your ATR is N4,480,000")
elif age >= 35 and experience > 10:
    print("Your ATR is N1,500,000")
elif age < 35 and experience < 10:
    print("Your ATR is N550,000")