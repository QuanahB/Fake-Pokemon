from tkinter import *
from Card import *
from DefenseCard import *
from HealthCard import *
import random
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



#Main:

window = Tk()
window.title("Fake Pokemon")
window.configure(background="white")

#GLOBALS
activeMonster1 = None
activeMonster2 = None

monsterCard1 = None
effectCard1 = None
effectCard2 = None
effectCard3 = None

monsterCard2 = None
effectCard4 = None
effectCard5 = None
effectCard6 = None

usagePointsOne = 0
usagePointsTwo = 0

#Functions

def monsterCard1Shuffle():
    global monsterCard1
    monsterCard1 = random.choice(deckOne)
    monsterSelect1.configure(image=monsterCard1.getImage())
    monsterSelect1.image = monsterCard1.getImage()

def monsterCard2Shuffle():
    global monsterCard2
    monsterCard2 = random.choice(deckOne)
    monsterSelect2.configure(image=monsterCard2.getImage())
    monsterSelect2.image = monsterCard2.getImage()

def effectCard1Shuffle():
    global effectCard1
    effectCard1 = random.choice(deckTwo)
    effectSelect1.configure(image=effectCard1.getImage())
    effectSelect1.image = effectCard1.getImage()

def effectCard2Shuffle():
    global effectCard2
    effectCard2 = random.choice(deckTwo)
    effectSelect2.configure(image=effectCard2.getImage())
    effectSelect2.image = effectCard2.getImage()

def effectCard3Shuffle():
    global effectCard3
    effectCard3 = random.choice(deckTwo)
    effectSelect3.configure(image=effectCard3.getImage())
    effectSelect3.image = effectCard3.getImage()

def effectCard4Shuffle():
    global effectCard4
    effectCard4 = random.choice(deckTwo)
    effectSelect4.configure(image=effectCard4.getImage())
    effectSelect4.image = effectCard4.getImage()

def effectCard5Shuffle():
    global effectCard5
    effectCard5 = random.choice(deckTwo)
    effectSelect5.configure(image=effectCard5.getImage())
    effectSelect5.image = effectCard5.getImage()

def effectCard6Shuffle():
    global effectCard6
    effectCard6 = random.choice(deckTwo)
    effectSelect6.configure(image=effectCard6.getImage())
    effectSelect6.image = effectCard6.getImage()

def redrawOne():
    monsterCard1Shuffle()
    effectCard1Shuffle()
    effectCard2Shuffle()
    effectCard3Shuffle()

def redrawTwo():
    monsterCard2Shuffle()
    effectCard4Shuffle()
    effectCard5Shuffle()
    effectCard6Shuffle()

def updateActiveMonsterInfo1():
    activeMonsterInfo1.delete(0.0, END)
    activeMonsterInfo1.insert(END, "Health: " + str(activeMonster1.getHealth()) + "\nAttack: " +
                              str(activeMonster1.getAttack()) + "\nDefense: " + str(activeMonster1.getDefense()))

def updateActiveMonsterInfo2():
    activeMonsterInfo2.delete(0.0, END)
    activeMonsterInfo2.insert(END, "Health: " + str(activeMonster2.getHealth()) + "\nAttack: " +
                              str(activeMonster2.getAttack()) + "\nDefense: " + str(activeMonster2.getDefense()))

def displayInfo1(card):

    if card == monsterCard1:
        infoPanel1.delete(0.0,END)
        infoPanel1.insert(END,"Name: " + card.getName() + "\nHealth: " + str(card.getHealth()) + "\nAttack: " +
                          str(card.getAttack()) + "\nDefense: " + str(card.getDefense()))

    if card == effectCard1:
        infoPanel1.delete(0.0,END)
        infoPanel1.insert(END,"Name: " + card.getName() + "\nType: " + card.getType() + "\nStat: " +
                          str(card.getStat()))

    if card == effectCard2:
        infoPanel1.delete(0.0,END)
        infoPanel1.insert(END,"Name: " + card.getName() + "\nType: " + card.getType() + "\nStat: " +
                          str(card.getStat()))

    if card == effectCard3:
        infoPanel1.delete(0.0,END)
        infoPanel1.insert(END,"Name: " + card.getName() + "\nType: " + card.getType() + "\nStat: " +
                          str(card.getStat()))


