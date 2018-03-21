def game():
    import random, time
    global p1_score, p2_score
    p1_score = 0 ; p2_score = 0  

    
    def default():
        global p1_stats_base, p2_stats_base,p1_stats_mod, p2_stats_mod, p1_actions, p2_actions, p1_actions_count, p2_actions_count
        global crit
        global turn, firstm, p1_class, p2_class, p1_mech, p2_mech, stat2, stat1, stats
        
        p1_stats_base = {} ; p1_stats_mod = {}
        p2_stats_base = {} ; p2_stats_mod = {}
        p1_mech = {}
        p2_mech = {}
        p1_actions_count = {'attack':0 , 'magic':0 , 'heal':0 , 'increase attack':0 , 'increase defense':0 , 'special':0 , 'ability':0}
        p2_actions_count = {'attack':0 , 'magic':0 , 'heal':0 , 'increase attack':0 , 'increase defense':0 , 'special':0 , 'ability':0}

        
        desc = '#%s#'
        
        if p1_class == "1" or p1_class == "Normal":
            file = open('game_details/classes/normal/normal_stats.txt','r')
        if p1_class == "2" or p1_class == "Fighting":
            file = open('game_details/classes/fighting/fighting_stats.txt','r')
        if p1_class == "3" or p1_class == "Magic":
            file = open('game_details/classes/magic/magic_stats.txt','r')
        if p1_class == "4" or p1_class == "Custom_Class1":
            file = open('game_details/classes/custom_class1/custom_class1_stats.txt','r')
        if p1_class == "5" or p1_class == "Custom_Class2":
            file = open('game_details/classes/custom_class2/custom_class2_stats.txt','r')
        if p1_class == "6" or p1_class == "Custom_Class3":
            file = open('game_details/classes/custom_class3/custom_class3_stats.txt','r')
            
        if p2_class == "1" or p2_class == "Normal":
            file2 = open('game_details/classes/normal/normal_stats.txt','r')
        if p2_class == "2" or p2_class == "Fighting":
            file2 = open('game_details/classes/fighting/fighting_stats.txt','r')
        if p2_class == "3" or p2_class == "Magic":
            file2 = open('game_details/classes/magic/magic_stats.txt','r')
        if p2_class == "4" or p2_class == "Custom_Class1":
            file2 = open('game_details/classes/custom_class1/custom_class1_stats.txt','r')
        if p2_class == "5" or p2_class == "Custom_Class2":
            file2 = open('game_details/classes/custom_class2/custom_class2_stats.txt','r')
        if p2_class == "6" or p2_class == "Custom_Class3":
            file2 = open('game_details/classes/custom_class3/custom_class3_stats.txt','r')
            
        if p1_class in "123456" or p1_class in "NormalFightingMagicCustom_Class1Custom_Class2Custom_Class3":
            while file:
                stats = file.read() ; stat1 = stats.split()
                for desc in stat1:
                    stat1.remove(desc)
                p1_mech['class name'] = (stat1[0])
                p1_stats_base['hp'] = +int(stat1[1]) ; p1_stats_base['attack'] = +int(stat1[2]) ; p1_stats_base['defense'] = +int(stat1[3]) ; p1_stats_base['speed'] = +int(stat1[4])
                p1_mech['attack name'] = (stat1[5]) ; p1_mech['attack damage'] = +float(stat1[6]) / 10 ; p1_mech['attack accuracy'] = +int(stat1[7])
                p1_mech['magic name'] = (stat1[8]) ; p1_mech['magic low'] = +float(stat1[9]) / 10 ; p1_mech['magic high'] = +float(stat1[10]) / 10 ; p1_mech['magic accuracy'] = +int(stat1[11])
                p1_mech['special damage'] = +float(stat1[12]) / 10
                p1_mech['ability id'] = stat1[13]
                p1_stats_mod = p1_stats_base.copy()
                break

            
        if p2_class in "123456" or p2_class in "NormalFightingMagicCustom_Class1Custom_class2Custom_Class3":
            while file2:
                stats2 = file2.read()
                stat2 = stats2.split()
                for desc in stat2:
                    stat2.remove(desc)
                p2_mech['class name'] = (stat2[0])
                p2_stats_base['hp'] = +int(stat2[1]) ; p2_stats_base['attack'] = +int(stat2[2]) ; p2_stats_base['defense'] = +int(stat2[3]) ; p2_stats_base['speed'] = +int(stat2[4])
                p2_mech['attack name'] = (stat2[5]) ; p2_mech['attack damage'] = +float(stat2[6]) / 10 ; p2_mech['attack accuracy'] = +int(stat2[7])
                p2_mech['magic name'] = (stat2[8]) ; p2_mech['magic low'] = +float(stat2[9]) / 10 ; p2_mech['magic high'] = +float(stat2[10]) / 10 ; p2_mech['magic accuracy'] = +int(stat2[11])
                p2_mech['special damage'] = +float(stat2[12]) / 10
                p2_mech['ability id'] = stat2[13]
                p2_stats_mod = p2_stats_base.copy()
                break
        p1_score = 0 ; p2_score = 0
        turn = 0 ; firstm = 0 

    def tutorial():
        from game_details.other import tutorial
        tutorial.run()
        
    def inputs():
        global Player1, Player2, p1_score, p2_score, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod
        global file, stats, stat1, stat2, desc, p1_class, p2_class, Player1_check, Player2_check, ti
        tut = input(">> Would you like to view tutorial? [y/n]").title() ; print("\n")
        if tut == "Y":
            tutorial()
        while True:
            Player1 = input(">> Who will be player 1?[Cpu to play against a computer]") ; print ("\n") ; Player1_check = Player1.title()
            if "Cpu" in Player1_check or "cpu" in Player1_check:
                p1_class = random.randrange(1,4) ; p1_class = str(p1_class)
                break
            
            else:
                z = 0
                print (">> What class " +str(Player1)+ "?"), time.sleep(.5)
                print ("  > (1) Normal"), time.sleep(.2) ; print ("  > (2) Fighting"), time.sleep(.2) ; print ("  > (3) Magic"), time.sleep(.2)
                print ("  > (4) Custom_Class1"), time.sleep(.2) ; print ("  > (5) Custom_Class2"), time.sleep(.2) ; print ("  > (6) Custom_Class3"), time.sleep(.2) ; print("  > (7) Random"), time.sleep(.2)
                p1_class = input("  > (8) Edit Class").title()
                print ("\n")
                if p1_class == "8" or p1_class == "Edit Class" or p1_class == "EditClass":
                    from game_details.classes import new_classes
                    new_classes.class_edit()
                if p1_class == "7":
                    p1_class = random.randrange(1,4) ; p1_class = str(p1_class)
                    break
                for x in "1" "2" "3" "4" "5" "6" "7" "8" "Normal" "Fighting" "Magic" "Custom_Class1" "Custom_Class2" "Custom_Class3" "Random" "Edit Class":
                    if p1_class == x:
                        z = 1
                if z != 1:
                    print ('> Unknown input "' +str(p1_class)+ '"!\n\n')
                else:
                    break

            
        while True:
            Player2 = input(">> Who will be player 2?[Cpu to play against a computer]") ; print ("\n")
            Player2_check = Player2.title()
            if "Cpu" in Player2_check or "cpu" in Player2_check:
                p2_class = random.randrange(1,4) ; p2_class = str(p2_class)
                break
            
            else:
                if Player2_check != Player1_check:
                    if "Cpu" in Player2_check or "cpu" in Player2_check:
                        p2_class = random.randrange(1,4) ; p2_class = str(p2_class)
                        break
                    else:
                        z = 0
                        print (">> What class " +str(Player2)+ "?"), time.sleep(.5)
                        print ("  > (1) Normal"), time.sleep(.2) ; print ("  > (2) Fighting"), time.sleep(.2) ; print ("  > (3) Magic"), time.sleep(.2)
                        print ("  > (4) Custom_Class1"), time.sleep(.2) ; print ("  > (5) Custom_Class2"), time.sleep(.2) ; print ("  > (6) Custom_Class3"), time.sleep(.2) ; print("  > (7) Random"), time.sleep(.2)
                        p2_class = input("  > (8) Edit Class").title()
                        print ("\n")
                        if p2_class == "8" or p2_class == "Edit Class" or p2_class == "EditClass":
                            from game_details.classes import new_classes
                            new_classes.class_edit()
                        if p2_class == "7":
                            p2_class = random.randrange(1,4) ; p2_class = str(p2_class)
                            break
                        for x in "1" "2" "3" "4" "5" "6" "7" "8" "Normal" "Fighting" "Magic" "Custom_Class1" "Custom_Class2" "Custom_Class3" "Random" "Edit Class":
                            if p2_class == x:
                                z = 1
                        if z != 1:
                            print ('> Unknown input "' +str(p2_class)+ '"!\n\n')
                        else:
                            break

                else:
                    print ('> User "' +str(Player1)+ '" already taken!') ; print ("\n")
           
        Edit = input(">> Would you like to edit stats? [y/n]") ; print ("\n")
        default()
        if Edit == "y":
            while True:
                try:
                    p1_stats_base['hp'] = input("> " +str(Player1)+ " hp? (d) for default") ; print ("\n")
                    if p1_stats_base['hp'] == "d" or p1_stats_base['hp'] == "D":
                        p1_stats_base['hp'] = +int(stat1[1])
                        break
                    else:
                        p1_stats_base['hp'] = +int(p1_stats_base['hp'])
                except ValueError:
                    if p1_stats_base['hp'] != "d" and p1_stats_base['hp'] != "D":
                        print ("\n\n> Must not contain letters!\n\n")
                        
            while True:
                try:
                    p1_stats_base['attack'] = input("> " +str(Player1)+ " attack? (d) for default") ; print ("\n")
                    if p1_stats_base['attack'] == "d" or p1_stats_base['attack'] == "D":
                        p1_stats_base['attack'] = +int(stat1[2])
                        break
                    else:
                        p1_stats_base['attack'] = +int(p1_stats_base['attack'])   
                except ValueError:
                    if p1_stats_base['attack'] != "d" and p1_stats_base['attack'] != "D":
                        print ("\n\n> Must not contain letters!\n\n")
                        
            while True:
                try:
                    p1_stats_base['defense'] = input("> " +str(Player1)+ " defense? (d) for default") ; print ("\n")
                    if p1_stats_base['defense'] == "d" or p1_stats_base['defense'] == "D":
                        p1_stats_base['defense'] = +int(stat1[3])
                        break
                    else:
                        p1_stats_base['defense'] = +int(p1_stats_base['defense'])      
                except ValueError:
                    if p1_stats_base['defense'] != "d" and p1_stats_base['defense'] != "D":
                        print ("\n\n> Must not contain letters!\n\n")
                        
            while True:
                try:
                    p1_stats_base['speed'] = input("> " +str(Player1)+ " speed? (d) for default") ; print ("\n")
                    if p1_stats_base['speed'] == "d" or p1_stats_base['speed'] == "D":
                        p1_stats_base['speed'] = +int(stat1[4])
                        break
                    else:
                        p1_stats_base['speed'] = +int(p1_stats_base['speed'])
                except ValueError:
                    if p1_stats_base['speed'] != "d" or p1_stats_base['speed'] != "D":
                        print ("\n\n> Must not contain letters!\n\n")
                        
            while True:
                try:
                    p2_stats_base['hp'] = input("> " +str(Player2)+ " hp? (d) for default") ; print ("\n")
                    if p2_stats_base['hp'] == "d" or p2_stats_base['hp'] == "D":
                        p2_stats_base['hp'] = +int(stat2[1])
                        break
                    else:
                        p2_stats_base['hp'] = +int(p2_stats_base['hp'])
                except ValueError:
                    if p2_stats_base['hp'] != "d" and p2_stats_base['hp'] != "D":
                        print ("\n\n> Must not contain letters!\n\n")
                        
            while True:
                try:
                    p2_stats_base['attack'] = input("> " +str(Player2)+ " attack? (d) for default") ; print ("\n")
                    if p2_stats_base['attack'] == "d" or p2_stats_base['attack'] == "D":
                        p2_stats_base['attack'] = +int(stat2[2])
                        break
                    else:
                        p2_stats_base['attack'] = +int(p2_stats_base['attack'])
                except ValueError:
                    if p2_stats_base['attack'] != "d" and p2_stats_base['attack'] != "D":
                        print ("\n\n> Must not contain letters!\n\n")
                        
            while True:
                try:
                    p2_stats_base['defense'] = input("> " +str(Player2)+ " defense? (d) for default") ; print ("\n")
                    if p2_stats_base['defense'] == "d" or p2_stats_base['defense'] == "D":
                        p2_stats_base['defense'] = +int(stat2[3])
                        break
                    else:
                        p2_stats_base['defense'] = +int(p2_stats_base['defense'])
                except ValueError:
                    if p2_stats_base['defense'] != "d" and p2_stats_base['defense'] != "D":
                        print ("\n\n> Must not contain letters!\n\n")
                        
            while True:
                try:
                    p2_stats_base['speed'] = input("> " +str(Player2)+ " speed? (d) for default") ; print ("\n")
                    if p2_stats_base['speed'] == "d" or p2_stats_base['speed'] == "D":
                        p2_stats_base['speed'] = +int(stat2[4])
                        break
                    else:
                        p2_stats_base['speed'] = +int(p2_stats_base['speed'])
                except ValueError:
                    if p2_stats_base['speed'] != "d" or p2_stats_base['speed'] != "D":
                        print ("\n\n> Must not contain letters!\n\n")


        ResetScore = input(">> Would you like to reset scoreboard? [y/n]") ; print ("\n")
        ResetScore = ResetScore
        if ResetScore == "y":
            p1_score = 0 ; p2_score = 0
            print ("> The score has been reset!\n\n")
          
        if ResetScore == "cheat":
            while True:
                try:
                    p1_score = +int(input("> What is "+str(Player1)+" score?")) ; print ("\n")
                    break
                except ValueError:
                    print ("\n\n> You cannot use letters, or decimals!\n")
                    
            while True:
                try:
                    p2_score = +int(input("> What is "+str(Player2)+" score?")) ; print ("\n")
                    break
                except ValueError:
                    print ("\n\n> You cannot use letters, or decimals!\n")
        
        if "Cpu" in Player1 or "cpu" in Player1:
            if "Cpu" in Player2 or "cpu" in Player2:
                while True:
                    try:
                        ti = +float(input(">> Time Delay between cpu actions?(1-2 seconds recomended).")) ; print ("\n")
                        break
                    except ValueError:
                        print ("\n\n> You cannot use letters, or decimals!\n")
                        
        p1_stats_mod = p1_stats_base.copy()
        p2_stats_mod = p2_stats_base.copy()
