#Dictionary : Allows us to work with Key:Value pair.
# Key unique identifier,Value contains our data.#
players = {'India':'Virat Kohli','Australia':'Steve Smith','England':'Joe Root','New Zealand':'Kane Williamson'}
print(players)

print(players.get('India'))#to print a specific key , returns value.

#to update a dictionary.
players.update({'Australia':'Pat Cummins','England':'Ben Stokes'})
print(players)

#To delete a key value pair and pop() method returns the deleted value , we can store it in a variable.
player_name = players.pop('England')
print(player_name)

print(len(players))#to know how many keys we have

print(players.get('Pakistan','Not found'))#to access a key,returns 'Not found' if no key is there.
print(players.keys())#to get all the keys in dicts.
print(players.values())# to get all the values in dicts.
print(players.items())# to get both all Keys:Value pair in dicts.

#for loop in dicts.
for key in players :#prints only Keys
    print(key)

for key,value in players.items():#to print all the Key:Value pair in dicts.
    print(key,value)
