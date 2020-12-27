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
        x=(int(self.weight))*2
        print("My speed is {} km/h".format(x))
        return x
    def info(self):
        print('Type of animal - {}, weight - {}kg, color is {}. I CAN RUN!'.format(self.typeanimal,self.weight,self.color))


class Cat(Mammals):
    def miu(self):
        print('Miu-miu')
    def info(self):
        print('Type of animal - {}, weight - {}kg, color is {}. Miu-miu )))!'.format(self.typeanimal,self.weight,self.color))


class Little_animals(Animals):
    def likemilk(self):
        print('I like milk')
        vol=self.weight/5
        print('I drink {}l of milk per day'.format(vol))
        return vol
    def info(self):
        print('Type of animal - {}, weight - {}kg, color is {}. I am a little animal and i like milk )))!'.format(self.typeanimal,self.weight,self.color))


class Kitten(Little_animals,Mammals):
    def game(self):
        print('I like game')


#call examples
animal1=Animals('dog',8,'black')
animal2=Mammals('tiger',2,'grey')
animal4=Cat('cat',1,'red')
animal4.info()
animal7=Kitten('cat',2,'white')
x=animal7.likemilk()
y=animal7.run()

