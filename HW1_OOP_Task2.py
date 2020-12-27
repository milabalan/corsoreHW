
# 2. Create two classes: Laptop, Guitare, one for composition, another one for aggregation.
class Laptop:
    def __init__(self):
        soft1=Soft('Slack')
        soft2=Soft('PyCharm')
        soft3=Soft('Trello')
        self.soft_all=[soft1,soft2,soft3]
class Soft:
    def __init__(self,app):
        self.app=app

lp=Laptop()


class Chords:
    def __init__(self,amount,think,lenth):
        self.amount=amount
        self.think=think
        self.lenth=lenth
class Guitare:
    def __init__(self,chord:Chords):
        self.chord=chord
    def info(self):
        return 'This Guitare has {} chords. Think of chords is {}, lenth is {}'.format(self.chord.amount, self.chord.think, self.chord.lenth)

x=Chords(1,8,60)
y=Guitare(x)
print(y.info())
