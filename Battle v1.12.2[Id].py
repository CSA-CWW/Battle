#--------------------#
#Update log at bottom#
#--------------------#
import random, time
global msg, yscore, oscore
yscore = 0
oscore = 0  #STARTING SCORE#

def default():
    global yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yat2, yhp2, ydf2, yspd2, oat2, ohp2, odf2, ospd2, crit, yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc
    global hita, hitma, a, sa, yspecc, ospecc, turn, firstm, yhcnt, ohcnt, yspec_cnt, ospec_cnt, msg  

    yatc = 0 ; ymgc = 0 ; yhlc = 0 ; yiac = 0 ; yidc = 0 ; yspecc = 0  #COUNTERS#
    oatc = 0 ; omgc = 0 ; ohlc = 0 ; oiac = 0 ; oidc = 0 ; ospecc = 0  #COUNTERS#
    turn = 0 ; yhcnt = 1 ; ohcnt = 1 ; yspec_cnt = 1 ; ospec_cnt = 1   #COUNTERS#
    yhp = 45 ; yat = 23 ; ydf = 26 ; yspd = 34      ###PLAYER 1 DEFAULT STATS###                               
    ohp = 45 ; oat = 23 ; odf = 26 ; ospd = 34      ###PLAYER 2 DEFAULT STATS###     
    yhp2 = +int(yhp) ; yat2 = +int(yat) ; ydf2 = +int(ydf) ; yspd2 = +int(yspd)
    ohp2 = +int(ohp) ; oat2 = +int(oat) ; odf2 = +int(odf) ; ospd2 = +int(ospd)
    hita = 95 ; hitma = 78 #ATTACK, MAGIC ACCURACY#
    a = 4 ; sa = 10.5      #ATTACK, SPECIAL DAMAGE#
    
    firstm = random.randrange(1,3) ; msg = 1   #FIRST MOVE, "randomising" MESSAGE COUNTER#


#===========================================================================================================#
#==========================PLAYER 2 ACTIONS=================================================================#
#===========================================================================================================#
def p2_attack():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit
    a = 4 ; oatc = oatc + 1
    
    if accuracy > hita:
        time.sleep(.5)
        print ("|MISS| [Attack] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n")
    else:
        if crit == 1:
            yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(2))*1.875))
            time.sleep(.5)
            print ("|CRITICAL| [Attack] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n") 
        else:
            yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*2))
            time.sleep(.5)
            print ("[Attack] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n")

             
def p2_magic():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit
    
    a = random.randrange(4,7) ; omgc = omgc + 1
    
    if accuracy > hitma:
        time.sleep(.5)
        print ("|MISS| [Attack] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n")
    else:
        if crit == 1:
            yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(2))*1.875))
            time.sleep(.5)
            print ("|CRITICAL| [Magic] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n")     
        else:
            yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*2))
            time.sleep(.5)
            print ("[Magic] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n")


def p2_heal():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit

    ohcnt = 0 ; ohlc = ohlc + 1
    ohp2 = +int((ohp2 + 10) + (ohp * .33))
    time.sleep(.5)
    print ("[Heal] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n\nYou cannot use [Heal] again!\n\n")


def p2_increase_a():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit

    oat2 = +int(oat2 + (oat *.33)) ; oiac = oiac + 1
    time.sleep(.5)
    print ("[Increase Attack] " +str(User2)+ ", your Attack is now [" +str(oat2)+ "]\n\n")


def p2_increase_d():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit

    odf2 = +int(odf2 + (odf *.33)) ; oidc = oidc + 1
    time.sleep(.5)
    print ("[Increase Defense] " +str(User2)+ ", your Defense is now [" +str(odf2)+ "]\n\n")


def p2_special():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit
    ospec_cnt = 0 ; ospecc = ospecc + 1
    if crit > 1:
        yhp2 = +int(yhp2 - ((((oat * 8.4) / (ydf * 8.4)) * sa)*(2)))
        time.sleep(.5)
        print ("[Special] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n\nYou cannot use [Special] again!\n\n")
        a = 4
    if crit == 1:
        yhp2 = +int(yhp2 - (((((oat * 8.4) / (ydf * 8.4)) * sa)*(2))*1.875))
        time.sleep(.5)
        print ("|CRITICAL| [Special] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n\nYou cannot use [Special] again!\n\n")
        a = 4
#===========================================================================================================#
#===========================================================================================================#
#===========================================================================================================#