def displayInfo2(card):

    if card == monsterCard2:
        infoPanel2.delete(0.0,END)
        infoPanel2.insert(END,"Name: " + card.getName() + "\nHealth: " + str(card.getHealth()) + "\nAttack: " +
                          str(card.getAttack()) + "\nDefense: " + str(card.getDefense()))

    if card == effectCard4:
        infoPanel2.delete(0.0,END)
        infoPanel2.insert(END,"Name: " + card.getName() + "\nType: " + card.getType() + "\nStat: " +
                          str(card.getStat()))

    if card == effectCard5:
        infoPanel2.delete(0.0,END)
        infoPanel2.insert(END,"Name: " + card.getName() + "\nType: " + card.getType() + "\nStat: " +
                          str(card.getStat()))

    if card == effectCard6:
        infoPanel2.delete(0.0,END)
        infoPanel2.insert(END,"Name: " + card.getName() + "\nType: " + card.getType() + "\nStat: " +
                          str(card.getStat()))


def useEffect1(card):
    global activeMonster1
    global  usagePointsOne

    try:
        if card == effectCard1:
            if type(card) is DefenseCard:
                activeMonster1.setDefense(activeMonster1.getDefense() + card.getStat())
                updateActiveMonsterInfo1()
            if type(card) is HealthCard:
                activeMonster1.setHealth(activeMonster1.getHealth() + card.getStat())
                updateActiveMonsterInfo1()

        if card == effectCard2:
            if type(card) is DefenseCard:
                activeMonster1.setDefense(activeMonster1.getDefense() + card.getStat())
                updateActiveMonsterInfo1()
            if type(card) is HealthCard:
                activeMonster1.setHealth(activeMonster1.getHealth() + card.getStat())
                updateActiveMonsterInfo1()

        if card == effectCard3:
            if type(card) is DefenseCard:
                activeMonster1.setDefense(activeMonster1.getDefense() + card.getStat())
                updateActiveMonsterInfo1()
            if type(card) is HealthCard:
                activeMonster1.setHealth(activeMonster1.getHealth() + card.getStat())
                updateActiveMonsterInfo1()

        usagePointsOne = usagePointsOne + 1
        activateSwitch1()

        effectSelect1['state'] = DISABLED
        effectSelect2['state'] = DISABLED
        effectSelect3['state'] = DISABLED
        activeMonsterAttack1['state'] = DISABLED

    except AttributeError:
        print("no card in slot to be made active yet")


def useEffect2(card):
    global activeMonster2
    global usagePointsTwo

    try:
        if card == effectCard4:
            if type(card) is DefenseCard:
                activeMonster2.setDefense(activeMonster2.getDefense() + card.getStat())
                updateActiveMonsterInfo2()
            if type(card) is HealthCard:
                activeMonster2.setHealth(activeMonster2.getHealth() + card.getStat())
                updateActiveMonsterInfo2()

        if card == effectCard5:
            if type(card) is DefenseCard:
                activeMonster2.setDefense(activeMonster2.getDefense() + card.getStat())
                updateActiveMonsterInfo2()
            if type(card) is HealthCard:
                activeMonster2.setHealth(activeMonster2.getHealth() + card.getStat())
                updateActiveMonsterInfo2()

        if card == effectCard6:
            if type(card) is DefenseCard:
                activeMonster2.setDefense(activeMonster2.getDefense() + card.getStat())
                updateActiveMonsterInfo2()
            if type(card) is HealthCard:
                activeMonster2.setHealth(activeMonster2.getHealth() + card.getStat())
                updateActiveMonsterInfo2()

        usagePointsTwo = usagePointsTwo + 1
        activateSwitch2()

        effectSelect4['state'] = DISABLED
        effectSelect5['state'] = DISABLED
        effectSelect6['state'] = DISABLED
        activeMonsterAttack2['state'] = DISABLED

    except AttributeError:
        print("no card to place effect on")

