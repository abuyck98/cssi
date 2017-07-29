percy_invitation = ("The family of Percy Weasley proudly invite you to their "
                    "graduation commencement on Saturday the 22nd of May 1993. "
                    "Festivities will be held at The Burrow. See you then!")

wrong_date = "Saturday the 22nd of May 1993"

#functions in python = def say_hello():
#   print('Hello')

#boring parrot
def boring_parrot(parrot_saying):
    print "This is just practice %s" %(parrot_saying)

boring_parrot("yup")

#math parrot - Create a method that accepts two numbers as arguments and adds
# them together!
def math_parrot(num1, num2):
    print (num1 + num2)
math_parrot(1, 5)

#Friendly Parrot - This parrot greets people by returning their name and age
def Friendly_parrot(name, age):
    print str((name, age))
Friendly_parrot('ash', 23)

#Favorites Parrot - Tell this parrot about your three favorite things and he
# will return "I love <that thing> too!" for each of them.

def Favorites_parrot(fav_thing1, fav_thing2, fav_thing3):
    print("I love " + fav_thing1 + fav_thing2 + fav_thing3  + "too!")
Favorites_parrot("pie ", "movies ", "music ")