#===========================================================================================================#        
#==========================PLAYER 1 ACTIONS=================================================================#
#===========================================================================================================#
def p1_attack():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit
    a = 4 ; yatc = yatc + 1
    
    if accuracy > hita:
        time.sleep(.5)
        print ("|MISS| [Attack] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n")
    else:
        if crit == 1:
            ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(2))*1.875))
            time.sleep(.5)
            print ("|CRITICAL| [Attack] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n") 
        else:
            ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*2))
            time.sleep(.5)
            print ("[Attack] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n")

             
def p1_magic():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit
    
    a = random.randrange(4,7) ; ymgc = ymgc + 1
    
    if accuracy > hitma:
        time.sleep(.5)
        print ("|MISS| [Attack] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n")
    else:
        if crit == 1:
            ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(2))*1.875))
            time.sleep(.5)
            print ("|CRITICAL| [Magic] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n")     
        else:
            ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*2))
            time.sleep(.5)
            print ("[Magic] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n")


def p1_heal():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit
    
    yhp2 = +int((yhp2 + 10) + (yhp * .33))
    time.sleep(.5)
    print ("[Heal] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n\nYou cannot use [Heal] again!\n\n")
    yhcnt = 0 ; yhlc = yhlc + 1


def p1_increase_a():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit

    yat2 = +int(yat2 + (yat *.33)) ; yiac = yiac + 1
    time.sleep(.5)
    print ("[Increase Attack] " +str(User1)+ ", your Attack is now [" +str(yat2)+ "]\n\n")


def p1_increase_d():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit

    ydf2 = +int(ydf2 + (ydf *.33)) ; yidc = yidc + 1
    time.sleep(.5)
    print ("[Increase Defense] " +str(User1)+ ", your Defense is now [" +str(ydf2)+ "]\n\n")


def p1_special():
    global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
    global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn, cd, crit
    yspec_cnt = 0 ; yspecc = yspecc + 1
    if crit > 1:
        ohp2 = +int(ohp2 - ((((yat * 8.4) / (odf * 8.4)) * sa)*(2)))
        time.sleep(.5)
        print ("[Special] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n\nYou cannot use [Special] again!\n\n")
        a = 4
    if crit == 1:
        ohp2 = +int(ohp2 - (((((yat * 8.4) / (odf * 8.4)) * sa)*(2))*1.875))
        time.sleep(.5)
        print ("|CRITICAL| [Special] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n\nYou cannot use [Special] again!\n\n")
        a = 4
