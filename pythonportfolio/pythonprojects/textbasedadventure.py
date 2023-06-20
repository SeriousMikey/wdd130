bad_input = False
print("")
print("Welcome to Family Simulator!!! ")
ready = input("Are you ready? YES or NO? ")
if ready == 'yes':
    gender = input("Are you more afraid of MEN or WOMEN? ")
    if gender.upper() == 'MEN':
        print("Your phone vibrates, meaning you got a notification. ")
        check_phone = input("Do you CHECK or IGNORE? ")
        if check_phone.upper() == 'IGNORE':
            print("You decide to ignore the notification and go to sleep. ")
            print("You wake up to someone standing over you with what looks like a knife.")
            ignored_notification = input("Do you SCREAM or CRY? ")
            if ignored_notification.upper() == 'SCREAM':
                print("You scream as loud as you can, disorienting the individual for a split second. ")
                screamed = input("Do you ATTACK or RUN? ")
                if screamed.upper() == 'ATTACK':
                    print("You attack the individual by kicking them in the groin. ")
                    print("Luckily the individual seemed to be a man, as he yelped in pain and fell on the floor.")
                    attacked = input("Do you CONTINUE your attack or RUN away? ")
                    if attacked.upper() == 'CONTINUE':
                        print("You continue your attack, going for the kill. ")
                        print("You grab the knife that the man dropped in pain and stab him multiple times in the chest. ")
                        print("You are arrested by the police for the murder of your father. ")
                        print("You won! ")
                    elif attacked.upper() == 'RUN': 
                        print("You use this opportunity to run away from your attacker. ")
                        print("You run out of the house as far away as you can. ")
                        print("Once you decide that you're a safe distance away, you call the police. ")
                        print("The police show up at your house, but find no one there. Not even your parents. ")
                        print("The police tell you that they will look for your parents if they are still missing for a few days. ")
                        print("You survived! For now. ")
                    else: 
                        bad_input = True
                else: 
                    bad_input = True
            elif ignored_notification.upper() == 'CRY':
                print("You start to cry. ")
                print("You get stabbed multiple times in the chest. ")
                print("You have died. ")
            else: 
                bad_input = True
        elif check_phone.upper() == 'CHECK':
            print("You decide to check your phone and see that you got a text. You don't recognize the number. ")
            print("The messanger says that someone is coming into your house to kill you tonight. ")
            checked_notification = input("Do you RUN, go to your PARENTS, or IGNORE the text? ")
            if checked_notification.upper == 'RUN':
                print("You run out of the house. ")
                print("You go don't really know what to do now. ")
                ran = input("Do you call the POLICE or go BACK? ")
                if ran.upper() == 'POLICE':
                    print("You call the police and tell them about the text message. ")
                    print("They tell you that they will go watch your house tonight. ")
                    print("You survived! For now.")
                elif ran.upper() == 'BACK':
                    print("You decide to go back because you didn't really have a plan. ")
                    print("All of the lights are off for some reason. ")
                    print("Before you can turn them on, you get stabbed multiple times in the chest. ")
                    print("You have died.")
                else: 
                    bad_input = True
            elif checked_notification == 'PARENTS':
                print("You decide to go tell your parents about the message. ")
                print("The lights are off for some reason. ")
                print("Before you can turn the them on, you get stabbed multiple times in the chest. ")
                print("You have died. ")
            elif checked_notification == 'IGNORE':
                print("You decide to ignore the text and go to sleep. ")
            print("You wake up to someone standing over you with what looks like a knife.")
            ignored_notification = input("Do you SCREAM or CRY? ")
            if ignored_notification.upper() == 'SCREAM':
                print("You scream as loud as you can, disorienting the individual for a split second. ")
                screamed = input("Do you ATTACK or RUN? ")
                if screamed.upper() == 'ATTACK':
                    print("You attack the individual by kicking them in the groin, hoping that they're a man. ")
                    print("Luckily the individual seemed to be a man, as he yelped in pain and fell on the floor.")
                    man = input("Do you CONTINUE your attack or RUN away? ")
                    if man.upper() == 'CONTINUE':
                        print("You continue your attack, going for the kill. ")
                        print("You grab the knife that the man dropped in pain and stab him multiple times in the chest. ")
                        print("You are arrested by the police for the murder of your father. ")
                        print("You won! ")
                    elif man.upper() == 'RUN': 
                        print("You use this opportunity to run away from your attacker. ")
                        print("You run out of the house as far away as you can. ")
                        print("Once you decide that you're a safe distance away, you call the police. ")
                        print("The police show up at your house, but find no one there. Not even your parents. ")
                        print("The police tell you that they will look for your parents if they are still missing for a few days. ")
                        print("You survived! ")
                    else: 
                        bad_input = True
                else: 
                    bad_input = True
            elif ignored_notification.upper() == 'CRY':
                print("You start to cry. ")
                print("You get stabbed multiple times in the chest. ")
                print("You have died. ")
        else: 
            bad_input = True
    elif gender.upper() == 'WOMEN':
        print("You wake up to your mom calling your name for breakfast. Your stomach growls. ")
        awoken = input("Do you EAT breakfast, or go back to SLEEP? ")
        if awoken.upper() == 'EAT':
            print("You go downstairs to the kitchen to eat breakfast. ")
            print("You are peacefully eating your eggs when your mom brings up your grades. ")
            print("They are bad. ")
            grades = input("Do you tell the TRUTH or LIE? ")
            if grades.upper() == 'TRUTH':
                print("You decide to tell the truth about your grades. ")
                print("Your mom is grateful that you told the truth, but she is not happy about your grades. ")
                print("She asks you how you will fix them. ")
                fix_grades = input("Do you talk to the TEACHER or SHRUG? ")
                if fix_grades.upper() == 'TEACHER':
                    print("Your mom seems to be satisfied by that answer. ")
                    print("After breakfast, you go to school. ")
                    print("You go through school, not really paying attention. ")
                    print("Your teacher doesn't like that, so you get scolded. ")
                    print("The bell rings to go home, but now you need to talk to your teacher. ")
                    teacher = input("Do you TALK to the teacher or just go HOME? ")
                    if teacher.upper() == 'TALK':
                        print("You told your mom you would, so you go to talk to your teacher. ")
                        print("Before you can say anything, your teacher stabs you multiple times in the chest. ")
                        print("You should know better than to talk to your teacher. ")
                        print("You have died. ")
                    elif teacher.upper() == 'HOME':
                        print("You told your mom you would, but you didn't really want to. ")
                        print("You go home, hoping she forgot. ")
                        print("The rest of the day went by and you go to sleep peacefully. ")
                        print("She forgot. ")
                        print("You won! ")
                    else:
                        bad_input = True
                elif fix_grades.upper() == 'SHRUG':
                    print("You shrug at the question. ")
                    print("You should know better than to shrug at your mom. ")
                    print("You get yelled at. ")
                else:
                    bad_input = True
            elif grades.upper() == 'LIE':
                print("You lie to your mom about your grades. ")
                print("You should know better than to lie to your mom. ")
                print("You get yelled at. ")
            else:
                bad_input = True
        elif awoken.upper() == 'SLEEP':
            print("You go back to sleep. ")
            print("You should know better than to go back to sleep. ")
            print("You get yelled at. ")
        else:
            bad_input = True
    else: 
        bad_input = True
elif ready == 'no':
    print("If you say so. ")
else:
    bad_input = True
if  bad_input:
    print("INCORRECT INPUT")
else:
    print("Come back soon!!! ")