def makeActive1():

    global activeMonster1
    global monsterCard1
    global usagePointsOne

    try:
        activeMonster1 = monsterCard1
        activeMonsterSlot1.configure(image=activeMonster1.getImage())
        activeMonster1.image = activeMonster1.getImage()

        activeMonsterInfo1.delete(0.0, END)
        activeMonsterInfo1.insert(END, "Health: " + str(activeMonster1.getHealth()) + "\nAttack: " +
                                  str(activeMonster1.getAttack()) + "\nDefense: " + str(activeMonster1.getDefense()))

        monsterSelect1['state'] = DISABLED
    except AttributeError:
        print("no card in slot to be made active yet")

def makeActive2():

    global activeMonster2
    global monsterCard2
    global usagePointsTwo

    try:
        activeMonster2 = monsterCard2
        activeMonsterSlot2.configure(image=activeMonster2.getImage())
        activeMonsterSlot2.image = activeMonster2.getImage()

        activeMonsterInfo2.delete(0.0, END)
        activeMonsterInfo2.insert(END, "Health: " + str(activeMonster2.getHealth()) + "\nAttack: " +
                                  str(activeMonster2.getAttack()) + "\nDefense: " + str(activeMonster2.getDefense()))

        monsterSelect2['state'] = DISABLED
    except AttributeError:
        print('no card in slot to be made active yet')

def attack1():
    global activeMonster2
    global usagePointsOne
    if activeMonster1.getAttack() > activeMonster2.getDefense():
        damage = activeMonster1.getAttack() - activeMonster2.getDefense()
        activeMonster2.setHealth(activeMonster2.getHealth() - damage)
        updateActiveMonsterInfo2()
    if activeMonster1.getAttack() < activeMonster2.getDefense():
        damage = ((activeMonster2.getDefense()/activeMonster1.getAttack()) * 2)
        activeMonster2.setHealth(activeMonster2.getHealth() - damage)
        updateActiveMonsterInfo2()

    usagePointsOne = usagePointsOne + 1
    activateSwitch1()

    monsterSelect1['state'] = DISABLED
    effectSelect1['state'] = DISABLED
    effectSelect2['state'] = DISABLED
    effectSelect3['state'] = DISABLED
    activeMonsterAttack1['state'] = DISABLED

def attack2():
    global activeMonster1
    global usagePointsTwo
    damage = activeMonster2.getAttack() - activeMonster1.getDefense()
    activeMonster1.setHealth(activeMonster1.getHealth() - damage)
    updateActiveMonsterInfo1()

    usagePointsTwo = usagePointsTwo + 1
    activateSwitch2()

    monsterSelect2['state'] = DISABLED
    effectSelect4['state'] = DISABLED
    effectSelect5['state'] = DISABLED
    effectSelect6['state'] = DISABLED
    activeMonsterAttack2['state'] = DISABLED

def activateSwitch1():

    global usagePointsOne
    global usagePointsTwo


    if usagePointsOne == 1 and usagePointsTwo == 0:
        endTurn1['state'] = NORMAL

def switch1():

    global usagePointsOne
    monsterSelect1['state'] = DISABLED
    effectSelect1['state'] = DISABLED
    effectSelect2['state'] = DISABLED
    effectSelect3['state'] = DISABLED
    activeMonsterAttack1['state'] = DISABLED

    effectSelect4['state'] = NORMAL
    effectSelect5['state'] = NORMAL
    effectSelect6['state'] = NORMAL
    activeMonsterAttack2['state'] = NORMAL
    usagePointsOne = 0
    endTurn1['state'] = DISABLED

def activateSwitch2():

    global usagePointsOne
    global usagePointsTwo


    if usagePointsOne == 0 and usagePointsTwo == 1:
        endTurn2['state'] = NORMAL


