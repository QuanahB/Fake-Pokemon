from tkinter import *

class Card:

    def __init__(self,health,defense,name,image,attack):

        self._attack = attack
        self._health = health
        self._defense = defense
        self._name = name
        self._image = image


    def setName(self,name):
        self._name = name

    def getName(self):
        return self._name

    def setDefense(self,defense):
        self._defense = defense

    def getDefense(self):
        return self._defense

    def setHealth(self,health):
        self._health = health

    def getHealth(self):
        return self._health

    def setImage(self,image):
        self._image = image

    def getImage(self):
        return self._image

    def setAttack(self,attack):
        self._attackOne = attack

    def getAttack(self):
        return self._attack
