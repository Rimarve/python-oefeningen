

def bereken_gemiddelde(leeftijd):

	if not leeftijd:
		print("lege lijst")
		return None
	totaal = sum(leeftijd)
	aantal = len(leeftijd)
	gemiddelde = totaal / aantal
	print(f"📊 Het gemiddelde van de leeftijden is: {gemiddelde:.2f} jaar")
	return gemiddelde

leeftijden = [25, -30, 22, 40, 35, 28, 27, 31, 29, 33]
# bereken_gemiddelde(leeftijden)

bereken_gemiddelde(leeftijden)