#===========================================================================================================#        
#=========================|PLAYER 1 ACTIONS|================================================================#
#===========================================================================================================#
    def ability_p1(): ###
        global Player1, p1_mech, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech
        if p1_mech['ability id'] == '1':
            p1_mech['ability name'] = ''
            if p1_actions_count['ability'] == 0:
                if p1_stats_mod['hp'] > (p2_stats_mod['hp']  + (p2_stats_mod['hp'] * .33)):
                    print ('>> [' +str(p1_mech['class name'])+ '] ' +str(Player1)+ ', ability activated! << \n\n')
                    p1_mech['attack accuracy'] += 5
                    p1_mech['magic accuracy'] += 5
                    p1_actions_count['ability'] = 1
                    
        if p1_mech['ability id'] == '2':
            p1_mech['ability name'] = 'First Strike'
            if p1_actions_count['ability'] == 1:
                print ("TEST")
                p1_stats_mod['speed'] = p1_stats_base['speed']
                
            if p1_actions_count['ability'] == 0:
                if p2_mech['ability id'] == '2':
                    p1_stats_mod['speed'] = p2_stats_mod['speed'] 
                else:
                    if p1_stats_mod['speed'] <= p2_stats_mod['speed']:
                        p1_stats_mod['speed'] = p2_stats_mod['speed'] + 1
                    print ('>> [' +str(p1_mech['class name'])+ '] ' +str(Player1)+ ', ability activated! << \n\n')
                p1_actions_count['ability'] = 1
            
        if p1_mech['ability id'] == '3':
            p1_mech['ability name'] = 'Test'
            if p1_actions_count['ability'] == 0:
                if p1_stats_mod['hp'] < (p1_stats_base['hp'] * .25):
                    print ('>> [' +str(p1_mech['class name'])+ '] ' +str(Player1)+ ', ability activated! << \n\n')
                    p1_stats_mod['attack'] = +int(p1_stats_mod['attack'] + (p1_stats_base['attack'] * .05))
                    p1_stats_mod['defense'] = +int(p1_stats_mod['defense'] + (p1_stats_base['defense'] * .05))
                    p1_actions_count['ability'] = 1
                    


                
    def p1_attack(): ###/
        global accuracy, crit, Player1, Player2, p1_mech, p1_stats_base, p1_stats_mod, p2_mech, p2_stats_base, p2_stats_mod, p1_actions_count, p2_actions_count
        p1_mech['attack damage'] = 4 ; p1_actions_count['attack'] += 1
        if accuracy > p1_mech['attack accuracy']:
            time.sleep(.5)
            print ("> |MISS| [" +str(p1_mech['attack name'])+ "] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n")
            
        else:
            if crit == 1:
                p2_stats_mod['hp'] = +int(p2_stats_mod['hp'] - ((((p1_stats_mod['attack'] / p2_stats_mod['defense']) * p1_mech['attack damage'])*(2))*1.875))
                time.sleep(.5), print ("> |CRITICAL| [" +str(p1_mech['attack name'])+ "] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n") 
            else:
                p2_stats_mod['hp'] = +int(p2_stats_mod['hp'] - (((p1_stats_mod['attack'] / p2_stats_mod['defense']) * p1_mech['attack damage'])*2))
                time.sleep(.5), print ("> [" +str(p1_mech['attack name'])+ "] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n")



                 
    def p1_magic(): ###/
        global accuracy, crit, Player1, Player2, p1_mech, p1_stats_base, p1_stats_mod, p2_mech, p2_stats_base, p2_stats_mod, p1_actions_count, p2_actions_count
        
        p1_mech['attack damage'] = random.randrange((p1_mech['magic low'] - 1),p1_mech['magic high']) ; p1_actions_count['magic'] += 1

        
        if accuracy > p1_mech['magic accuracy']:
            time.sleep(.5), print ("> |MISS| [" +str(p1_mech['magic name'])+ "] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n")
            
        else:
            if crit == 1:
                p2_stats_mod['hp'] = +int(p2_stats_mod['hp'] - ((((p1_stats_mod['attack'] / p2_stats_mod['defense']) * p1_mech['attack damage'])*(2))*1.875))
                time.sleep(.5), print ("> |CRITICAL| [" +str(p1_mech['magic name'])+ "] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n")     
            else:
                p2_stats_mod['hp'] = +int(p2_stats_mod['hp'] - (((p1_stats_mod['attack'] / p2_stats_mod['defense']) * p1_mech['attack damage'])*2))
                time.sleep(.5), print ("> [" +str(p1_mech['magic name'])+ "] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n") 




    def p1_heal(): ###/
        global accuracy, crit, Player1, Player2, p1_mech, p1_stats_base, p1_stats_mod, p2_mech, p2_stats_base, p2_stats_mod, p1_actions_count, p2_actions_count
        
        p1_stats_mod['hp'] = +int((p1_stats_mod['hp'] + 10) + (p1_stats_base['hp'] * .33))
        time.sleep(.5), print ("> [Heal] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n\nYou cannot use [Heal] again!\n\n")
        p1_mech['heal'] = 0 ; p1_actions_count['heal'] += 1




    def p1_increase_a(): ###
        global accuracy, crit, Player1, Player2, p1_mech, p1_stats_base, p1_stats_mod, p2_mech, p2_stats_base, p2_stats_mod, p1_actions_count, p2_actions_count
        
        p1_stats_mod['attack'] = +int(p1_stats_mod['attack'] + (p1_stats_base['attack'] *.33)) ; p1_actions_count['increase attack'] += 1
        time.sleep(.5), print ("> [Increase Attack] " +str(Player1)+ ", your Attack is now [" +str(p1_stats_mod['attack'])+ "]\n\n")




    def p1_increase_d(): ###
        global accuracy, crit, Player1, Player2, p1_mech, p1_stats_base, p1_stats_mod, p2_mech, p2_stats_base, p2_stats_mod, p1_actions_count, p2_actions_count

        p1_stats_mod['defense'] = +int(p1_stats_mod['defense'] + (p1_stats_base['defense'] *.33)) ; p1_actions_count['increase defense'] += 1
        time.sleep(.5), print ("> [Increase Defense] " +str(Player1)+ ", your Defense is now [" +str(p1_stats_mod['defense'])+ "]\n\n")



        
    def p1_special(): ###
        global accuracy, crit, Player1, Player2, p1_mech, p1_stats_base, p1_stats_mod, p2_mech, p2_stats_base, p2_stats_mod, p1_actions_count, p2_actions_count
        p1_mech['special'] = 0 ; p1_actions_count['special'] += 1
        
        if crit > 1:
            p2_stats_mod['hp'] = +int(p2_stats_mod['hp'] - (((p1_stats_base['attack'] / p2_stats_base['defense']) * p1_mech['special damage'])*(2)))
            time.sleep(.5), print ("> [Special] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n\nYou cannot use [Special] again!\n\n")
            p1_mech['attack damage'] = 4
            
        if crit == 1:
            p2_stats_mod['hp'] = +int(p2_stats_mod['hp'] - ((((p1_stats_base['attack'] / p2_stats_base['defense']) * p1_mech['special damage'])*(2))*1.875))
            time.sleep(.5), print ("> |CRITICAL| [Special] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n\nYou cannot use [Special] again!\n\n")
            p1_mech['attack damage'] = 4
