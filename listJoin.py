# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise


# import re
# zelf verzonnen 

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = []
# print(friends_list)
print('csv is:', type(csv))
# x = csv.replace(":", ",")
# y = x.replace(";", ",")
# re.split(", |; | :", csv)
y = csv.replace(';', ',').replace(':',',').split(',')
print('y is:', type(y))
# print(y.split(',')) # var Y is type string maar door comma's gescheden
# print(type(y)) 
# friends_list.append(y) 
print(y)
# print(friends_list)

# print(type(friends_list)) # type list 
# print(friends_list) # een lange list van een hele string.