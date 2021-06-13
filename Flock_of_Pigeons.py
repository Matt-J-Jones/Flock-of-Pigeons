import random
loop=True
def reset():
    gatheredfood=0
    pigeons=20
    chicks=10

def huntingforfood(number, location):
    global surv
    global dead
    global food
    surv=0
    food=0
    dead=0

    while number > 0:
        if location == "Trafalgar":
            result = random.randint(1,10)
            foodgathered=random.randint(0,1)
        elif location == "Hampstead":
            result = random.randint(1,6)
            foodgathered=random.randint(0,3)
        elif location == "Soho":
            result = random.randint(1,4)
            foodgathered=random.randint(0,5)

        if result <= 2:
            dead=dead+1
        else:
            surv=surv+1
            food=food+foodgathered
        number=number-1
    print(""" 
    """)
    print("You found",food,"Food!")
    print(surv, "pigeons survived")
    print(dead,"pigeons died")

def feedingpigeons(avaliblefood):
    global supplies
    global starved
    global chicks_starved
    chicks_starved=0
    starved = 0
    if avaliblefood > foodreq:
        supplies=gatheredfood-foodreq
        print(" ")
        print("You fed your pigeons!")
    else:
        print(" ")
        print("You can't feed all your pigeons!")
        starved=(foodreq-avaliblefood)//2
        starved=int(starved)
        if chicks > 0 and starved > 2:
            chicks_starved=starved//2

def tenpige():
    global pigeons
    global foodreq
    global loop
    global chicks
    chickcount=chicks
    if pigeons==1:
        foodreq=2
    else:
        foodreq=pigeons+((chickcount+1)//2)
        #foodreq=pigeons
    foodreq=int(foodreq)
    print("You have",pigeons,"pigeons, and",chicks,"chicks. You need at least",foodreq,"food")
    pigeonstosend=input("How many pigeons will you send to look for food? ")
    pigeonstosend=int(pigeonstosend)
    if pigeonstosend > pigeons:
        print("You don't have enough pigeons, max pigeons chosen")
        pigeonstosend=pigeons
    hunting_loc=input("""Enter hunting location number:

    [1] Trafalgar Square (Danger: LOW, Food Availability: LOW
    [2] Hampstead Heath (Danger MEDIUM, Food Availability: MEDIUM
    [3] Soho (Danger: HIGH, Food Availability: HIGH
    
    :""")

    if hunting_loc == 1:
        where_togo="Trafalgar"
    elif hunting_loc == 2:
        where_togo="Hampstead"
    else:
        where_togo="Soho"
    
    huntingforfood(pigeonstosend, where_togo)
    feedingpigeons(food)
    pigeons=(pigeons-pigeonstosend)+surv
    print("")
    print(pigeons,"Survived Hunting")
    print(starved, "Pigeons Starved to death")
    print(chicks_starved, "Chicks starved to death")
    chicks=chicks-chicks_starved
    if chicks < 0:
        chicks=0
    print("")
    pigeons=pigeons-starved
    if pigeons < 0:
        pigeons = 0
    print("You have",pigeons,"pigeons, and",chicks,"chicks remaining.")
    
    if pigeons > 0:
        loop=True
   
    else:
        if chicks > 0:
            print("With no pigeons left to find food, the remaining",chicks,"chicks starved to death.")
        loop=False

print("""

 __     __   ____    _    _                _____    ______                    
 \ \   / /  / __ \  | |  | |       /\     |  __ \  |  ____|           /\      
  \ \_/ /  | |  | | | |  | |      /  \    | |__) | | |__             /  \     
   \   /   | |  | | | |  | |     / /\ \   |  _  /  |  __|           / /\ \    
    | |    | |__| | | |__| |    / ____ \  | | \ \  | |____         / ____ \   
    |_|     \____/   \____/    /_/    \_\ |_|  \_\ |______|       /_/    \_\  
  ______     _           ____       _____     _  __       ____      ______    
 |  ____|   | |         / __ \     / ____|   | |/ /      / __ \    |  ____|   
 | |__      | |        | |  | |   | |        | ' /      | |  | |   | |__      
 |  __|     | |        | |  | |   | |        |  <       | |  | |   |  __|     
 | |        | |____    | |__| |   | |____    | . \      | |__| |   | |        
 |_|        |______|    \____/     \_____|   |_|\_\      \____/    |_|        
  _____      _____      _____     ______      ____      _   _      _____      
 |  __ \    |_   _|    / ____|   |  ____|    / __ \    | \ | |    / ____|     
 | |__) |     | |     | |  __    | |__      | |  | |   |  \| |   | (___       
 |  ___/      | |     | | |_ |   |  __|     | |  | |   | . ` |    \___ \      
 | |         _| |_    | |__| |   | |____    | |__| |   | |\  |    ____) |     
 |_|        |_____|    \_____|   |______|    \____/    |_| \_|   |_____/      
                                                                              
                                                                            """)

x=input("Press ENTER to play ")
reset()

#pigeons=input("Enter starting number of pigeons: ")
#pigeons=int(pigeons)

pigeons= 20
gatheredfood=0
remainingfood=0
chicks= 10

while loop:
    tenpige()
input("""

GAME OVER.

Press ENTER to quit.
""")