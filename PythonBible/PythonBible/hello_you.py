# Ask user for name

name = input('what is your name?: ')

# Ask user for age

age = input('what is your age?: ')

# Ask user for city

city = input('what is your city?: ')

# Ask user what they enjoy

love = input('what do you love doing?: ')

# create ouput text

string = 'your name is {} and you are {} years old. You live in {} and you love {}'
output= string.format(name, age, city ,love)

# print output to screen
print(output)
