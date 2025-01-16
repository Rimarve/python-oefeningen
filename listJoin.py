# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise


# import re
# zelf verzonnen 

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = []
# print(friends_list)

x = csv.replace(":", ",")

# re.split(", |; | :", csv)

print(x)
print()