#===========================================================================================================#
#===========================================================================================================#
#===========================================================================================================#





#===========================================================================================================#
#=========================|PLAYER 2 ACTIONS|================================================================#
#===========================================================================================================#
    def ability_p2(): ###/
        global Player2, p1_mech, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech
        if p2_mech['class name'] == '1':
            p2_mech['ability name'] = 'test'
            if p2_actions_count['ability'] == 0:
                if p2_stats_mod['hp'] > (p1_stats_mod['hp']  + (p1_stats_mod['hp'] * .33)):
                    print ('>> [' +str(p2_mech['class name'])+ '] ' +str(Player2)+ ', ability activated! << \n\n')
                    p2_mech['attack accuracy'] += 5
                    p2_mech['magic accuracy'] += 5
                    p2_actions_count['ability'] = 1
                    
        if p2_mech['class name'] == '2':
            p2_mech['ability name'] = 'First Strike'
            if p2_actions_count['ability'] == 1:
                p2_stats_mod['speed'] = p2_stats_base['speed']
                
            if p2_actions_count['ability'] == 0:
                if p1_mech['class name'] == '2':
                    p2_stats_mod['speed'] = p1_stats_mod['speed']
                else:
                    if p2_stats_mod['speed'] <= p1_stats_mod['speed']:
                        p2_stats_mod['speed'] = p1_stats_mod['speed'] + 1
                    print ('>> [' +str(p2_mech['class name'])+ '] ' +str(Player2)+ ', ability activated! << \n\n')
                p2_actions_count['ability'] = 1
                        
        if p2_class == '3':
            p2_mech['ability name'] = 'test'
            if p2_actions_count['ability'] == 0:
                if p2_stats_mod['hp'] < (p2_stats_base['hp'] * .25):
                    print ('>> [' +str(p2_mech['class name'])+ '] ' +str(Player2)+ ', ability activated! << \n\n')
                    p2_stats_mod['attack'] += (p2_stats_base['attack'] * .05)
                    p2_stats_mod['defense'] += (p2_stats_base['defense'] * .05)
                    p2_actions_count['ability'] = 1
                    
                    
    def p2_attack(): ###/
        global Player2, p1_mech, abil_name_p2, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech, crit, accuracy, p1_actions_count, p2_actions_count
        p2_mech['attack damage'] = 4 ; p2_actions_count['attack'] += 1
        
        if accuracy > p2_mech['attack accuracy']:
            time.sleep(.5), print ("> |MISS| [" +str(p2_mech['attack name'])+ "] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n")
        else:
            if crit == 1:
                p1_stats_mod['hp'] = +int(p1_stats_mod['hp'] - ((((p2_stats_mod['attack'] / p2_stats_mod['defense']) * p2_mech['attack damage'])*(2))*1.875))
                time.sleep(.5), print ("> |CRITICAL| [" +str(p2_mech['attack name'])+ "] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n") 
            else:
                p1_stats_mod['hp'] = +int(p1_stats_mod['hp'] - (((p2_stats_mod['attack'] / p2_stats_mod['defense']) * p2_mech['attack damage'])*2))
                time.sleep(.5), print ("> [" +str(p2_mech['attack name'])+ "] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n")


                 
    def p2_magic(): ###/
        global Player2, p1_mech, abil_name_p2, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech, crit, accuracy, p1_actions_count, p2_actions_count
        
        p2_mech['attack damage'] = random.randrange((p2_mech['magic low'] - 1),p2_mech['magic high']) ; p2_actions_count['magic'] += 1
        
        if accuracy > p2_mech['magic accuracy']:
            time.sleep(.5), print ("> |MISS| [" +str(p2_mech['magic name'])+ "] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n")
        else:
            if crit == 1:
                p1_stats_mod['hp'] = +int(p1_stats_mod['hp'] - ((((p2_stats_mod['attack'] / p2_stats_mod['defense']) * p2_mech['attack damage'])*(2))*1.875))
                time.sleep(.5), print ("> |CRITICAL| [" +str(p2_mech['attack name'])+ "] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n")     
            else:
                p1_stats_mod['hp'] = +int(p1_stats_mod['hp'] - (((p2_stats_mod['attack'] / p2_stats_mod['defense']) * p2_mech['attack damage'])*2))
                time.sleep(.5), print ("> [" +str(p2_mech['magic name'])+ "] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n")



    def p2_heal(): ###/
        global Player2, p1_mech, abil_name_p2, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech, crit, accuracy, p1_actions_count, p2_actions_count

        p2_actions_count['heal'] += 1
        p2_stats_mod['hp'] = +int((p2_stats_mod['hp'] + 10) + (p2_stats_base['hp'] * .33))
        time.sleep(.5), print ("> [Heal] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n\nYou cannot use [Heal] again!\n\n")



    def p2_increase_a(): ###
        global Player2, p1_mech, abil_name_p2, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech, crit, accuracy, p1_actions_count, p2_actions_count

        p2_actions_count['attack'] += 1
        p2_stats_mod['attack'] = +int(p2_stats_mod['attack'] + (p2_stats_base['attack'] *.33)) 
        time.sleep(.5), print ("> [Increase Attack] " +str(Player2)+ ", your Attack is now [" +str(p2_stats_mod['attack'])+ "]\n\n")



    def p2_increase_d(): ###
        global Player2, p1_mech, abil_name_p2, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech, crit, accuracy, p1_actions_count, p2_actions_count
        
        p2_actions_count['increase defense'] += 1
        p2_stats_mod['defense'] = +int(p2_stats_mod['defense'] + (p2_stats_base['defense'] *.33)) 
        time.sleep(.5), print ("> [Increase Defense] " +str(Player2)+ ", your Defense is now [" +str(p2_stats_mod['defense'])+ "]\n\n")



    def p2_special(): ###
        global Player2, p1_mech, abil_name_p2, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech, crit, accuracy, p1_actions_count, p2_actions_count
        
        p2_actions_count['special'] += 1
        if crit > 1:
            p1_stats_mod['hp'] = +int(p1_stats_mod['hp'] - ((((p2_stats_base['attack'] / p1_stats_base['defense']) * p2_mech['special damage'])*(2))))
            time.sleep(.5), print ("> [Special] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n\nYou cannot use [Special] again!\n\n")
            p2_mech['attack damage'] = 4
        if crit == 1:
            p1_stats_mod['hp'] = +int(p1_stats_mod['hp'] - ((((p2_stats_base['attack'] / p1_stats_base['defense']) * p2_mech['special damage'])*(2))*1.875))
            time.sleep(.5), print ("> |CRITICAL| [Special] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n\nYou cannot use [Special] again!\n\n")
            p2_mech['attack damage']
    #===========================================================================================================#
    #===========================================================================================================#
    #===========================================================================================================#




            
    def rerun():
        global P1
        global P2
        def P1():
            global firstm, p1_act, p2_act, cpuact, Player1, Player2, crit, accuracy, turn, p1_score, p2_score, Player1_check, Player2_check
            global p1_mech, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech, p1_actions_count, p2_actions_count
            turn += 1
            crit = random.randrange(1,20); accuracy = random.randrange(1,101)          
            if p1_stats_mod['hp'] > 0:
                if "Cpu" in Player1_check or "cpu" in Player1_check:
                    if p1_stats_mod['hp'] >= (+int(p1_stats_base['hp'] * .38)):
                        cpuact = random.randrange(1,7)
                        if cpuact == 1:
                            p1_attack()
                                
                        if cpuact == 2:
                            if p1_actions_count['heal'] == 0:
                                p1_heal()                                 
                            else:
                                p1_magic()

                        if cpuact == 3:
                            p1_increase_a()
                                        
                        if cpuact == 4:
                            p1_increase_d()
                                        
                        if cpuact == 5:
                            p1_magic()
                        
                        if cpuact == 6:
                            if p1_actions_count['special'] == 0:
                                p1_special()
                            else:
                                p1_increase_d()


                    if p1_stats_mod['hp'] < (+int(p1_stats_base['hp'] * .38)):
                        if p1_actions_count['heal'] > 0:
                            if p1_actions_count['special'] > 0:
                                cpuact = random.randrange(1,4)
                                
                                if cpuact == 1:
                                    p1_attack()            
                                if cpuact == 2:
                                    p1_magic()
                                if cpuact == 3:
                                    p1_attack()

                            if p1_actions_count['special'] == 0:
                                p1_special()

                        if p1_actions_count['heal'] == 0:
                            p1_heal()
                            
                else:
                    while True:
                        p1_act = input(">> What will your action be " +str(Player1)+ "?").title()
                        print ("\n")
                        
                        if p1_act == p1_mech['attack name'] or p1_act == "1" :
                            p1_attack()
                            break

                        if p1_act == p1_mech['magic name'] or p1_act == "2":
                            p1_magic()
                            break
                        
                        if p1_act == "Increase Attack" or p1_act == "3":
                            p1_increase_a()
                            break


                        if p1_act == "Increase Defense" or p1_act == "4":
                            p1_increase_d()
                            break
                        
                        if p1_act == "Heal" or p1_act == "5":
                            if p1_actions_count['heal'] > 0:
                                time.sleep(.5), print ("> You cannot use [Heal] again!\n\n")
                            else:
                                p1_heal()
                                break
                                
                            
                        if p1_act == "Special" or p1_act == "6":
                            if p1_actions_count['special'] > 0:
                                time.sleep(.5), print ("> You cannot use [Special] again!\n\n")
                            else:
                                p1_special()
                                break
                            
                            
                        if p1_act == "7" or p1_act == "Action Details":
                            detail_act()
                            
                        if p1_act == "8":
                            time.sleep(.3), message()

                        if p1_act == "Quit" or p1_act == "9":
                            quit()
                            
                        if p1_act == "Virus" :
                            while True:
                                print ("> Virus.exe loaded \n> HAHAHAHAHAHA")

                        if p1_act == "Debug2":
                            p2_stats_mod['hp'] = +int(input("> " +str(Player2)+ " hp?")) ; print("\n")
                            
                        if p1_act == "Debug1":
                            p1_stats_mod['hp'] = +int(input("> " +str(Player1)+ " hp?")) ; print("\n")

                            
                        if p1_act == "+++":
                            break

                        
                        if p1_act == "Shrekt":
                            p2_stats_mod['hp'] = +int(p2_stats_mod['hp'] - (((((p1_stats_mod['attack'] / p2_stats_mod['attack'])) * p1_mech['special damage']) ** 3.14) * 420))
                            time.sleep(.5) , print ("> |Its now ogre| [Shrekt] " +str(Player2)+ ", your Hp is now [" +str(p2_stats_mod['hp'])+ "]\n\n")
                            break
                        
                        if p1_act == "Hax":
                            print ("> Haxing...\n\n"), time.sleep(4)
                            p2_stats_mod['hp'] = 0
                            break

                        
        def P2():
            global firstm, p1_act, p2_act, cpuact, Player1, Player2, crit, accuracy, turn, p1_score, p2_score, Player1_check, Player2_check
            global p1_mech, abil_name_p2, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech, p2_actions_count
            turn += 1 #TURN COUNTER#
            
            crit = random.randrange(1,20) #CRITICAL RANDOMISER#
            accuracy = random.randrange(1,101) #ACCURACY RANDOMISER#     
            if p2_stats_mod['hp'] > 0:    
                if "Cpu" in Player2_check or "cpu" in Player2_check:   
                    if p2_stats_mod['hp'] >= (+int(p2_stats_base['hp'] * .38)):
                        cpuact = random.randrange(1,7)
                        if cpuact == 1:
                            p2_attack()
                    
                        if cpuact == 2:
                            if p2_actions_count['heal'] == 0:
                                p2_heal()
                            else:
                                p2_magic()

                        if cpuact == 3:
                            p2_increase_a()
                                        
                        if cpuact == 4:
                            p2_increase_d()
                                        
                        if cpuact == 5:
                            p2_magic()

                        if cpuact == 6:
                            if p2_actions_count['special'] == 0:
                                p2_special()
                            else:
                                p2_increase_d()
                                
                    if p2_stats_mod['hp'] < (+int(p2_stats_base['hp'] * .38)):
                        if p2_actions_count['heal'] > 0:        
                            if p2_actions_count['special'] > 0:
                                cpuact = random.randrange(1,4)
                                if cpuact == 1:
                                    p2_attack()
                                        
                                if cpuact == 2:
                                    p2_magic()
                                            
                                if cpuact == 3:
                                    p2_attack()

                            if p2_actions_count['special'] == 0:
                                p2_special()
                        
                        if p2_actions_count['heal'] == 0:
                            p2_heal()
                else:
                    while True:
                        p2_act = input(">> What will be your action " +str(Player2)+ "?").title()
                        print ("\n")
              
                        if p2_act == p2_mech['attack name'] or p2_act == "1":
                            p2_attack()
                            break
                        
                        if p2_act == p2_mech['magic name'] or p2_act == "2":
                            p2_magic()
                            break
                                          
                        if p2_act == "Increase Attack" or p2_act == "3":
                            p2_increase_a()
                            break

                        if p2_act == "Increase Defense" or p2_act == "4":
                            p2_increase_d()
                            break

                        if p2_act == "Heal" or p2_act == "5":
                            if p2_actions_count['heal'] > 0:
                                time.sleep(.5), print ("> You cannot use [Heal] again!\n\n")
                            else:
                                p2_heal()
                                break
                            
                        if p2_act == "Special" or p2_act == "6":
                            if p2_actions_count['special'] > 0:
                                time.sleep(.5), print ("> You cannot use [Special] again!\n\n")
                            else:
                                p2_special()
                                break         

                        if p2_act == "7" or p2_act == "Action Details":
                            detail_act()

                        if p2_act == "8":
                            time.sleep(.5)
                            message()
                            
                        if p2_act == "Quit" or p2_act == "9":
                            quit()

                        if p2_act == "Virus":
                            while True:
                                print ("> Virus.exe loaded \n> HAHAHAHAHAHA")
                            break

                        if p2_act == "Hax":
                            print ("> Haxing...\n\n")
                            time.sleep(4)
                            p1_hp2 = 0
                            break

                        if p2_act == "Debug1":
                            p1_stats_mod['hp'] = +int(input("> " +str(Player1)+ " hp?")) 
                            print ("\n")
                            
                        if p2_act == "Debug2":
                            p1_stats_mod['hp'] = +int(input("> " +str(Player2)+ " hp?"))
                            print ("\n")

                        if p2_act == "+++":
                            break

                        if p2_act == "Shrekt":
                            p1_stats_mod['hp'] = +int(p1_stats_mod['hp'] - (((((p1_stats_mod['attack'] / p1_stats_mod['defense'])) * p2_mech['special damage']) ** 3.14) * 420))
                            time.sleep(.5) , print ("> |Its now ogre| [Shrekt] " +str(Player1)+ ", your Hp is now [" +str(p1_stats_mod['hp'])+ "]\n\n")
                            break

                        
        def message():
            global Player1, Player2, ti
            global p1_score, p2_score
            global p1_mech, abil_name_p2, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech
            if "Cpu" in Player1 or "cpu" in Player1:
                if "Cpu" in Player2 or "cpu" in Player2:
                    time.sleep(ti)
            else:
                time.sleep(.5)
            print ("==========================================")
            print ("[Score]")
            print ("  > " +str(Player1)+ " Score [" +str(p1_score)+ "]")
            print ("  > " +str(Player2)+ " Score [" +str(p2_score)+ "]")
            print ("==========================================")
            print ("[Stats]")
            print ("  [" +str(p1_mech['class name'])+ "] " +str(Player1)+ ":")
            print ("    > Hp [" +str(p1_stats_mod['hp'])+ "]")
            print ("    > Attack [" +str(p1_stats_mod['attack'])+ "]")
            print ("    > Defense [" +str(p1_stats_mod['defense'])+ "]")
            print ("    > Speed [" +str(p1_stats_mod['speed'])+ "]")
            print ("")
            print ("  [" +str(p2_mech['class name'])+ "] " +str(Player2)+ ":")
            print ("    > Hp [" +str(p2_stats_mod['hp'])+ "]")
            print ("    > Attack [" +str(p2_stats_mod['attack'])+ "]")            
            print ("    > Defense [" +str(p2_stats_mod['defense'])+ "]")
            print ("    > Speed [" +str(p2_stats_mod['speed'])+ "]")
            print ("==========================================")
            print ("[Actions]")
            print ("  " +str(Player1)+":")
            print ("    > (1) " +str(p1_mech['attack name'])+ "")
            print ("    > (2) " +str(p1_mech['magic name'])+ "")
            print ("    > (3) Increase Attack")
            print ("    > (4) Increase Defense")
            print ("    > (5) Heal")
            print ("    > (6) Special")
            print ("")
            print ("  " +str(Player2)+":")
            print ("    > (1) " +str(p2_mech['attack name'])+ "")
            print ("    > (2) " +str(p2_mech['magic name'])+ "")
            print ("    > (3) Increase Attack")
            print ("    > (4) Increase Defense")
            print ("    > (5) Heal")
            print ("    > (6) Special")
            print ("")
            print ("  > (7) Action Details")
            print ("  > (8) Stats")
            print ("  > (9) Quit")
            print ("==========================================") 
            print ("\n")
            
        def detail_act():
            global Player1, Player2
            global p1_score, p2_score
            global p1_mech, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech
            print ("==========================================")
            print ("[Action Details]\n")
            print ("  " +str(Player1)+":")
            print ("    > (1) " +str(p1_mech['attack name'])+ " [" +str(+int(p1_mech['attack damage'] * 10))+ " damage, " +str(p1_mech['attack accuracy'])+ "% accuracy]")
            print ("    > (2) " +str(p1_mech['magic name'])+ " [" +str(+int(p1_mech['magic low'] * 10))+ "-" +str(+int(p1_mech['magic high'] * 10))+ " damage, " +str(p1_mech['magic accuracy'])+ "% accracy]")
            print ("    > (3) Increase Attack [+33% Attack]")
            print ("    > (4) Increase Defense [+33% Defense]")
            print ("    > (5) Heal [+33% hp, +10 hp, CAN ONLY USE ONCE]")
            print ("    > (6) Special [105 power, 100% accuracy, CAN ONLY USE ONCE, IMMUNE TO STAT CHANGES]")
            print ("")
            print ("  " +str(Player2)+":")
            print ("    > (1) " +str(p2_mech['attack name'])+ " [" +str(+int(p2_mech['attack damage'] * 10))+ " damage, " +str(p2_mech['attack accuracy'])+ "% accuracy]")
            print ("    > (2) " +str(p2_mech['magic name'])+ " [" +str(+int(p2_mech['magic low'] * 10))+ "-" +str(+int(p2_mech['magic high'] * 10))+ " damage, " +str(p2_mech['magic accuracy'])+ "% accracy]")
            print ("    > (3) Increase Attack [+33% Attack]")
            print ("    > (4) Increase Defense [+33% Defense]")
            print ("    > (5) Heal [+33% hp, +10 hp, CAN ONLY USE ONCE]")
            print ("    > (6) Special [105 power, 100% accuracy, CAN ONLY USE ONCE, IMMUNE TO STAT CHANGES]")
            print ("==========================================")
            print ("\n")
            
        def end():
            global Player1, Player2
            global p1_score, p2_score
            global p1_mech, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod, p2_mech
            print ("==========================================")
            print ("[Score]")
            print ("  > Turns [" +str(turn)+ "]")
            print ("  > " +str(Player1)+ " Score [" +str(p1_score)+ "]")
            print ("  > " +str(Player2)+ " Score [" +str(p2_score)+ "]")
            print ("")
            print ("  " +str(Player1)+ ":")
            print ("    > " +str(p1_mech['attack name'])+ " [" +str(p1_actions_count['attack'])+"]") 
            print ("    > Heal [" +str(p1_actions_count['heal'])+ "]")
            print ("    > " +str(p1_mech['magic name'])+ " [" +str(p1_actions_count['magic'])+ "]")
            print ("    > Increase Attack [" +str(p1_actions_count['increase attack'])+ "]")
            print ("    > Increase Defense [" +str(p1_actions_count['increase defense'])+ "]")
            print ("    > Special [" +str(p1_actions_count['special'])+ "]")
            print ("")
            print ("  " +str(Player2)+ ":")
            print ("    > " +str(p2_mech['attack name'])+ " [" +str(p2_actions_count['attack'])+"]") 
            print ("    > Heal [" +str(p2_actions_count['heal'])+ "]")
            print ("    > " +str(p2_mech['magic name'])+ " [" +str(p2_actions_count['magic'])+ "]")
            print ("    > Increase Attack [" +str(p2_actions_count['increase attack'])+ "]")
            print ("    > Increase Defense [" +str(p2_actions_count['increase defense'])+ "]")
            print ("    > Special [" +str(p2_actions_count['special'])+ "]")
            print ("==========================================") 
            print ("\n")
          
        def rungame():
            while True:
                global Player1, Player2, firstm
                global p1_score, p2_score
                global p1_mech, p1_stats_base, p1_stats_mod, p2_stats_base, p2_stats_mod
                ability_p1(), ability_p2()
                if p1_stats_mod['speed'] > p2_stats_mod['speed']:
                    if p1_stats_mod['hp'] > 0 and p2_stats_mod['hp'] > 0:
                        message(), P1()
                        if p1_stats_mod['hp'] > 0 and p2_stats_mod['hp'] > 0:
                            P2()
                            
                if p1_stats_mod['speed'] < p2_stats_mod['speed']:
                    if p1_stats_mod['hp'] > 0 and p2_stats_mod['hp'] > 0:
                        message(), P2()
                        if p1_stats_mod['hp'] > 0 and p2_stats_mod['hp'] > 0:
                            P1()
                            
                if p1_stats_mod['speed'] == p2_stats_mod['speed']:
                    if firstm == 0: 
                        firstm = random.randrange(1,3)
        
                    if firstm == 1:
                        if p1_stats_mod['hp'] > 0 and p2_stats_mod['hp'] > 0:
                            message(), P1() 
                            if p1_stats_mod['hp'] > 0 and p2_stats_mod['hp'] > 0:
                                P2()
                                
                    if firstm == 2:
                        if p1_stats_mod['hp'] > 0 and p2_stats_mod['hp'] > 0:
                            message(), P2()
                            if p1_stats_mod['hp'] > 0 and p2_stats_mod['hp'] > 0:
                                P1()
                                
                if p1_stats_mod['hp'] <= 0 or p2_stats_mod['hp'] <= 0:       
                    if p1_stats_mod['hp'] <= 0:
                        p2_score += 1
                        print ("> " +str(Player2)+ " won the game with an Hp of [" +str(p2_stats_mod['hp'])+ "]!\n\n") , time.sleep(.5)
                    if p2_stats_mod['hp'] <= 0:
                        p1_score += 1
                        print ("> " +str(Player1)+ " won the game with an Hp of [" +str(p1_stats_mod['hp'])+ "]!\n\n") , time.sleep(.5)
                    end(), default(), inputs()
        
        inputs(), rungame()
        
    while True:
        rerun() #RERUNS THE GAME#
#==================================================================================================================================================================================================#
