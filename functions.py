def greeting(name, age=0):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print(f'Hello {name.capitalize()}, you will be {age} next birthday!')
    # print(f'We hear you like the color {color.lower()}')

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# color = input('Enter color: ').lower()

greeting("Rimar", 18)


def value_added_tax(amount):
	tax = amount * 0.37
	total_amount = amount * 1.25
	return f"{amount, tax, total_amount}"

prijs = value_added_tax(100)

print(prijs)

print()

a = 10
b = 25
print(a == b)