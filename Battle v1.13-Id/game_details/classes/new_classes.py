def class_edit():
    import time
    def ask():
        global choice
        print (">> Which file would you like to edit?") , time.sleep(.5)
        print ("  > (1) Normal") , time.sleep(.2)
        print ("  > (2) Fighting") , time.sleep(.2)
        print ("  > (3) Magic") , time.sleep(.2)
        print ("  > (4) Custom_Class1") , time.sleep(.2)
        print ("  > (5) Custom_Class2") , time.sleep(.2)
        choice = input("  > (6) Custom_Class3").title() ; print ("\n") , time.sleep(1)
     
    def write():
        global class_new, choice, class1_name, class2_name, class3_name, class4_name, class5_name, class6_name, class_names_combo
        
        if choice == "Normal" or choice == "1":
            class_new = open('game_details/classes/normal/normal_stats.txt','w')
            
        if choice == "Fighting" or choice == "2":
            class_new = open('game_details/classes/fighting/fighting_stats.txt','w')
            
        if choice == "Magic" or choice == "3":
            class_new = open('game_details/classes/magic/magic_stats.txt','w')
            
        if choice == "File1" or choice == "4":
            class_new = open('game_details/classes/custom_class1/custom_class1_stats.txt','w')
            
        if choice == "File2" or choice == "5":
            class_new = open('game_details/classes/custom_class2/custom_class2_stats.txt','w')
            
        if choice == "File3" or choice == "6":
            class_new = open('game_details/classes/custom_class3/custom_class3_stats.txt','w')
            
    def inputs():
        global class_new, class_name, choice, class1_name, class2_name, class3_name, class4_name, class5_name, class6_name, class_names_combo
        ask(), write()
        desc = "#class_name_->#" ; variable = input("> Class name? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n\n") ; print("\n")
        class_new.write(combo)
        desc = "#hp_->#" ; variable = input("> Hp? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n") ; print("\n")
        class_new.write(combo)
        desc = "#attack_->#" ; variable = input("> Attack? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n") ; print("\n")
        class_new.write(combo)
        desc = "#defense_->#" ; variable = input("> Defense? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n") ; print("\n")
        class_new.write(combo)
        desc = "#speed_->#" ; variable = input("> Speed? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n\n") ; print("\n")
        class_new.write(combo)
        desc = "#attack_name_->#" ; variable = input("> Attack Name? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n") ; print("\n")
        class_new.write(combo)
        desc = "#attack_damage_->#" ; variable = input("> Attack Damage? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n") ; print("\n")
        class_new.write(combo)
        desc = "#attack_accuracy_->#" ; variable = input("> Attack Accuracy? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n\n") ; print("\n")
        class_new.write(combo)
        desc = "#magic_name_->#" ; variable = input("> Magic Name? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n") ; print("\n")
        class_new.write(combo)
        desc = "#magic_damage_low_->#" ; variable = input("> Magic Damage(low)? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n") ; print("\n")
        class_new.write(combo)
        desc = "#magic_damage_high_->#" ; variable = input("> Magic Damage(high)? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n") ; print("\n")
        class_new.write(combo)
        desc = "#magic_accuracy_->#" ; variable = input("> Magic Accuracy? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n\n") ; print("\n")
        class_new.write(combo)
        desc = "#special_damage_->#" ; variable = input("> Special Damage? [Using spaces will mess it up]") ; combo = ("" +str(desc)+ " " +str(variable)+ "\n\n") ; print("\n")
        class_new.write(combo)
        desc = "#ability_id_->#" ; variable = input("> Ability Id?") ; combo = ("" +str(desc)+ " " +str(variable)+ "") ; print("\n")
        class_new.write(combo)
        class_new.close()
    inputs()

