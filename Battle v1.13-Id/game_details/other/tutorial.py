import time
def run():
    global brk
    brk = 0
    def check():
        global brk
        while True:
            resume = input(">> [c] to continue, [q] to quit.").title()
            print ("\n")
            if resume == "Q":
                brk = 1
                break
            if resume != "C" and resume != "Q":
                print ('> Unknown input "' +str(resume)+ '"!\n\n')
            else:
                brk = 0
                break
    if brk == 0:
        print ("> Hello, and welcome to Battle v1.13[Id]!\n\n") , time.sleep(4)
        print ("> In this game, your goal is to K.O the opponet in a turn based battle simulator.\n\n") , time.sleep(1)
        check()
    if brk == 0:
        print ("> There are different classes you can choose from, each with different stats and actions.\n\n"), time.sleep(4) 
        print ("==========================================") , time.sleep(.2)
        print ("[Stats]") , time.sleep(.2)
        print ("  [Tutorial] Bob:")
        print ("    > Hp [45]") , time.sleep(.2)
        print ("    > Attack [32]") , time.sleep(.2)
        print ("    > Defense [34]") , time.sleep(.2)
        print ("    > Speed [26]") , time.sleep(.2)
        print ("")
        print ("  [Tutorial] Billy:")
        print ("    > Hp [45]") , time.sleep(.2)
        print ("    > Attack [32]") , time.sleep(.2)
        print ("    > Defense [34]") , time.sleep(.2)
        print ("    > Speed [26]") , time.sleep(.2)
        print ("==========================================") , time.sleep(.2)
        print ("[Actions]") , time.sleep(.2)
        print ("  Bob:")
        print ("    > (1) Attack") , time.sleep(.2)
        print ("    > (2) Magic") , time.sleep(.2)
        print ("    > (3) Increase Attack") , time.sleep(.2)
        print ("    > (4) Increase Defense") , time.sleep(.2)
        print ("    > (5) Heal") , time.sleep(.2) 
        print ("    > (6) Special") , time.sleep(.2)
        print ("")
        print ("  Billy:")
        print ("    > (1) Attack") , time.sleep(.2)
        print ("    > (2) Magic") , time.sleep(.2)
        print ("    > (3) Increase Attack") , time.sleep(.2)
        print ("    > (4) Increase Defense") , time.sleep(.2)
        print ("    > (5) Heal") , time.sleep(.2) 
        print ("    > (6) Special") , time.sleep(.2)
        print ("==========================================\n\n") , time.sleep(1)
        check()
    if brk == 0:
        print ("> Each of these actions have an effect on stats.\n\n") , time.sleep(4)
        print ("==========================================") , time.sleep(.2)
        print ("[Action Details]") , time.sleep(.2)
        print ("    > (1) Attack [40 damage, 95% accuracy]") , time.sleep(.2)
        print ("    > (2) Magic [40-60 damage, 78% accracy]") , time.sleep(.2)
        print ("    > (3) Increase Attack [+33% Attack]") , time.sleep(.2)
        print ("    > (4) Increase Defense [+33% Defense]") , time.sleep(.2)
        print ("    > (5) Heal [+33% hp, +10 hp, CAN ONLY USE ONCE]") , time.sleep(.2)
        print ("    > (6) Special [105 power, 100% accuracy, CAN ONLY USE ONCE, IMMUNE TO STAT CHANGES]") , time.sleep(.2)
        print ("==========================================\n\n") , time.sleep(1)
        check()
    if brk == 0:
        print ("> When someone runs out of Hp, the game restarts.\n\n"), time.sleep(2)
