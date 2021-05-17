class Player():
    def __init__(self,choix):
        if choix == 1 :
            self.name = "Red"
            self.insult = False
            self.hp = 10
            self.choix = 1
            self.rep = 0
            self.turn= 0
        elif choix == 2 :
            self.name = "Blue"
            self.insult = False
            self.hp = 10
            self.choix = 2
            self.rep = 0
            self.turn = 0

    def setHp(self,x):
        self.hp = x

    def getHp(self):
        return self.hp
    # def getStr(self):
    #     return self.str

    # def setStr(self, value):
    #     self.str.append(value)

    def getInsult(self):
        return self.insult

    def setInsult(self, value):
        self.insult = value