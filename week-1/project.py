print("Welcome!.Input 1 to calculate simple interest")
print("Input 2 to caculate compound interest")
print("Input 3 to caculate annuity plan")
choice = input()

if choice == "1" or choice == "2" or choice == "3":

    rate = float(input("Input the Rate\n"))/100
    time = float(input("Input time in years\n"))

    if choice == "1":
        #simple interest 
        principal = float(input("Input the Principal\n"))
        si = principal * (1 + time*(rate))
        print(f"Simple interest will be {si}")

    elif choice == "2":
        #compound interest
        principal = float(input("Input the Principal\n"))
        n = float(input("Input n\n"))
        ci = principal * (1 + (rate/ n))**(n*time)
        print(f"Compound interest will be {ci}")


    else:
        #annuity plan
        pmt = float(input("Input PMT\n"))
        n = float(input("Input n\n"))
        ap = (pmt / (rate/n)) * (((1 + rate/n)**(n*time) - 1)) 
        print(f"Annuity plan will be {ap}")

else:
    print("wrong input.Try again")