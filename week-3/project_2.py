import math 
import cmath

def quadratic_solver(a, b, c ):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("This ")
        print(x1, "and",  x2)

    elif discriminant == 0:
        x = (-b + math.sqrt(discriminant)) / (2 * a)
        print("This equation has double roots")
        print("It's root is ", x)

    elif discriminant < 0:
        x1c = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2c = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("This equation has complex roots")
        print("It's roots are ", x1c,"and", x2c)


def cubic_solver(a, b, c ,d):
    q = ((3 * a * c) -(b**2)) / (9 * (a**2))
    r = ((9*a*b*c) - (27 * a**2 *d )- (2 * (b**3))) / (54 * (a**3))
    s = (r + math.sqrt((q**3 + r**2))) **(1/3)
    t = (r - math.sqrt((q**3 + r**2)))
    t = t ** (1/3)
    print(t)
    print(r - math.sqrt((q**3 + r**2)))
    h = -2.65712393117584 ** (1/3)
    print(h)


    x1 = (s + t) - (b/(3*a))
    x2 = -(s+t)/2 - b/(3*a) + (cmath.sqrt(-3) * (s - t))/2
    x3 = -(s+t)/2 - b/(3*a) - (cmath.sqrt(-3) * (s - t))/2

    print(f"The roots of this equation are {x1}, {x2}, and {x3}")


def quartic_solver(a, b, c, d, e):
    pass



choice = input("What type of equation do you wish to compute:Input quadratic, or cubic ,or quartic\n")

if choice == "quadratic" or choice == "cubic" or choice == "quartic":

    a = float(input("input a\n"))
    b = float(input("input b\n"))
    c = float(input("input c\n"))

    if choice == "quadratic":
       quadratic_solver(a, b, c)
       
    elif choice == "cubic":
        d = float(input("input d\n"))
        cubic_solver(a, b, c, d)

    elif choice == "quartic":
        d = float(input("input d\n"))
        e = float(input("input e\n"))
        quadratic_solver(a,b,c,d,e)