print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

getal1 = input("Getal: ")
operator = input("+,-,*,/? ")
getal2 = input("Getal: ")

if operator == "+":
	print(float(getal1) + float(getal2))
elif operator == "-":
	print(float(getal1) - float(getal2))
elif operator == "/":
	print(float(getal1) / float(getal2))
else:
	print(getal1 * getal2)

