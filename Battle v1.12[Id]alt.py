#--------------------#
#Update log at bottom#
#--------------------#


import random 
import time
global msg 
msg = 1

def default():
    global yhp 
    global yat
    global ydf 
    global yspd 
    global ohp 
    global oat 
    global odf
    global ospd
    global yat2
    global yhp2
    global ydf2
    global yspd2
    global oat2
    global ohp2
    global odf2
    global ospd2
    global yl
    global ol
    global yl2
    global ol2
    global crit
    global yatc
    global ymgc
    global yhlc
    global yiac
    global yidc
    global oatc
    global omgc
    global ohlc
    global oiac
    global oidc
    global yspec_desc
    global ospec_desc
    global hita
    global hitma
    global sa
    global yspecc
    global ospecc


    hita = 95
    hitma = 78

    
    yatc = 0
    ymgc = 0
    yhlc = 0
    yiac = 0
    yidc = 0
    oatc = 0
    omgc = 0
    ohlc = 0
    oiac = 0
    oidc = 0
    yspecc = 0
    ospecc = 0

    
    yspec_desc = "105 power, immune to stat changes, CAN ONLY USE ONCE"
    ospec_desc = "105 power, immune to stat changes, CAN ONLY USE ONCE"

    
    yhp = 45 #user 1 default Hp#
    yat = 23 #user 1 default Attack#
    ydf = 26 #user 1 default Defense#
    yspd = 34 #user 1 default Speed#
    yl = 10

    ohp = 45 #user 2 default Hp#
    oat = 23 #user 2 default Attack#
    odf = 26 #user 2 default Defense#
    ospd = 34 #user 2 default speed
    ol = 10 #user 2 default level#


    yat2 = yat
    yhp2 = yhp
    ydf2 = ydf
    yspd2 = yspd
    yl2 = yl

    oat2 = oat
    ohp2 = ohp
    odf2 = odf
    ospd2 = ospd
    ol2 = ol

    yhp = +int(yhp)
    yat = +int(yat)
    ydf = +int(ydf)
    yspd = +int(yspd)
    yl = +int(yl)
    
    ohp = +int(ohp)
    oat = +int(oat)
    odf = +int(odf)
    ospd = +int(ospd)
    ol = +int(ol)
    
    yhp2 = +int(yhp)
    yat2 = +int(yat)
    ydf2 = +int(ydf)
    yspd2 = +int(yspd)
    yl2 = +int(yl2)
    
    ohp2 = +int(ohp)
    oat2 = +int(oat)
    odf2 = +int(odf)
    ospd2 = +int(ospd)
    ol2 = +int(ol2)



global firstm
firstm = random.randrange(1,3)



global a
a = 4   #Default Attack power#
        #Example -> "a = 4" = 40#
sa = 10.5




global yhcnt
yhcnt = 1
global ohcnt
ohcnt = 1
global yspec_cnt
yspec_cnt = 1
global ospec_cnt
ospec_cnt = 1



global yscore
yscore = 0
global oscore
oscore = 0


