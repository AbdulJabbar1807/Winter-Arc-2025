print("Hello World")
greeting = 'Hello'
name = 'Bob'

print(greeting)
greet = """Hello Bob, How are you doing
           is everything all right"""
print(len(greeting))
print(greeting[:3])
print(greeting.count('l'))
# formatting in python we can use different ways like concatenation , sting formatting and f formatting
print(greeting + ', '+ name + '.Welcome!')
print('{} {}.Welcome!'.format(greeting,name))
print(f'{greeting} {name}.Welcome!')

print(greeting.find('l'))
name = name.replace('BoB','Jack')
print(dir(name))
print(help(str))