def switch2():
    global usagePointsTwo
    effectSelect1['state'] = NORMAL
    effectSelect2['state'] = NORMAL
    effectSelect3['state'] = NORMAL
    activeMonsterAttack1['state'] = NORMAL

    monsterSelect2['state'] = DISABLED
    effectSelect4['state'] = DISABLED
    effectSelect5['state'] = DISABLED
    effectSelect6['state'] = DISABLED
    activeMonsterAttack2['state'] = DISABLED
    usagePointsTwo = 0
    endTurn2['state'] = DISABLED









#Cards and Decks

#Set All Images for Cards

firstImage = PhotoImage(file=resource_path('GreenM.gif'))
secondImage = PhotoImage(file=resource_path('DancingZombies.gif'))
thirdImage = PhotoImage(file=resource_path('Godzilla.gif'))
fourthImage = PhotoImage(file=resource_path('HydraPride.gif'))
fifthImage = PhotoImage(file=resource_path('PinkThing.gif'))
sixthImage = PhotoImage(file=resource_path('WeirdAlien.gif'))

seventhImage = PhotoImage(file=resource_path('DeepFreeze.gif'))
eigthImage = PhotoImage(file=resource_path('RainyDay.gif'))
ninthImage = PhotoImage(file=resource_path('FallingTower.gif'))
tenthImage = PhotoImage(file=resource_path('EnchantedEyes.gif'))
eleventhImage = PhotoImage(file=resource_path('OminousSpell.gif'))
twelthImage = PhotoImage(file=resource_path('Unite.gif'))

blankImage = PhotoImage(file=resource_path('Solid_black.gif')) # Fill in blank image


#Monster Cards
monster1 = Card(1000,550,'Blue Horn',firstImage,600)
monster2 = Card(600,225,'Dancing Zombies',secondImage,400)
monster3 = Card(1500,600,'Godzilla',thirdImage,700)
monster4 = Card(1200,750,'Hydra Pride',fourthImage,750)
monster5 = Card(700,600,'Pink Thing',fifthImage,650)
monster6 = Card(400,700,'Weird Alien',sixthImage,750)

deckOne = []
deckOne.append(monster5)
deckOne.append(monster6)
deckOne.append(monster4)
deckOne.append(monster3)
deckOne.append(monster2)
deckOne.append(monster1)
random.shuffle(deckOne)

#Effect Cards
energyOne = DefenseCard(100,seventhImage,'Deep Freeze')
energyTwo = HealthCard(150,eigthImage,'Rainy Day')
energyThree = HealthCard(100,ninthImage,'Falling Tower')

defenseOne = DefenseCard(200,tenthImage,'Enchanted Eyes')
defenseTwo = DefenseCard(100,eleventhImage,'Ominous Spell')

healthOne = HealthCard(100,twelthImage,'Unite')

deckTwo = []
deckTwo.append(energyOne)
deckTwo.append(energyTwo)
deckTwo.append(energyThree)
deckTwo.append(defenseOne)
deckTwo.append(defenseTwo)
deckTwo.append(healthOne)
random.shuffle(deckTwo)

#Main Screen Player 1
monsterFrame1 = Frame(window)
monsterFrame1.grid(row=0,column=0)
monsterSelect1 = Button(monsterFrame1,image=blankImage,command=lambda : makeActive1())
monsterSelect1.pack(side='top')
monsterInfo1 = Button(monsterFrame1,text='info',command= lambda :displayInfo1(monsterCard1))
monsterInfo1.pack(side='top')

effectFrame1 = Frame(window)
effectFrame1.grid(row=0,column=1)
effectSelect1 = Button(effectFrame1,image=blankImage,command=lambda : useEffect1(effectCard1))
effectSelect1.pack(side="top")
effectInfo1 = Button(effectFrame1,text='info',command= lambda :displayInfo1(effectCard1))
effectInfo1.pack(side='top')

effectFrame2 = Frame(window)
effectFrame2.grid(row=1,column=0)
effectSelect2 = Button(effectFrame2,image=blankImage,command=lambda : useEffect1(effectCard2))
effectSelect2.pack(side="top")
effectInfo2 = Button(effectFrame2,text='info',command= lambda :displayInfo1(effectCard2))
effectInfo2.pack(side='top')

