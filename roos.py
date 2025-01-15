from datetime import datetime
import locale # standaard bibliotheek om de internationale lokale tijd en datum te noteren
locale.setlocale(locale.LC_TIME, "nl_NL") # nederlandse tijdnotering 

nu = datetime.now() # huidige DTG (datum tijd groep)

datum_tijd = nu.strftime("%d %B %Y, %H:%M:%S") # toont dag maand jaar, uur minuut seconde

def groet(naam): # def is het defineren van een functie, () is de parameter.
	print(f"Hallo, {naam}. Vandaag is het {datum_tijd}.")

groet("Rimar")

def dtg(target_dtg):
	delta = target_dtg - nu
	
	# reken dagen, uren en minuten uit
	days = delta.days
	hours, remainder = divmod(delta.seconds, 3600)
	minutes, seconds = divmod(remainder, 60)

	dagen = "dag" if days == 1 else "dagen"

	print(f"Resterende tijd tot landen in Nederland: {days} {dagen}, {hours:02d} uur, {minutes:02d} minuten en {seconds:02d} seconden.")

einddatum_tijd = datetime(2025, 1, 29, 13, 0, 0)

dtg(einddatum_tijd)