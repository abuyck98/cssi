#Exercise: Defining a spaceship class
#What properties will your spaceship have? Define 3 properties
#Define 3 properties for your spaceship, then use the class to create 2 different instances of your spaceship

class Rocket(object):
    def __init__ (self, name, size, color, pilot_name):
        self.name = name
        self.size = size
        self.color = color
        self.pilot_name = pilot_name


    def description(self):
        print('Hello! I\'m the rocket named ' + self.name + ' I am pretty ' + self.size + ' and I am ' + self.color)

    def pilot_name(self):
        if 

zoomie = Rocket('Zoomie', 'small', ' blue')

zoomie.description()