effectFrame3 = Frame(window)
effectFrame3.grid(row=1,column=1)
effectSelect3 = Button(effectFrame3,image=blankImage,command=lambda : useEffect1(effectCard3))
effectSelect3.pack(side="top")
effectInfo3 = Button(effectFrame3,text='info',command= lambda :displayInfo1(effectCard3))
effectInfo3.pack(side='top')

redraw1 = Button(window,text='Redraw',command=lambda : redrawOne())
redraw1.grid(row=2,column=0,sticky='E')

infoPanel1 = Text(window,width=15,height=10,wrap=WORD,background="white",fg="black")
infoPanel1.grid(row=0,column=2,sticky='S')

activeMonsterSlotFrame1 = Frame(window)
activeMonsterSlotFrame1.grid(row=0,column=3,sticky='S')
activeMonsterSlot1 = Label(activeMonsterSlotFrame1,image=blankImage)
activeMonsterSlot1.pack(side='top')
activeMonsterAttack1 = Button(activeMonsterSlotFrame1,text='Attack',command=lambda : attack1())
activeMonsterAttack1.pack(side='top')
activeMonsterInfo1 = Text(activeMonsterSlotFrame1,width=15,height=3,wrap=WORD,background="white",fg="black")
activeMonsterInfo1.pack(side='top')
endTurn1 = Button(activeMonsterSlotFrame1,text='End Turn',command=lambda : switch1(),state=DISABLED)
endTurn1.pack(side='top')

#Main Screen Player 2
monsterFrame2 = Frame(window)
monsterFrame2.grid(row=0,column=6)
monsterSelect2 = Button(monsterFrame2,image=blankImage,command=lambda : makeActive2())
monsterSelect2.pack(side='top')
monsterInfo2 = Button(monsterFrame2,text='info',command= lambda :displayInfo2(monsterCard2))
monsterInfo2.pack(side='top')

effectFrame4 = Frame(window)
effectFrame4.grid(row=0,column=7)
effectSelect4 = Button(effectFrame4,image=blankImage,command=lambda : useEffect2(effectCard4))
effectSelect4.pack(side="top")
effectInfo4 = Button(effectFrame4,text='info',command= lambda :displayInfo2(effectCard4))
effectInfo4.pack(side='top')

effectFrame5 = Frame(window)
effectFrame5.grid(row=1,column=6)
effectSelect5 = Button(effectFrame5,image=blankImage,command=lambda : useEffect2(effectCard5))
effectSelect5.pack(side="top")
effectInfo5 = Button(effectFrame5,text='info',command= lambda :displayInfo2(effectCard5))
effectInfo5.pack(side='top')

effectFrame6 = Frame(window)
effectFrame6.grid(row=1,column=7)
effectSelect6 = Button(effectFrame6,image=blankImage,command=lambda : useEffect2(effectCard6))
effectSelect6.pack(side="top")
effectInfo6 = Button(effectFrame6,text='info',command= lambda :displayInfo2(effectCard6))
effectInfo6.pack(side='top')

redraw2 = Button(window,text='Redraw',command=lambda : redrawTwo())
redraw2.grid(row=2,column=7,sticky='W')

infoPanel2 = Text(window,width=15,height=10,wrap=WORD,background="white",fg="black")
infoPanel2.grid(row=0,column=5,sticky='S')

activeMonsterSlotFrame2 = Frame(window)
activeMonsterSlotFrame2.grid(row=0,column=4,sticky='S')
activeMonsterSlot2 = Label(activeMonsterSlotFrame2,image=blankImage)
activeMonsterSlot2.pack(side='top')
activeMonsterAttack2 = Button(activeMonsterSlotFrame2,text='Attack',command=lambda : attack2())
activeMonsterAttack2.pack(side='top')
activeMonsterInfo2 = Text(activeMonsterSlotFrame2,width=15,height=3,wrap=WORD,background="white",fg="black")
activeMonsterInfo2.pack(side='top')
endTurn2 = Button(activeMonsterSlotFrame2,text='End Turn',state=DISABLED,command=lambda : switch2())
endTurn2.pack(side='top')

##run the main loop
window.mainloop()