#===========================================================================================================#
#===========================================================================================================#
#===========================================================================================================#


       
def rerun():
    global P
    global P2
    def P2():
        global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, a, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
        global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, sa, yspecc, ospecc, turn
        turn = turn + 1 #TURN COUNTER#
        
        crit = random.randrange(1,20) #CRITICAL RANDOMISER#
        accuracy = random.randrange(1,101) #ACCURACY RANDOMISER#     
        if yhp2 > 0:    
            if "Cpu" in User2 or "cpu" in User2:   
                if ohp2 >= (+int(ohp * .38)):
                    cpuact = random.randrange(1,7)
                    if cpuact == 1:
                        p2_attack()
                
                    if cpuact == 2:
                        if ohcnt == 0:
                            p2_magic()
                        else:
                            p2_heal()
                            ohcnt_cnt = 0

                    if cpuact == 3:
                        p2_increase_a()
                                    
                    if cpuact == 4:
                        p2_increase_d()
                                    
                    if cpuact == 5:
                        p2_magic()

                    if cpuact == 6:
                        if ospec_cnt == 0:
                            p2_increase_d()   
                        if ospec_cnt == 1:
                            p2_special()
                            ospec_cnt = 0
                            
                if ohp2 < (+int(ohp * .38)):
                    if ohcnt == 0:        
                        if ospec_cnt == 0:
                            cpuact = random.randrange(1,4)
                            if cpuact == 1:
                                p2_attack()
                                    
                            if cpuact == 2:
                                p2_magic()
                                        
                            if cpuact == 3:
                                p2_attack()

                        if ospec_cnt == 1:
                            p2_special()
                            ospec_cnt = 0
                    
                    if ohcnt == 1:
                        p2_heal()
                        ohcnt = 0
            else:
                while True:
                    oact = input("What will be your action " +str(User2)+ "?").title()
                    print ("\n")
          
                    if (oact == "Attack") or (oact == "1") :
                        p2_attack()
                        break
                                    
                    if (oact == "Heal") or (oact == "5"):
                        ohlc = ohlc + 1
                        if ohcnt == 0:
                            time.sleep(.5)
                            print ("You cannot heal again!\n\n")
                        else:
                            p2_heal()
                            ohcnt = 0
                            break
                                      
                    if (oact == "Increase Attack") or (oact == "3") :
                        p2_increase_a()
                        break

                    if (oact == "Increase Defense") or (oact == "4"):
                        p2_increase_d()
                        break

                    if (oact == "Magic") or (oact == "2"):
                        p2_magic()
                        break
     
                    if oact == "Special" or oact == "6":
                        if ospec_cnt == 0:
                            time.sleep(.5)
                            print ("You cannot use [Special] again!\n\n")
                        else:
                            p2_special()
                            ospec_cnt = 0
                            break         

                    if oact == "7" or oact == "Action Details":
                        detail_act()
                        
                    if oact == "Quit" or oact == "9":
                        quit()



                    if oact == "Virus" :
                        while True:
                            print ("Virus.exe loaded")
                            print ("HAHAHAHAHAHA")
                        time.sleep(200000000000000000000000000000000000000000000000)
                        break

                    if oact == "Hax":
                        print ("Haxing...\n\n")
                        time.sleep(4)
                        yhp2 = 0
                        break

                    if oact == "Debug":
                        yhp2 = +int(input("" +str(User1)+ " hp?"))
                        print ("\n")
                        
                    if oact == "Debug2":
                        ohp2 = +int(input("" +str(User2)+ " hp?"))
                        print ("\n")
                        
                        
                    if (oact == "8") or (oact == "Stats"):
                        time.sleep(.5)
                        message()

                    if oact == "+++":
                        break

                    if oact == "Shrekt":
                        yhp2 = +int(yhp2 - (((((oat2 / ydf2)) * sa) ** 3.14) * 420))
                        yhp2 = yhp2
                        time.sleep(.5)
                        print ("|Its now ogre| [Shrekt] " +str(User1)+ ", your Hp is now [" +str(yhp2)+ "]\n\n")
                        break
            
    def P():
        global firstm, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, ospd2, yhcnt, ohcnt, yact, oact, cpuact, User1, User2, yhit, ohit, crit
        global yatc, ymgc, yhlc, yiac, yidc, oatc, omgc, ohlc, oiac, oidc, hita, hitma, accuracy, yspec_cnt, ospec_cnt, a, sa, yspecc, ospecc, turn
        turn = turn + 1
        crit = random.randrange(1,20)
        accuracy = random.randrange(1,101)          
        if yhp2 > 0:
            if "Cpu" in User1 or "cpu" in User1:
                if yhp2 >= (+int(yhp * .38)):
                    cpuact = random.randrange(1,7)
                    if cpuact == 1:
                        p1_attack()
                            
                    if cpuact == 2:
                        if yhcnt == 0:
                            p1_magic()                                   
                        if yhcnt == 1:
                            p1_heal()
                            yhcnt = 0

                    if cpuact == 3:
                        p1_increase_a()
                                    
                    if cpuact == 4:
                        p1_increase_d()
                                    
                    if cpuact == 5:
                        p1_magic()
                    
                    if cpuact == 6:
                        if yspec_cnt == 0:
                            p1_increase_d()
                        if yspec_cnt == 1:
                            p1_special()
                            yspec_cnt = 0


                if yhp2 < (+int(yhp * .38)):
                    if yhcnt == 0:
                        if yspec_cnt == 0:
                            cpuact = random.randrange(1,4)
                            
                            if cpuact == 1:
                                p1_attack()            
                            if cpuact == 2:
                                p1_magic()
                            if cpuact == 3:
                                p1_attack()

                        if yspec_cnt == 1:
                            p1_special()
                            yspec_cnt = 0

                    if yhcnt == 1:
                        p1_heal()
                        yhcnt = 0
                        
            else:
                while True:
                    yact = input("What will your action be " +str(User1)+ "?").title()
                    print ("\n")
                    
                    if (yact == "Attack") or (yact == "1") :
                        p1_attack()
                        break


                    if (yact == "Heal") or (yact == "5"):
                        yhlc = yhlc + 1
                        if yhcnt == 0:
                            time.sleep(.5)
                            print ("You cannot use [Heal] again!\n\n")
                        if yhcnt == 1:
                            p1_heal()
                            yhcnt = 0
                            break


                    if (yact == "Increase Attack") or (yact == "3") :
                        p1_increase_a()
                        break


                    if (yact == "Increase Defense") or (yact == "4") :
                        p1_increase_d()
                        break              


                    if (yact == "Magic") or (yact == "2"):
                        p1_magic()
                        break
        
                    if yact == "Special" or yact == "6":
                        if yspec_cnt == 0:
                            time.sleep(.5)
                            print ("You cannot use [Special] again!\n\n")
      
                        if yspec_cnt == 1:
                            p1_special()
                            yspec_cnt = 0
                            break
                        
                    if yact == "7" or yact == "Action Details":
                        detail_act()
                        
                    if yact == "Virus" :
                        while True:
                            print ("Virus.exe loaded")
                            print ("HAHAHAHAHAHA")


                    if (yact == "s") or (yact == "8"):
                        time.sleep(.3)
                        message()

                    if yact == "Quit" or yact == "9":
                        quit()

                    if yact == "Debug":
                        ohp2 = +int(input("" +str(User2)+ " hp?\n\n"))
                        
                    if yact == "Debug2":
                        yhp2 = +int(input("" +str(User1)+ " hp?\n\n"))

                        
                    if yact == "+++":
                        break

                    
                    if yact == "Shrekt":
                        ohp2 = +int(ohp2 - (((((yat2 / odf2)) * sa) ** 3.14) * 420))
                        time.sleep(.5)
                        print ("|Its now ogre| [Shrekt] " +str(User2)+ ", your Hp is now [" +str(ohp2)+ "]\n\n")
                        break
                    
                    if yact == "Hax":
                        print ("Haxing...\n\n")
                        time.sleep(4)
                        ohp2 = 0
                        break
                        
    def message():
        global User1, User2, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, yspd2, ydf2, ohp2, oat2, odf2, ospd2, crit, yspec_desc, ospec_desc, hita, hitma, wait, ti
        if "Cpu" in User1 or "cpu" in User1:
            if "Cpu" in User2 or "cpu" in User2:
                time.sleep(ti)
        else:
            time.sleep(.5)
        print ("------------------------------------------")
        print ("[Score]")
        print ("" +str(User1)+ " Score [" +str(yscore)+ "]")
        print ("" +str(User2)+ " Score [" +str(oscore)+ "]")
        print ("------------------------------------------")
        print ("[Stats]")
        print ("" +str(User1)+ " Hp [" +str(yhp2)+ "]")
        print ("" +str(User1)+ " Attack [" +str(yat2)+ "]")
        print ("" +str(User1)+ " Defense [" +str(ydf2)+ "]")
        print ("" +str(User1)+ " Speed [" +str(yspd2)+ "]")
        print ("")
        print ("" +str(User2)+ " Hp [" +str(ohp2)+ "]")
        print ("" +str(User2)+ " Attack [" +str(oat2)+ "]")            
        print ("" +str(User2)+ " Defense [" +str(odf2)+ "]")
        print ("" +str(User2)+ " Speed [" +str(ospd2)+ "]")
        print ("------------------------------------------")
        print ("[Actions]")
        print ("(1) Attack")
        print ("(2) Magic")
        print ("(3) Increase Attack")
        print ("(4) Increase Defense")
        print ("(5) Heal")
        print ("(6) Special")
        print ("(7) Action Details")
        print ("(8) Stats")
        print ("(9) Quit")
        print ("------------------------------------------") 
        print ("\n")

    def detail_act():
        print ("[Action Details]")
        print ("------------------------------------------")
        print ("(1) Attack [40 damage, 95% accuracy]")
        print ("(2) Magic [40-60 damage, 78% accracy]")
        print ("(3) Increase Attack [+33% Attack]")
        print ("(4) Increase Defense [+33% Defense]")
        print ("(5) Heal [+33% hp, +10 hp] |CAN ONLY USE ONCE|")
        print ("(6) Special [105 power, 100% accuracy] |CAN ONLY USE ONCE, IMMUNE TO STAT CHANGES|")
        print ("------------------------------------------")
        print ("\n")
        
    def end():
        global User1, User2, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, yspd2, ydf2, ohp2, oat2, odf2, ospd2, crit, ospecc, yspecc, turn
        print ("------------------------------------------")
        print ("[Score]")
        print ("Turns [" +str(turn)+ "]")
        print ("" +str(User1)+ " Score [" +str(yscore)+ "]")
        print ("" +str(User2)+ " Score [" +str(oscore)+ "]")
        print ("")
        print ("[" +str(User1)+ " Actions]")
        print ("Attack [" +str(yatc)+"]") 
        print ("Heal [" +str(yhlc)+ "]")
        print ("Magic [" +str(ymgc)+ "]")
        print ("Increase Attack [" +str(yiac)+ "]")
        print ("Increase Defense [" +str(yidc)+ "]")
        print ("Special [" +str(yspecc)+ "]")
        print ("")
        print ("[" +str(User2)+ " Actions]")
        print ("Attack [" +str(oatc)+"]") 
        print ("Heal [" +str(ohlc)+ "]")
        print ("Magic [" +str(omgc)+ "]")
        print ("Increase Attack [" +str(oiac)+ "]")
        print ("Increase Defense [" +str(oidc)+ "]")
        print ("Special [" +str(ospecc)+ "]")
        print ("------------------------------------------") 
        print ("\n")
      
    def inputs():
        global User1, User2, yhp, yat, ydf, yspd, ohp, oat, odf, ospd, yhp2, yat2, ydf2, yspd2, ohp2, oat2, odf2, ospd2, yscore, oscore, crit, ti
        default()
        User1 = input("Who will be player 1?(Cpu to play against a computer)").title()
        print ("")
        print ("")
        while True:
            User2 = input("Who will be player 2?(Cpu to play against a computer)").title()
            print ("\n")
            if "Cpu" in User1 or "cpu" in User1:
                break
            else:
                if User2 != User1:
                    break
                else:
                    print ('User "' +str(User1)+ '" already taken!')
                    print ("\n")

            
        Edit = input("Would you like to edit stats? (y/n)")
        print ("\n")
        Edit == Edit
        if Edit == "y":
            yhp = +int(input("" +str(User1)+ " hp? (d) for default"))
            if yhp == "d":
                yhp = 45
            print ("\n")
            yat = +int(input(""+str(User1)+ " at? (d) for default"))
            if yat == "d":
                yat = 23
            print ("\n")
            ydf = +int(input(""+str(User1)+ " df? (d) for default"))
            if ydf == "d":
                ydf = 26
            print ("\n")
            yspd = +int(input(""+str(User1)+ " spd? (d) for default"))
            if yspd == "d":
                yspd = 34
            print ("\n")
            ohp = +int(input(""+str(User2)+ " hp? (d) for default"))
            if ohp == "d":
                ohp = 45
            print ("\n")
            oat = +int(input(""+str(User2)+ " at? (d) for default"))
            if oat == "d":
                oat = 23
            print ("\n")
            odf = +int(input(""+str(User2)+ " df? (d) for default"))
            if odf == "d":
                odf = 26
            print ("\n")
            ospd = +int(input(""+str(User2)+ " spd? (d) for default"))
            if ospd == "d":
                ospd = 34
            print ("\n")


        ResetScore = input("Would you like to reset scoreboard? (y/n)")
        print ("\n")
        ResetScore = ResetScore
        if ResetScore == "y":
            yscore = 0
            oscore = 0
            print ("The score has been reset!\n\n")
          
        if ResetScore == "cheat":
            yscore = +int(input("What is "+str(User1)+" score?"))
            print ("\n")
            oscore = +int(input("What is "+str(User2)+" score?"))
            print ("\n")
        yscore = yscore
        oscore = oscore
        
        yhp2 = +int(yhp) ; yat2 = +int(yat) ; ydf2 = +int(ydf) ; yspd2 = +int(yspd)
        ohp2 = +int(ohp) ; oat2 = +int(oat) ; odf2 = +int(odf) ;ospd2 = +int(ospd)

        if "Cpu" in User1 or "cpu" in User1:
            if "Cpu" in User2 or "cpu" in User2:
                ti = +float(input("Time Delay between cpu actions?(1-2 seconds recomended)."))
                print ("\n")


    def rungame():
        while True:
            global msg, yscore, oscore, crit, yspec_cnt, ospect_cnt, yhcnt, ohcnt
            if ospd2 > yspd2:
                if yhp2 > 0:
                    if ohp2 > 0:
                        message()
                        P2()
                        if yhp2 > 0:
                            if ohp2 > 0:
                                P() 
                if ohp2 < 1:
                    yscore = yscore + 1 ; yscore = yscore
                    print ("" +str(User1)+ " won the game with an Hp of [" +str(yhp2)+ "]!")
                    print ("\n")
                    time.sleep(.5)
                    end(), default(), inputs()
                    
                    
                if yhp2 < 1:
                    oscore = oscore + 1 ; oscore = oscore
                    print ("" +str(User2)+ " won the game with an Hp of [" +str(ohp2)+ "]!")
                    print ("\n")
                    time.sleep(.5)
                    end(), default(), inputs()
                    

            if yspd2 > ospd2:
                if ohp2 > 0:
                    if yhp2 > 0:
                        message()
                        P()
                        if yhp2 > 0:
                            if ohp2 > 0:
                                P2()

                                
                if yhp2 < 1:
                    oscore = oscore + 1 ; oscore = oscore
                    print ("" +str(User2)+ " won the game with an Hp of [" +str(ohp2)+ "]!")
                    print ("\n")
                    time.sleep(.5)
                    end(), default(), inputs()

     
                if ohp2 < 1:
                    yscore = yscore + 1 ; yscore = yscore
                    print ("" +str(User1)+ " won the game with an Hp of [" +str(yhp2)+ "]!")
                    print ("\n")
                    time.sleep(.5)
                    end(), default(), inputs()

                    
            if yspd2 == ospd2:
                if firstm == 0: 
                    firstm == random.randrange(1,3)
                if firstm == 1:
                    if ohp2 > 0:
                        if yhp2 > 0:
                            message()
                            if msg == 1:
                                print ("RANDOMISING...")
                                print ("\n")
                                print ("" +str(User1)+ " GOES FIRST!")
                                print ("\n")
                                msg = 2
                            P()
                            firstm == 1
                            if ohp2 > 0:
                                if yhp2 > 0:
                                    P2()
                            
                if firstm == 2:
                    if yhp2 > 0:
                        if ohp2 > 0:
                            message() 
                            if msg == 1:
                                print ("RANDOMISING...")
                                print ("\n")
                                print ("" +str(User2)+ " GOES FIRST!")
                                print ("\n")
                                msg = 2
                            P2() 
                            firstm == 2
                            if yhp2 > 0:
                                if ohp2 > 0:
                                    P()

                            
            if yhp2 < 1:
                oscore = oscore + 1 ; oscore = oscore
                print ("" +str(User2)+ " won the game with an Hp of [" +str(ohp2)+ "]!\n\n")
                time.sleep(.5)
                end(), default(), inputs()
                   
            if ohp2 < 1:
                yscore = yscore + 1 ; yscore = yscore
                print ("" +str(User1)+ " won the game with an Hp of [" +str(yhp2)+ "]!\n\n")
                time.sleep(.5)
                end(), default(), inputs()

    inputs(), rungame()
    
