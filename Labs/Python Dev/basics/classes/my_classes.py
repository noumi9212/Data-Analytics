class Human():
    def __init__(self, _name, continent='Asia'):
        self.continent = continent
        self.name = _name

    def changeContinent(self, new_continent):
        self.continent = new_continent
def printHuman(object):
        print(f"{object.name} is located in {object.continent}")
    
        
nouman = Human('Nouman')
tesa = Human('Tesa')
tesa.continent = 'Africa'
tesa.name = 'manga'

printHuman(nouman)
printHuman(tesa)

