# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each.

class Animals:
    def __init__(self,typeanimal,weight,color):
        self.typeanimal=typeanimal
        self.weight=weight
        self.color=color

    def info(self):
        print('Type of animal - {}, weight - {}kg, color is {}'.format(self.typeanimal,self.weight,self.color))


class Birds(Animals):
    def flyt(self):
        print('I can fly')
    def info(self):
        print('Type of animal - {}, weight - {}kg, color is {}. I CAN FLY!'.format(self.typeanimal,self.weight,self.color))

class Mammals(Animals):
    def run(self):
        print('I can run')
    def info(self):
        print('Type of animal - {}, weight - {}kg, color is {}. I CAN RUN!'.format(self.typeanimal,self.weight,self.color))

class Cat(Mammals):
    def miu(self):
        print('Miu-miu')
    def info(self):
        print('Type of animal - {}, weight - {}kg, color is {}. Miu-miu )))!'.format(self.typeanimal,self.weight,self.color))


animal1=Animals('Dog',8,'Black')
animal2=Mammals('Tiger',2,'Grey')
animal4=Cat('cat',1,'Red')
animal4.info()