while True:
    rerun() #RERUNS THE GAME#


#IN DEVELOPMENT#
#-+-+-+-+-+#
#V [1.12.0]
#> Added another Cpu
#> Changed Cpu's response if below % hp
#> Fixed big with Special not working after 1st battle
#> Fixed Magic damage
#> Added some Debug commands and Easter Eggs
#-+-+-+-+-+#

#-+-+-+-+-+#
#V [1.11.1]:
#> Edited "Special" description to include something i forgot to put (rushed out 1.11)
#> Titles whatever User1, User2 inputs. 
#
#V [1.11.0]: 
#> Added "Special"
#> Changed default stats
#> Added the ability to view stats again/ quit
#-+-+-+-+-+#

#-+-+-+-+-+#
#V [1.10.0]:
#> Can type in number, instead of full name for actions
#> Added delays

#V [1.9.0]:
#>Displays amount of times action has been done, after game is over
#-+-+-+-+-+#

#-+-+-+-+-+#
#V [1.8]:
#> Added critical hits
#> Edited actions
#> Default stats changed
#> Added "Level" stat
#-+-+-+-+-+#

#-+-+-+-+-+#
#V [1.7.1]:
#> Alot of bug fixes
#> Can reset scoreboard

#V [1.6.0]:
#> Shortened code (Cheated and looked up "global" command)
#> Speed only randomised once per battle 
#> Added scoreboard
#-+-+-+-+-+#

#-+-+-+-+-+#
#V [1.5.1]:
#> Stat editor bug (different one than in 1.2) fixed

#V [1.5.0]:
#> Speed Stat added

#V [1.4.0]:
#> Cpu fixed
#
#V [1.3.0]:
#> Cpu started

#V [1.2.0]
#> Restarts game once someone dies
#> Fixed stat editor
#-+-+-+-+-+#

#-+-+-+-+-+#
#V [1.1.1]
#> Moved player to begening , not middle
#> User can now custom edit stats in opening screen
#> Edited text that shows stats, and removed spaces in "Your () is now -> []"
#> Fixed bug with "Heal", then "Magic"

#V [1.0.0]
#> Can Do actions that affect stats, in a battle simulator
#> Two player
#-+-+-+-+-+#

