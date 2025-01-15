sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]


limonade = int(input("Hoeveel limonade verkocht op zondag? "))

sales_w2.append(limonade)

# print(limonade) // output hetgene wat je input
# print(sales_w2) // output 2 lists 

sales_total = sales_w1 + sales_w2
print(sales_total)

best_day = max(sales_total)
worst_day = min(sales_total)

stuks = "stuk" if worst_day == 1 else "stuks"


totaal_verdiend = sum(sales_total) * 1.50	

print(f"Er zijn in totaal {sum(sales_total)} limonades verkocht. De beste dag was {best_day} stuks en de minste dag was {worst_day} {stuks}.")
print(f"Je hebt in totaal € {totaal_verdiend} verdiend.")
# print(len(sales_w1))
# print(len(sales_w2))

# naam = "Rimar"
# leeftijd = 31

# print(f"Mijn naam is " + naam)
# print(f"Mijn leeftijd is " + str(leeftijd))

# vrienden = ["Niels", "Sascha", "Casper", "Rik"]
# leeftijden = [31, 32, 22, 33]

# print(vrienden[1],vrienden[2:4])
# print(len(vrienden))
# vrienden.reverse()
# vrienden.sort(reverse=True)
# print(min(vrienden))

# leeftijden.sort()
# print(max(leeftijden))
# del vrienden[2]

# print(vrienden)

