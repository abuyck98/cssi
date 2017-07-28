fave_food = raw_input('What\'s your fave food?')

fave_food = fave_food.upper()

vowels = ['A', 'E', 'I', 'O', 'U']

for v in vowels: #why is there a "for v" part??
    fave_food = fave_food.replace(v, v * 5)
print(fave_food)
