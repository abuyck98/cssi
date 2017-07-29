import random

print(random.randint(1,10)) #random refers to the library random

di_thing_1 = random.randint(1, 6)
di_thing_2 + random.randint(1, 6)

if(di_thing_1 == di_thing_2):
    print('Doubles! Move {0} spaces and roll again'.format(di_thing_1 * 2))
else:
    print('Move {0} spaces. Next player\'s turn!'.format(di_thing_1 + di_thing_2))
