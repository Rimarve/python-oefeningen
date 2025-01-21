def check_range(getallen):
	x = range(getallen)
	for n in x:
		print(n)

reeks = 3
print(check_range(reeks))


def bereken_factorial(getal):
	factorial = 1
	for i in range(1, getal+1):
		factorial = factorial * i
	return factorial
print(f"factor = {bereken_factorial(23)}")




#find maximum of three numbers
# def max_of_twee(x, y):

# 	if x > y:
# 		return x
# 	return y

# print(max_of_twee(10,15))

# def draai_om(zin):
# 	txt = zin[::-1]
# 	return  # je moet iets teruggeven anders krijg je none

# _input = "1234abcd"

# print(draai_om(_input))

# def som_van_nummers(lijst):
# 	totaal = sum(lijst)	
# 	return totaal

# nummers = [8, 2, 3, 0, 7]

# print(f"De som van alle nummers = {som_van_nummers(nummers)}")


# def vermenigvuldig(nummers):
# 	totaal = 1
# 	for i in nummers:
# 		totaal *= i
# 	return totaal


# list1 = [8, 2, 3, -1, 7]

# print(f"Vermenigvuldigen van alle nummers = {(vermenigvuldig(list1))}")


# def bereken_gemiddelde(leeftijd):

# 	if not leeftijd:
# 		print("lege lijst")
# 		return None
# 	totaal = sum(leeftijd)
# 	aantal = len(leeftijd)
# 	gemiddelde = totaal / aantal
# 	print(f"📊 Het gemiddelde van de leeftijden is: {gemiddelde:.2f} jaar")
# 	return gemiddelde

# leeftijden = [25, -30, 22, 40, 35, 28, 27, 31, 29, 33]
# # bereken_gemiddelde(leeftijden)

# bereken_gemiddelde(leeftijden)

