# Tuples are Immutable,unlike lists. 
# Tuples don't support built-in methods like extend(),remove(),append(),pop(),insert().
# We can loop through tuples#

languages = ('English','Arabic','Hindi','Mandarin','English','Urdu')
print(languages)

for index,language in enumerate(languages):
    print(index,language)

print(languages.index('Hindi'))
print(languages.count('English')) # counts the number of occurence of Value.

# To add an empty tuple.
empty_tuple = ()
empty_tuple = tuple()
