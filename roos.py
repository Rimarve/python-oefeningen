from datetime import datetime
import locale # standaard bibliotheek om de internationale lokale tijd en datum te noteren
locale.setlocale(locale.LC_TIME, "nl_NL") # nederlandse tijdnotering 

nu = datetime.now() # huidige DTG (datum tijd groep)



datum_tijd = nu.strftime("%d %B %Y, %H:%M:%S") # toont dag maand jaar, uur minuut seconde

def groet(naam):
	print(f"Hallo, {naam}. Vandaag is het {datum_tijd}.")

groet("Rimar")


