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
  
def check_vinst(val, datorns_val):
    match val:
        case 'rock':
            match datorns_val:
                case 'rock': return 0
                case 'paper': return -1
                case 'scissors': return 1
        case 'paper':
            match datorns_val:
                case 'rock': return 1
                case 'paper': return 0
                case 'scissors': return -1
        case 'scissors':
            match datorns_val:
                case 'rock': return -1
                case 'paper': return 1
                case 'scissors': return 0  

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
        point = check_vinst(val, datorns_val)
        if point == 0:
           print("Oavgjort")
        elif point == 1:
            print("Du vann")           
        else:
            print("Du förlorade")
        points = points + point
    elif val == 'q' or val == 'Q':
        play = False
    else:
        print('Du skrev in ett felaktigt val')
        print('Försök igen')
        omg -= 1               


print('Spelet är slut!')
print('Du spelade ' + str(omg) + ' omgångar och fick ' + str(points) + ' poäng')