def rerun():
    global P
    global P2
    def P2():
        global firstm
        global yhp
        global yat
        global ydf
        global yspd
        global ohp
        global oat
        global odf
        global ospd
        global yhp2
        global yat2
        global ydf2
        global yspd2
        global ohp2
        global oat2
        global odf2
        global ospd2
        global a
        global yl
        global ol
        global yl2
        global ol2
        global yhcnt
        global ohcnt
        global yact
        global oact
        global cpuact
        global User2
        global yhit
        global ohit
        global crit
        global yatc
        global ymgc
        global yhlc
        global yiac
        global yidc
        global oatc
        global omgc
        global ohlc
        global oiac
        global oidc
        global hita
        global hitma
        global acurracy
        global yspec_cnt
        global ospec_cnt
        global sa
        global yspecc
        global ospecc

        
        crit = random.randrange(1,20)
        crit = random.randrange(21,100)
        crit = random.randrange(1,20)
        accuracy = random.randrange(2,69)
        accuracy = random.randrange(1,101)
        
        if yhp2 > 0:    
            if "Cpu" in User2 or "cpu" in User2:   
                if ohp2 >= (+int(ohp * .38)):
                    cpuact = random.randrange(7,100)
                    cpuact = random.randrange(1,7)
                    if cpuact == 1:
                        oatc = oatc + 1
                        oatc = oatc
                        if accuracy > hita:
                            yhp2 = yhp2
                            print ("|MISS| [Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                            print ("")
                            print ("")
                        else: 
                            if crit > 1:
                                yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5)))
                                time.sleep(.5)
                                print ("[Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                print ("")
                                print ("")

                            if crit == 1:
                                yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                print ("")
                                print ("")
                            


                                
                    if cpuact == 2:
                        if ohcnt == 0:
                            omgc = omgc + 1
                            omgc = omgc
                            if accuracy > hitma:
                                yhp2 = yhp2
                                time.sleep(.5)
                                print ("|MISS| [Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                print ("")
                                print ("")
                            else:
                                if crit > 1:
                                    a = random.randrange(4, 7)
                                    yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5)))
                                    time.sleep(.5)
                                    print ("[Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                    a = 4
                                    print ("")
                                    print ("")
                                    
                 
                                if crit == 1:
                                    a = random.randrange(4, 7)
                                    yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5))*1.875))
                                    time.sleep(.5)
                                    print ("|CRITICAL| [Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                    a = 4
                                    print ("")
                                    print ("")
                                

                                
                                
                        if ohcnt == 1:
                            ohp2 = +int((ohp2 + 10) + (ohp * .33))
                            time.sleep(.5)
                            print ("[Heal] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                            ohp2 = ohp2
                            print ("")
                            print ("") 
                            print ("You cannot heal again!")
                            print ("")
                            print ("")
                            ohcnt = 0
                            ohlc = ohlc + 1
                            ohlc = ohlc

                            
            
                    if cpuact == 3:
                        oat2 = +int(oat2 + (oat *.33))
                        time.sleep(.5)
                        print ("[Increase Attack] " +str(User2)+ ", your Attack is now -> [" +str(oat2)+ "]")
                        oat2 = oat2
                        print ("")
                        print ("")
                        oiac = oiac + 1
                        oiac = oiac
                                    


                    if cpuact == 4:
                        odf2 = +int(odf2 + (odf * .33))
                        time.sleep(.5)
                        print ("[Increase Defense] " +str(User2)+ ", your Defense is now -> [" +str(odf2)+ "]")
                        odf2 = odf2
                        print ("")
                        print ("")
                        oidc = oidc + 1
                        oidc = oidc
                                    


                    if cpuact == 5:
                        omgc = omgc + 1
                        omgc = omgc
                        if accuracy > hitma:
                            yhp2 = yhp2
                            time.sleep(.5)
                            print ("|MISS| [Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                            print ("")
                            print ("")
                        else:
                            if crit > 1:
                                a = random.randrange(4, 7)
                                yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5)))
                                time.sleep(.5)
                                print ("[Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                
                            if crit == 1:
                                a = random.randrange(4, 7)
                                yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                    
                    a = a
                    if cpuact == 6:
                        if ospec_cnt == 0:
                            odf2 = +int(odf2 + (odf * .33))
                            time.sleep(.5)
                            print ("[Increase Defense] " +str(User2)+ ", your Defense is now -> [" +str(odf2)+ "]")
                            odf2 = odf2
                            print ("")
                            print ("")
                            oidc = oidc + 1
                            oidc = oidc
                            
                        if ospec_cnt == 1:
                            ospec_cnt = 0
                            ospecc = ospecc + 1
                            if crit > 1:
                                yhp2 = +int(yhp2 - ((((oat * 8.4) / (ydf * 8.4)) * sa)*(ol2 / 5)))
                                time.sleep(.5)
                                print ("[Special] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                            if crit == 1:
                                yhp2 = +int(yhp2 - (((((oat * 8.4) / (ydf * 8.4)) * sa)*(ol2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Special] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")                            
                    a = a 


                        
                if ohp2 < (+int(ohp * .38)):
                    if ohcnt == 0:        
                        if ospec_cnt == 0:
                            cpuact = random.randrange(1,4)
                            if cpuact == 1:
                                oatc = oatc + 1
                                oatc = oatc
                                if accuracy > hita:
                                    yhp2 = yhp2
                                    time.sleep(.5)
                                    print ("|MISS| [Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                    print ("")
                                    print ("")
                                else:
                                    if crit > 1:
                                        yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5)))
                                        time.sleep(.5)
                                        print ("[Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                        print ("")
                                        print ("")
                                    if crit == 1:
                                        yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5))*1.875))
                                        time.sleep(.5)
                                        print ("|CRITICAL| [Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                        print ("")
                                        print ("")
                                    
                            if cpuact == 2:
                                omgc = omgc + 1
                                omgc = omgc
                                a = random.randrange(4, 7)
                                if accuracy > hitma:
                                    yhp2 = yhp2
                                    time.sleep(.5)
                                    print ("|MISS| [Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                    print ("")
                                    print ("")
                                else:
                                    if crit > 1:
                                        yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5)))
                                        time.sleep(.5)
                                        print ("[Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                        a = 4
                                        print ("")
                                        print ("")
                                    if crit == 1:
                                        yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5))*1.875))
                                        time.sleep(.5)
                                        print ("|CRITICAL| [Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                        a = 4
                                        print ("")
                                        print ("")
                                        
                            if cpuact == 3:
                                oatc = oatc + 1
                                oatc = oatc
                                if accuracy > hita:
                                    yhp2 = yhp2
                                    time.sleep(.5)
                                    print ("|MISS| [Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                    print ("")
                                    print ("")
                                else:
                                    if crit > 1:
                                        yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5)))
                                        time.sleep(.5)
                                        print ("[Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                        print ("")
                                        print ("")
                                    if crit == 1:
                                        yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5))*1.875))
                                        time.sleep(.5)
                                        print ("|CRITICAL| [Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                        print ("")
                                        print ("")        
                        a = a

                        if ospec_cnt == 1:
                            ospec_cnt = 0
                            ospecc = ospecc + 1
                            if crit > 1:
                                yhp2 = +int(yhp2 - ((((oat * 8.4) / (ydf * 8.4)) * sa)*(ol2 / 5)))
                                time.sleep(.5)
                                print ("[Special] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                            if crit == 1:
                                yhp2 = +int(yhp2 - (((((oat * 8.4) / (ydf * 8.4)) * sa)*(ol2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Special] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                   
                    if ohcnt == 1:
                        ohlc = ohlc + 1
                        ohlc = ohlc
                        ohp2 = +int((ohp2 + 10) + (ohp * .33))
                        time.sleep(.5)
                        print ("[Heal] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                        ohp2 = ohp2
                        print ("")
                        print ("")
                        print ("You cannot heal again!")
                        print ("")
                        print ("")
                        ohcnt = 0

                        
        

            else:
                while True:
                    oact = input("What will be your action " +str(User2)+ "?").title()
                    print ("")
                    print ("")

                        
                    if (oact == "Attack") or (oact == "1") :
                        oatc = oatc + 1
                        oatc = oatc
                        if accuracy > hita:
                            yhp2 = yhp2
                            time.sleep(.5)
                            print ("|MISS| [Attack] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                            print ("")
                            print ("")
                            break
                        else:
                            if crit > 1:
                                yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5)))
                                time.sleep(.5)
                                print ("[Attack] " +str(User1)+ ", your Hp is now ->","["+str(yhp2)+"]")
                                print ("")
                                print ("")
                                break
                            if crit == 1:
                                yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Attack] " +str(User1)+ ", your Hp is now ->","["+str(yhp2)+"]")
                                print ("")
                                print ("")
                                break
                                    


                    if (oact == "Heal") or (oact == "5"):
                        ohlc = ohlc + 1
                        ohlc = ohlc
                        if ohcnt == 0:
                            time.sleep(.5)
                            print ("You cannot heal again!")
                            print ("")
                            print ("")
                        if ohcnt == 1:
                            ohp2 = +int((ohp2 + 10) + (ohp * .33))
                            time.sleep(.5)
                            print ("[Heal] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                            ohp2 = ohp2
                            ohcnt = 0
                            print ("")
                            print ("")
                            print ("You cannot heal again!")
                            print ("")
                            print ("")
                            break
                              

                             
                    if (oact == "Increase Attack") or (oact == "3") :
                        oiac = oiac + 1
                        oiac = oiac
                        oat2 = +int(oat2 + (oat * .33))
                        time.sleep(.5)
                        print ("[Increase Attack] " +str(User2)+ ", your Attack is now -> [" +str(oat2)+ "]")
                        oat2 = oat2
                        print ("")
                        print ("")
                        break



                    if (oact == "Increase Defense") or (oact == "4"):
                        oidc = oidc + 1
                        oidc = oidc
                        odf2 = +int(odf2 + (odf * .33))
                        time.sleep(.5)
                        print ("[Increase Defense] " +str(User2)+ ", your Defense is now -> [" +str(odf2)+ "]")
                        odf2 = odf2
                        print ("")
                        print ("")
                        break



                    if (oact == "Magic") or (oact == "2"):
                        omgc = omgc + 1
                        omgc = omgc
                        if accuracy > hitma:
                            yhp2 = yhp2
                            time.sleep(.5)
                            print ("|MISS| [Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                            print ("")
                            print ("")
                            break
                        else:
                            if crit > 1:
                                a = random.randrange(4, 7)
                                yhp2 = +int(yhp2 - ((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5)))
                                time.sleep(.5)
                                print ("[Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                break
                            if crit == 1:
                                a = random.randrange(4, 7)
                                yhp2 = +int(yhp2 - (((((oat2 * 8.4) / (ydf2 * 8.4)) * a)*(ol2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Magic] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                break


                            
                    if oact == "Special" or oact == "7":
                        if ospec_cnt == 0:
                            time.sleep(.5)
                            print ("You cannot use [Special] again!")
                            print ("")
                            print ("")
                            
                        if ospec_cnt == 1:
                            ospec_cnt = 0
                            ospecc = ospecc + 1
                            if crit > 1:
                                yhp2 = +int(yhp2 - ((((oat * 8.4) / (ydf * 8.4)) * sa)*(ol2 / 5)))
                                time.sleep(.5)
                                print ("[Special] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                print ("You cannot use [Special] again!")
                                print ("")
                                print ("")
                                break
                            if crit == 1:
                                yhp2 = +int(yhp2 - (((((oat * 8.4) / (ydf * 8.4)) * sa)*(ol2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Special] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                print ("You cannot use [Special] again!")
                                print ("")
                                print ("")
                                break
                        
                    a = a

                    if oact == "Quit" or oact == "9":
                        quit()



                    if oact == "Virus" :
                        while True:
                            print ("Virus.exe loaded")
                            print ("HAHAHAHAHAHA")
                        time.sleep(200000000000000000000000000000000000000000000000)
                        break

                    if oact == "Hax":
                        print ("Haxing...")
                        print ("")
                        print ("")
                        time.sleep(4)
                        yhp2 = 0
                        yhp2 = yhp2
                        break

                    if oact == "Debug":
                        yhp2 = +int(input("" +str(User1)+ " hp?"))
                        print ("")
                        print ("")
                        
                    if oact == "Debug2":
                        ohp2 = +int(input("" +str(User2)+ " hp?"))
                        print ("")
                        print ("")
                        
                    if (oact == "8") or (oact == "Stats"):
                        time.sleep(.5)
                        message()

                    if oact == "+++":
                        break

                    if oact == "Shrekt":
                        yhp2 = +int(yhp2 - (((((oat2 / ydf2)) * sa) ** 3.14) * 420))
                        yhp2 = yhp2
                        time.sleep(.5)
                        print ("|Its now ogre| [Shrekt] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                        print ("")
                        print ("")
                        break
                    


    def P():
        global firstm       
        global yhp
        global yat
        global ydf
        global yspd
        global ohp
        global oat
        global odf
        global ospd
        global yhp2
        global yat2
        global ydf2
        global yspd2
        global ohp2
        global oat2
        global odf2
        global ospd2
        global a
        global yl
        global ol
        global yl2
        global ol2
        global yhcnt
        global ohcnt
        global oact      
        global cpuact
        global yact
        global crit
        global yatc
        global ymgc
        global yhlc
        global yiac
        global yidc
        global oatc
        global omgc
        global ohlc
        global oiac
        global oidc
        global hita
        global hitma
        global accuracy
        global yspec_cnt
        global ospec_cnt
        global sa
        global yspecc
        global ospecc


        crit = random.randrange(1,20)
        crit = random.randrange(21,100)
        crit = random.randrange(1,20)
        accuracy = random.randrange(2,69)
        accuracy = random.randrange(1,101)
        

        
        if yhp2 > 0:
            if "Cpu" in User1 or "cpu" in User1:
                if yhp2 >= (+int(yhp * .38)):
                    cpuact = random.randrange(7,100)
                    cpuact = random.randrange(1,7)
                    if cpuact == 1:
                        yatc = yatc + 1
                        yatc = yatc
                        if accuracy > hita:
                            ohp2 = ohp2
                            print ("|MISS| [Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                            print ("")
                            print ("")
                        else: 
                            if crit > 1:
                                ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5)))
                                time.sleep(.5)
                                print ("[Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                print ("")
                                print ("")

                            if crit == 1:
                                ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                print ("")
                                print ("")
                            


                                
                    if cpuact == 2:
                        if yhcnt == 0:
                            ymgc = ymgc + 1
                            ymgc = ymgc
                            if accuracy > hitma:
                                ohp2 = ohp2
                                time.sleep(.5)
                                print ("|MISS| [Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                print ("")
                                print ("")
                            else:
                                if crit > 1:
                                    a = random.randrange(4, 7)
                                    ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5)))
                                    time.sleep(.5)
                                    print ("[Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                    a = 4
                                    print ("")
                                    print ("")
                                    
                 
                                if crit == 1:
                                    a = random.randrange(4, 7)
                                    ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5))*1.875))
                                    time.sleep(.5)
                                    print ("|CRITICAL| [Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                    a = 4
                                    print ("")
                                    print ("")
                                

                                
                                
                        if yhcnt == 1:
                            yhp2 = +int((yhp2 + 10) + (yhp * .33))
                            time.sleep(.5)
                            print ("[Heal] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                            yhp2 = yhp2
                            print ("")
                            print ("") 
                            print ("You cannot heal again!")
                            print ("")
                            print ("")
                            yhcnt = 0
                            yhlc = yhlc + 1
                            yhlc = yhlc

                            
            
                    if cpuact == 3:
                        yat2 = +int(yat2 + (yat *.33))
                        time.sleep(.5)
                        print ("[Increase Attack] " +str(User1)+ ", your Attack is now -> [" +str(yat2)+ "]")
                        yat2 = yat2
                        print ("")
                        print ("")
                        yiac = yiac + 1
                        yiac = yiac
                                    


                    if cpuact == 4:
                        ydf2 = +int(ydf2 + (ydf * .33))
                        time.sleep(.5)
                        print ("[Increase Defense] " +str(User1)+ ", your Defense is now -> [" +str(ydf2)+ "]")
                        ydf2 = ydf2
                        print ("")
                        print ("")
                        yidc = yidc + 1
                        yidc = yidc
                                    


                    if cpuact == 5:
                        ymgc = ymgc + 1
                        ymgc = ymgc
                        if accuracy > hitma:
                            ohp2 = ohp2
                            time.sleep(.5)
                            print ("|MISS| [Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                            print ("")
                            print ("")
                        else:
                            if crit > 1:
                                a = random.randrange(4, 7)
                                ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5)))
                                time.sleep(.5)
                                print ("[Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                
                            if crit == 1:
                                a = random.randrange(4, 7)
                                ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                    
                    a = a
                    if cpuact == 6:
                        if yspec_cnt == 0:
                            ydf2 = +int(ydf2 + (ydf * .33))
                            time.sleep(.5)
                            print ("[Increase Defense] " +str(User1)+ ", your Defense is now -> [" +str(ydf2)+ "]")
                            ydf2 = ydf2
                            print ("")
                            print ("")
                            yidc = yidc + 1
                            yidc = yidc
                            
                        if yspec_cnt == 1:
                            yspec_cnt = 0
                            yspecc = yspecc + 1
                            if crit > 1:
                                ohp2 = +int(ohp2 - ((((yat * 8.4) / (odf * 8.4)) * sa)*(yl2 / 5)))
                                time.sleep(.5)
                                print ("[Special] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                            if crit == 1:
                                ohp2 = +int(ohp2 - (((((yat * 8.4) / (odf * 8.4)) * sa)*(yl2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Special] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                a = 4
                                print ("")
                                print ("")                            
                    a = a 


                        
                if yhp2 < (+int(yhp * .38)):
                    if yhcnt == 0:
                        if yspec_cnt == 0:
                            cpuact = random.randrange(1,4)
                            if cpuact == 1:
                                yatc = yatc + 1
                                yatc = yatc
                                if accuracy > hita:
                                    ohp2 = ohp2
                                    time.sleep(.5)
                                    print ("|MISS| [Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                    print ("")
                                    print ("")
                                else:
                                    if crit > 1:
                                        ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5)))
                                        time.sleep(.5)
                                        print ("[Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                        print ("")
                                        print ("")
                                    if crit == 1:
                                        ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5))*1.875))
                                        time.sleep(.5)
                                        print ("|CRITICAL| [Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                        print ("")
                                        print ("")
                                        
                            if cpuact == 2:
                                ymgc = ymgc + 1
                                ymgc = ymgc
                                a = random.randrange(4, 7)
                                if accuracy > hitma:
                                    ohp2 = ohp2
                                    time.sleep(.5)
                                    print ("|MISS| [Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                    print ("")
                                    print ("")
                                else:
                                    if crit > 1:
                                        ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5)))
                                        time.sleep(.5)
                                        print ("[Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                        a = 4
                                        print ("")
                                        print ("")
                                    if crit == 1:
                                        ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5))*1.875))
                                        time.sleep(.5)
                                        print ("|CRITICAL| [Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                        a = 4
                                        print ("")
                                        print ("")                        
                            if cpuact == 3:
                                yatc = yatc + 1
                                yatc = yatc
                                if accuracy > hita:
                                    ohp2 = ohp2
                                    time.sleep(.5)
                                    print ("|MISS| [Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                    print ("")
                                    print ("")
                                else:
                                    if crit > 1:
                                        ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5)))
                                        time.sleep(.5)
                                        print ("[Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                        print ("")
                                        print ("")
                                    if crit == 1:
                                        ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5))*1.875))
                                        time.sleep(.5)
                                        print ("|CRITICAL| [Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                        print ("")
                                        print ("")

                        if yspec_cnt == 1:
                            yspec_cnt = 0
                            yspecc = yspecc + 1
                            if crit > 1:
                                ohp2 = +int(ohp2 - ((((yat * 8.4) / (odf * 8.4)) * sa)*(yl2 / 5)))
                                time.sleep(.5)
                                print ("[Special] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                            if crit == 1:
                                ohp2 = +int(ohp2 - (((((yat * 8.4) / (odf * 8.4)) * sa)*(yl2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Special] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                    a = a
                    if yhcnt == 1:
                        yhlc = yhlc + 1
                        yhlc = yhlc
                        yhp2 = +int((yhp2 + 10) + (yhp * .33))
                        print ("")
                        time.sleep(.5)
                        print ("[Heal] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                        yhp2 = yhp2
                        print ("")
                        print ("")
                        print ("You cannot heal again!")
                        print ("")
                        print ("")
                        yhcnt = 0


                        
            else:
                while True:
                    yact = input("What will your action be " +str(User1)+ "?").title()
                    print ("")
                    print ("")


                    
                    if (yact == "Attack") or (yact == "1") :
                        yatc = yatc + 1
                        yatc = yatc
                        if accuracy > hita:
                            ohp2 = ohp2
                            time.sleep(.5)
                            print ("|MISS| [Attack] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                            print ("")
                            print ("")
                            break
                        else:
                            if crit > 1:
                                ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5)))
                                time.sleep(.5)
                                print ("[Attack] " +str(User2)+ ", your Hp is now ->","["+str(ohp2)+"]")
                                print ("")
                                print ("")
                                ohp2 = ohp2
                                break
                                
                            if crit == 1:
                                ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5))*1.875))
                                time.sleep(.5)
                                print ("|CRITICAL| [Attack] " +str(User2)+ ", your Hp is now ->","["+str(ohp2)+"]")
                                print ("")
                                print ("")
                                ohp2 = ohp2
                                break




                    if (yact == "Heal") or (yact == "5"):
                        yhlc = yhlc + 1
                        yhlc = yhlc
                        if yhcnt == 0:
                            time.sleep(.5)
                            print ("You cannot heal again!")
                            print ("")
                            print ("")


                            
                        if yhcnt == 1:
                            yhp2 = +int((yhp2 + 10) + (yhp * .33))
                            time.sleep(.5)
                            print ("[Heal] " +str(User1)+ ", your Hp is now -> [" +str(yhp2)+ "]")
                            print ("")
                            print ("")
                            print ("You cannot heal again!")
                            print ("")
                            print ("")
                            yhp2 = yhp2
                            yhcnt = 0
                            break



                    if (yact == "Increase Attack") or (yact == "3") :
                        yiac = yiac + 1
                        yiac = yiac
                        yat2 = +int(yat2 + (yat * .33))
                        time.sleep(.5)
                        print ("[Increase Attack] " +str(User1)+ ", your Attack is now -> [" +str(yat2)+ "]")
                        print ("")
                        print ("")
                        yat2 = yat2
                        break



                    if (yact == "Increase Defense") or (yact == "4") :
                        yidc = yidc + 1
                        yidc = yidc
                        ydf2 = +int(ydf2 + (ydf * .33))
                        time.sleep(.5)
                        print ("[Increase Defense] " +str(User1)+ ", your Defense is now -> [" +str(ydf2)+ "]")
                        print ("")
                        print ("")
                        ydf2 = ydf2
                        break



                    if (yact == "Magic") or (yact == "2"):
                        ymgc = ymgc + 1
                        ymgc = ymgc
                        if accuracy > hitma:
                            ohp2 = ohp2
                            time.sleep(.5)
                            print ("|MISS| [Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                            print ("")
                            print ("")
                            break


                        
                        else:
                            if crit > 1:
                                a = random.randrange(4, 7)
                                ohp2 = +int(ohp2 - ((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5)))
                                ohp2 = ohp2
                                time.sleep(.5)
                                print ("[Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                print ("")
                                print ("")
                                a = 4
                                break
                                
                            if crit == 1:
                                a = random.randrange(4, 7)
                                ohp2 = +int(ohp2 - (((((yat2 * 8.4) / (odf2 * 8.4)) * a)*(yl2 / 5))*1.875))
                                ohp2 = ohp2
                                time.sleep(.5)
                                print ("|CRITICAL| [Magic] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                print ("")
                                print ("")
                                a = 4
                                break
                    a = a



                    if yact == "Special" or yact == "6":
                        if yspec_cnt == 0:
                            time.sleep(.5)
                            print ("You cannot use [Special] again!")
                            print ("")
                            print ("")
                            
                        if yspec_cnt == 1:
                            yspec_cnt = 0
                            yspecc = yspecc + 1
                            if crit > 1:
                                ohp2 = +int(ohp2 - ((((yat * 8.4) / (odf * 8.4)) * sa)*(yl2 / 5)))
                                ohp2 = ohp2
                                time.sleep(.5)
                                print ("[Special] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                print ("You cannot use [Special] again!")
                                print ("")
                                print ("")
                                break
                            
                            if crit == 1:
                                ohp2 = +int(ohp2 - (((((yat * 8.4) / (odf * 8.4)) * sa)*(yl2 / 5))*1.875))
                                ohp2 = ohp2
                                time.sleep(.5)
                                print ("|CRITICAL| [Special] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                                a = 4
                                print ("")
                                print ("")
                                print ("You cannot use [Special] again!")
                                print ("")
                                print ("")
                                break
                        


                    if yact == "Virus" :
                        while True:
                            print ("Virus.exe loaded")
                            print ("HAHAHAHAHAHA")
                        time.sleep(91142036069696661984)
                        break


                        

                    if (yact == "s") or (yact == "8"):
                        time.sleep(.5)
                        message()

                    if yact == "Quit" or yact == "9":
                        quit()

                    if yact == "Debug":
                        ohp2 = +int(input("" +str(User2)+ " hp?"))
                        print ("")
                        print ("")
                        
                    if yact == "Debug2":
                        yhp2 = +int(input("" +str(User1)+ " hp?"))
                        print ("")
                        print ("")
                        
                    if yact == "+++":
                        break


                    
                    if yact == "Shrekt":
                        ohp2 = +int(ohp2 - (((((yat2 / odf2)) * sa) ** 3.14) * 420))
                        ohp2 = ohp2
                        time.sleep(.5)
                        print ("|Its now ogre| [Shrekt] " +str(User2)+ ", your Hp is now -> [" +str(ohp2)+ "]")
                        print ("")
                        print ("")
                        break
                    
                    if yact == "Hax":
                        print ("Haxing...")
                        print ("")
                        print ("")
                        time.sleep(4)
                        ohp2 = 0
                        ohp2 = ohp2
                        break
                        

    global firstm    
    global yhp
    global yat
    global ydf
    global yspd
    global ohp
    global oat
    global odf
    global ospd
    global yhp2
    global yat2
    global ydf2
    global yspd2
    global ohp2
    global oat2
    global odf2
    global ospd2
    global a
    global yl
    global ol
    global yl2
    global ol2
    global yhcnt
    global ohcnt
    global User1
    global crit


    def message():
        global User1
        global User2
        global yhp
        global yat
        global ydf
        global yspd
        global ohp
        global oat
        global odf
        global ospd
        global yhp2
        global yat2
        global yspd2
        global ydf2
        global ohp2
        global oat2
        global odf2
        global ospd2
        global yl
        global ol
        global yl2
        global ol2
        global crit
        global yspec_desc
        global ospec_desc
        global hita
        global hitma
        global wait
        time.sleep(.5)
        if "Cpu" in User1 or "cpu" in User1:
            if "Cpu" in User2 or "cpu" in User2:
                something_ = input("------------------------------------------")
            else:
                print ("------------------------------------------")
        else: 
            print ("------------------------------------------")
        print ("[Score]")
        print ("" +str(User1)+ " Score -> [" +str(yscore)+ "]")
        print ("" +str(User2)+ " Score -> [" +str(oscore)+ "]")
        print ("")
        print ("[Level]")
        print ("" +str(User1)+ " Level -> [" +str(yl2)+ "]")
        print ("" +str(User2)+ " Level -> [" +str(ol2)+ "]")
        print ("------------------------------------------")
        print ("[Stats]")
        print ("" +str(User1)+ " Hp -> [" +str(yhp2)+ "]")
        print ("" +str(User1)+ " Attack -> [" +str(yat2)+ "]")
        print ("" +str(User1)+ " Defense -> [" +str(ydf2)+ "]")
        print ("" +str(User1)+ " Speed -> [" +str(yspd2)+ "]")
        print ("" +str(User1)+ " Potions left -> [" +str(yhcnt)+ "]")
        print ("")
        print ("" +str(User2)+ " Hp -> [" +str(ohp2)+ "]")
        print ("" +str(User2)+ " Attack -> [" +str(oat2)+ "]")            
        print ("" +str(User2)+ " Defense -> [" +str(odf2)+ "]")
        print ("" +str(User2)+ " Speed -> [" +str(ospd2)+ "]")
        print ("" +str(User2)+ " Potions left -> [" +str(ohcnt)+ "]")
        print ("------------------------------------------")
        print ("[Actions]")
        print ("(1) Attack [40 power] [" +str(hita)+ "% Accuracy]")
        print ("(2) Magic [40-60 power] [" +str(hitma)+ "% Accuracy]")
        print ("(3) Increase Attack [33% increase in Attack]")
        print ("(4) Increase Defense [33% increase in Defense]")
        print ("(5) Heal [+10 Hp, +33% Hp, CAN ONLY USE ONCE]")
        print ("")
        print ("(6) " +str(User1)+ " Special [" +str(yspec_desc)+ "] [100% accuracy]")
        print ("(7) " +str(User2)+ " Special [" +str(ospec_desc)+ "] [100% accuracy]")
        print ("")
        print ("(8) Stats [Shows stats again]")
        print ("(9) Quit [Quits the game]")
        print ("------------------------------------------") 
        print ("")
        print ("")
    def end():
        global User1
        global User2
        global yhp
        global yat
        global ydf
        global yspd
        global ohp
        global oat
        global odf
        global ospd
        global yhp2
        global yat2
        global yspd2
        global ydf2
        global ohp2
        global oat2
        global odf2
        global ospd2
        global yl
        global ol
        global yl2
        global ol2
        global crit
        global ospecc
        global yspecc
        print ("------------------------------------------")
        print ("[Score]")
        print ("" +str(User1)+ " Score -> [" +str(yscore)+ "]")
        print ("" +str(User2)+ " Score -> [" +str(oscore)+ "]")
        print ("")
        print ("[" +str(User1)+ " Actions]")
        print ("Attack -> [" +str(yatc)+"]") 
        print ("Heal -> [" +str(yhlc)+ "]")
        print ("Magic -> [" +str(ymgc)+ "]")
        print ("Increase Attack -> [" +str(yiac)+ "]")
        print ("Increase Defense -> [" +str(yidc)+ "]")
        print ("Special -> [" +str(yspecc)+ "]")
        print ("")
        print ("[" +str(User2)+ " Actions]")
        print ("Attack -> [" +str(oatc)+"]") 
        print ("Heal -> [" +str(ohlc)+ "]")
        print ("Magic -> [" +str(omgc)+ "]")
        print ("Increase Attack -> [" +str(oiac)+ "]")
        print ("Increase Defense -> [" +str(oidc)+ "]")
        print ("Special -> [" +str(ospecc)+ "]")
        print ("------------------------------------------") 
        print ("")
        print ("")



        
    def inputs():
        global User1
        global User2
        global yhp
        global yat
        global ydf
        global yspd
        global ohp
        global oat
        global odf
        global ospd
        global yhp2
        global yat2
        global ydf2
        global yspd2
        global ohp2
        global oat2
        global odf2
        global ospd2
        global yl
        global ol
        global yl2
        global ol2
        global crit
        default()
        User1 = input("Who will be player 1?(Cpu to play against a computer)").title()
        User1 == User1
        print ("")
        print ("")
        while True:
            User2 = input("Who will be player 2?(Cpu to play against a computer)").title()
            User2 == User2
            print ("")
            print ("")
            if "Cpu" in User1 or "cpu" in User1:
                break
            else:
                if User2 != User1:
                    break
                else:
                    print ('User "' +str(User1)+ '" already taken!')
                    print ("")
                    print ("")

        global yhp2
        global yat2
        global ydf2
        global yspd2
        global ohp2
        global oat2
        global odf2
        global ospd2
        global yscore
        global oscore
        global crit


        
        Edit = input("Would you like to edit stats? (y/n)")
        print ("")
        print ("")
        Edit == Edit
        if Edit == "y":
            yhp = input("" +str(User1)+ " hp? (d) for default")
            if yhp == "d":
                yhp = 45
            yhp2 = yhp
            print ("")
            print ("")
            yat = input(""+str(User1)+ " at? (d) for default")
            if yat == "d":
                yat = 23
            yat2 = yat
            print ("")
            print ("")
            ydf = input(""+str(User1)+ " df? (d) for default")
            if ydf == "d":
                ydf = 26
            ydf2 = ydf
            print ("")
            print ("")
            yspd = input(""+str(User1)+ " spd? (d) for default")
            if yspd == "d":
                yspd = 34
            yspd2 = yspd
            print ("")
            print ("")
            yl = input(""+str(User1)+ " lvl? (d) for default")
            if yl == "d":
                yl = 10
            yl2 = yl
            print ("")
            print ("")
            ohp = input(""+str(User2)+ " hp? (d) for default")
            if ohp == "d":
                ohp = 45
            ohp2 = ohp
            print ("")
            print ("")
            oat = input(""+str(User2)+ " at? (d) for default")
            if oat == "d":
                oat = 23
            oat2 = oat
            print ("")
            print ("")
            odf = input(""+str(User2)+ " df? (d) for default")
            if odf == "d":
                odf = 26
            odf2 = odf
            print ("")
            print ("")
            ospd = input(""+str(User2)+ " spd? (d) for default")
            if ospd == "d":
                ospd = 34
            ospd2 = ospd
            print ("")
            print ("")
            ol = input(""+str(User2)+ " lvl? (d) for default")
            if ol == "d":
                ol = 10
            print ("")
            print ("")
            ol2 = ol

            
        yhp2 = yhp
        yat2 = yat
        ydf2 = ydf
        yspd2 = yspd
        yl2 = yl
        ohp2 = ohp
        odf2 = odf
        oat2 = oat
        ospd2 = ospd
        ol2 = ol


        ResetScore = input("Would you like to reset scoreboard? (y/n)")
        print ("")
        print ("")
        ResetScore = ResetScore
        if ResetScore == "y":
            yscore = 0
            oscore = 0
            print ("The score has been reset!")
            print ("")
            print ("")
        yscore = yscore
        oscore = oscore


        
        if ResetScore == "cheat":
            yscore = +int(input("What is "+str(User1)+" score?"))
            print ("")
            print ("")
            oscore = +int(input("What is "+str(User2)+" score?"))
            print ("")
            print ("")
        yscore = yscore
        oscore = oscore

     
        yhp = +int(yhp)
        yat = +int(yat)
        ydf = +int(ydf)
        yspd = +int(yspd)
        yl = +int(yl)
        
        ohp = +int(ohp)
        oat = +int(oat)
        odf = +int(odf)
        ospd = +int(ospd)
        ol = +int(ol)
        
        yhp2 = +int(yhp)
        yat2 = +int(yat)
        ydf2 = +int(ydf)
        yspd2 = +int(yspd)
        yl2 = +int(yl2)
        
        ohp2 = +int(ohp)
        oat2 = +int(oat)
        odf2 = +int(odf)
        ospd2 = +int(ospd)
        ol2 = +int(ol2)








    inputs()
    while True:
        global msg
        global yscore
        global oscore
        global crit
        global yspec_cnt
        global ospec_cnt
        global yhcnt
        global ohcnt
        if ospd2 > yspd2:
            if yhp2 > 0:
                if ohp2 > 0:
                    message()
                    P2()
                    if yhp2 > 0:
                        if ohp2 > 0:
                            P() 
            if ohp2 < 1:
                yscore = yscore + 1
                yscore = yscore
                print ("" +str(User1)+ " won the game with an Hp of [" +str(yhp2)+ "]!")
                print ("")
                print ("")
                yspec_cnt = 1
                ospec_cnt = 1
                yhcnt = 1
                ohcnt = 1
                msg = 1
                time.sleep(.5)
                end()
                default()
                inputs()
                

                
            if yhp2 < 1:
                oscore = oscore + 1
                oscore = oscore
                print ("" +str(User2)+ " won the game with an Hp of [" +str(ohp2)+ "]!")
                print ("")
                print ("")
                time.sleep(.5)
                msg = 1
                yspec_cnt = 1
                ospec_cnt = 1
                yhcnt = 1
                ohcnt = 1
                end()
                default()
                inputs()
                

        if yspd2 > ospd2:
            if ohp2 > 0:
                if yhp2 > 0:
                    message()
                    P()
                    if yhp2 > 0:
                        if ohp2 > 0:
                            P2()
            if yhp2 < 1:
                oscore = oscore + 1
                oscore = oscore
                print ("" +str(User2)+ " won the game with an Hp of [" +str(ohp2)+ "]!")
                print ("")
                print ("")
                time.sleep(.5)
                yspec_cnt = 1
                ospec_cnt = 1
                yhcnt = 1
                ohcnt = 1
                msg = 1
                end()
                default()
                inputs()

                
                
            if ohp2 < 1:
                yscore = yscore + 1
                yscore = yscore
                print ("" +str(User1)+ " won the game with an Hp of [" +str(yhp2)+ "]!")
                print ("")
                print ("")
                time.sleep(.5)
                yspec_cnt = 1
                ospec_cnt = 1
                yhcnt = 1
                ohcnt = 1
                msg = 1
                end()
                default()
                inputs()


                
        if yspd2 == ospd2:
            if firstm == 0: 
                firstm == random.randrange(1,3)
            if firstm == 1:
                if ohp2 > 0:
                    if yhp2 > 0:
                        message()
                        if msg == 1:
                            print ("RANDOMISING...")
                            print ("")
                            print ("")
                            print ("" +str(User1)+ " GOES FIRST!")
                            print ("")
                            print ("")
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
                            print ("")
                            print ("")
                            print ("" +str(User2)+ " GOES FIRST!")
                            print ("")
                            print ("")
                            msg = 2
                        P2() 
                        firstm == 2
                        if yhp2 > 0:
                            if ohp2 > 0:
                                P()

                        
        if yhp2 < 1:
            oscore = oscore + 1
            oscore = oscore
            print ("" +str(User2)+ " won the game with an Hp of [" +str(ohp2)+ "]!")
            print ("")
            print ("")
            time.sleep(.5)
            yspec_cnt = 1
            ospec_cnt = 1    
            yhcnt = 1
            ohcnt = 1
            msg = 1
            end()
            default()
            inputs()
            

            
        if ohp2 < 1:
            yscore = yscore + 1
            yscore = yscore
            print ("" +str(User1)+ " won the game with an Hp of [" +str(yhp2)+ "]!")
            print ("")
            print ("")
            time.sleep(.5)
            yspec_cnt = 1
            ospec_cnt = 1    
            yhcnt = 1
            ohcnt = 1
            msg = 1
            end()
            default()
            inputs()




while True:
    rerun()

#IN DEVELOPMENT#
#V [1.12]
#
#Added another Cpu
#
#Changed Cpu's response if below % hp
#
#Fixed big with "Special" not working after 1st battle
#
#Fixed Magic damage
#
#Added some Debug commands, and Easter Eggs
#-----#
#V [1.11.1]
#
#Edited "Special" description to include something i forgot to put (rushed out 1.11)
#
#Titles whatever User1, User2 inputs.
#-----#
#V [1.11]
#
#Added "Special"
#
#Changed default stats
#
#Added the ability to view stats again/ quit
#-----#
#V [1.10]
#
#Can type in number, instead of full name for actions
#
#Added delays
#-----#
# V [1.9]
#
#Displays amount of times action has been done, after game is over
#-----#
#V [1.8]
#
#Added critical hits
#
#Edited actions
#
#Default stats changed
#
#Added "Level" stat
#-----#
#V [1.7 - 1.7.1]
#
#Alot of bug fixes
#
#Can reset scoreboard
#-----#
#V [1.6]
#
#Shortened code (Cheated and looked up "global" command)
#
#Speed only randomised once per battle
#    
#Added scoreboard
#-----#
#V [1.5.1]
#
#Stat editor bug (different one than in 1.2) fixed
#-----#
#V [1.5]
#
#Speed Stat added
#------#
#V [1.4]
#
#Cpu fixed
#------#
#V [1.3]
#
#Cpu started
#------#
#V [1.2]
#
#Restarts game once someone dies
#
#Fixed stat editor
#------#
#V [1.1.1]
#Moved player to begening , not middle
#
#User can now custom edit stats in opening screen
#
#Edited text that shows stats, and removed spaces in "Your () is now -> []"
#
#Fixed bug with "Heal", then "Magic"
#------#
#V [1.0]
#
#Can Do actions that affect stats, in a battle simulator
#
#Two player
#-----#



