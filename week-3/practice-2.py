#Input from user 
m = float(input("Enter mass in kilograms: "))

# Constant value for the speed of light in m/s 
c = 299792458

# Calculating energy using Einstein equation
energy = m * c ** 2

# Displaying the result
print(f"The energy equivalent to {m}kg of mass is {energy} joules")