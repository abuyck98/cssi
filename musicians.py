#create a musician class
# first atrributes will be name and genre
# other attributes: instrument, years active, top hit, number of albums

class Musician(object):
    """A class that creates musicians"""
    def __init__ (self, name, genre, top_hit, is_on_tour): # self = object calling, the name of the object itself
        self.name = name
        self.genre = genre
        self.top_hit = top_hit
        self.is_on_tour = is_on_tour


    def description(self):
        print('Hi, my name is ' + self.name + ' my number one single is ' + self.top_hit)

    def on_tour(self):
        if self.is_on_tour:
            print('Check out my tour')
        else:
            print('I\'m not on tour')

beyonce = Musician('Beyonce', 'R&B', 'Lemonade', True)

prince_clone = Musician('Prince', 'R&B', 'Rasberry Beret', False)

aj_clone = Musician('Michael Jackson', 'Pop', 'Thriller', False)

bruno_mars = Musician('Bruno Mars', 'Pop', '24K', True)

bruno_mars.on_tour()

#print(beyonce.name)
# print(beyonce.name + ' is a musician who plays ' + beyonce.genre + ' music.')

#print('Prince\'s top hit is ' + prince_clone.top_hit + '.')

#beyonce.description()
#prince_clone.description()
#aj_clone.description()
