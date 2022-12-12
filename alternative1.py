import random

def makeChoice(omg, points):
    print("\n################")
    print("Omgång ", omg)
    print("Poäng: ", points)
    print("-------------------")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("-------------------")
    print('Gör ditt val (Q för att avsluta):')
    val = str(input())
    val = val.lower()
    return val
 

#######
## Start here
#########
omg = 0
points = 0
play = True

while play: 
    omg += 1
    val = makeChoice(omg, points)

    siffer_val = ['1','2','3']
    valen = ['rock', 'paper', 'scissors']
    datorns_val = random.choice(valen[:2])

    if val in siffer_val:
        val = valen[int(val)-1]

    if val in valen:
        print("Mitt val är", val)
        print("Datorns val är", datorns_val)
        if val == datorns_val:
            print('oavgjort')
        elif val == 'rock':
            if datorns_val == 'paper':
                print('Du förlorade ')
                points -= 1
            elif datorns_val == 'scissors':
                print('Du vann')
                points += 1
        elif val == 'paper':
            if datorns_val == 'scissors':
                print('Du förlorade')
                points -= 1
            elif datorns_val == 'rock':
                print('Du vann')
                points += 1
        elif val == 'scissors':
            if datorns_val == 'rock':
                print('Du förlorade')
                points += 1    
        elif datorns_val == 'paper':
            print('Du vann')
    elif val == 'q' or val == 'Q':
        play = False
    else:
        print('Du skrev in ett felaktigt val')
        print('Försök igen')
        omg -= 1

print('Spelet är slut!')
print('Du spelade ' + str(omg) + ' omgångar och fick ' + str(points) + ' poäng')
