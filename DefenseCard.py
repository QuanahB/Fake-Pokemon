class DefenseCard:

    def __init__(self,stat,image,name):
        self._stat = stat
        self._image = image
        self.name = name
        self.type = 'Defense Card'

    def boost(self,card):
        card.setDefense(self._stat + card.getDefense())

    def getStat(self):
        return self._stat

    def setImage(self,image):
        self._image = image

    def getImage(self):
        return self._image

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def getType(self):
        return self.type