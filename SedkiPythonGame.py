#Fabio
#my game
Stage1 = False
ObamaMeeting = False #The stage selections
Stage1 = False
stage2 = False
stage3 = False
ObamaIntro = False
ObamaMeeting = False
chapter4 = False
bodyGaurd1 = False
chapter5 = False
end1 = False

score = 0
def credits2(): #Credits
    global score #death counter
    print ""
    print "You messed up and was sent back to the beginning of a chapter " , score , " Times"
    print """
This game was designed By: Fabio Sedki 
produced by: Fabio Sedki
created by: Fabio Sedki
written by: Fabio Sedki
and because I'm lazy to sum it up, Fabio Sedki did everything"""
    print ""
    print "There are still many more ending to find"
    print ""
    while end1 == False:
        toTheEnd = raw_input("Type 'restart' to begin again from the start again, or type 'quit' to close the game")
        toTheEnd.lower()
        if toTheEnd == 'restart':
            print """ Lets get going....."""
            beginGame()
        else:
            print"""
HAHAHAHAHAHAHAHAHAHA!!!!!!!!!!!!!!!
I LYED!!!!!!!!!!!!!!!!
YOU SHALL ALWAYS BE IN THIS GAME OF MINE!!!!!!!!!!


              \`.  |\
          \`-. \ `.| \!,,
         \ \  `.\  _   (__
     _ `-.> \ ___   \    __
      `-/,o-./O  `.      ._`
      -//   j_    |   `` _<`
       |\__(  \--'      '  \     .
       >   _    `--'      _/     ;
       |  / `----..   . /       (
       | (         `.  Y         )
        \ \     ,-.-.| |_       (_
         `.`.___\  \ \/=.`.     __)
           `--,==\    )==\,\   (_
            ,'\===`--'====\,\    `-.
          ,'.` ============\,\  (`-'
         /`=.`Y=============\,\ .'
        /`-. `|==============\_,-._
       /`-._`=|=___=========,'^, c-)
       \`-----+' ._)=====_(_`-' ^-'`-.
   -----`=====, \  `.-==(^_ ^c_,.^ `^_\-----
             (__/`--'('(_,-._)-._,-.,__)`)  hjw
                      `-._`._______.'_.-'
                          `---------'
                          """   #Something for fun, if they quit the game
    raw_input("")
def beginGame():
    global score #death counter
    global Stage1
    Stage1 = True
    print ""
    print "Chapter 1: 'Intro'"
    print ""
    print "Welcome to a day in the life of Bond.... James Bond"     #The player
    print "This is a text base parable.. that means choices you make will affect future events in the game. Spelling matters. Also remember to press enter after your choice"        #Stanley parable type game
    choice = raw_input ("So either you can BE James bond for the rest of the game type 'go' or you can quit already. Type 'exit' to enter a world of not so much fun.")        #first game choice
    choice = choice.lower() #lower casing
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if choice != 'go':
        print "I didn't quite catch that.... So I brought you to an insane asylum," #The intro to the game if they seem to not want to play. 
        print "you managed to give up on all hope and were condemned unfit to be outside of the walls of the insane asylum."
        print "Chaos flooded ever part of the world and you just sit there reading 'Time Magazine'"
        exit = raw_input("Now would you like to start again? Type 'yes' or 'no' to proceed.")
        exit = exit.lower()
        print "       "
    elif choice == 'go': #Find key word
         afterIntro()
    if exit == 'yes': #If they originally choose exit, and then decide to play the game                             
        print "Now that better... We can finally start!!!"
        print "So like I was saying before I was rudely interrupted!!!! Just encase if the insane asylum you where put into for no reason impacted your judgement."
        exit = 'original start'
        print ""
        afterIntro()
    elif exit != 'yes': #If they still don't want to play                                     
        print "Well my friend that means this is the end and you managed to never leave the insane asylum"
        thisIsTheEnd1 = raw_input("Enjoy your day, You will be recalled to the intro")
        if thisIsTheEnd1 != '100368792': #End of game choices 1
            if Stage1 == True:
                score = score + 1 #Death Counter
                beginGame()
#------------------------------------------------------------------------------------------------------------------------------------------------------
def afterIntro():
    global score #Death Counter
    global stage2
    stage2 = True
    print ""
    print "Chapter 2: 'The Morning'"
    print ""
    print "YOU are Bond.... James Bond"
    print "You have just woken up and need to start your morning routine with a cup of coffee and a nice refreshing shower"
    print " "                                    
    shower = raw_input("So to continue with your day type 'I am ready' or you can simply start your day by typing anything if you are in a hurry!")
    shower = shower.lower()
    if shower == 'i am ready': #Getting ready for the day
        print ""
        print "As you finish up your morning routine, you come to your closet and it is time to pick a outfit" #outfit choices
        print "You have so many choices to pick!!"
        print ""
        print "You can wear your favourite and lucky outfit. (Type '1' for this choice)" #option 1
        print ""
        print "Or you can wear your brand new pair of pj's. (Type '2' for this choice)"  #option 2
        print""
        print "But Ya know if you are in a hurry you can just leave in your underwear. (Type anything for this choice)"  #option no outfit
        global clothes
        clothes = raw_input("So what do you feel like wearing?") #The input
        print ""
        if clothes == '1': #if choice 1 was chosen
            print ""
            print "Well it seems today is going to be a good day!"
            print "You are going to have a fantastic day, luck is on your side."
            print "As you put on your super nice pair of one of the most expensive suit you own; The Brioni Vanquish II"
            print "You then leave for your day, When you get to work you are given your first assignment from M"
            clothes = 'Brioni Vanquish II'
            if stage2 == True: #proceeds to chapter 3, stage3
                chapter3()
        elif clothes == '2': #If they choose choice 2
            print ""
            print "You have chosen to wear your favourite pj's."
            print "The purple and orange pok a dot pj's, with rainbow stripped pants, and your obey top hat" 
            print "Well it looks like today is going to be a comfy day."
            clothes = 'purple and orange pok a dot pjs with rainbow stripped pants and an obey top hat'
            if stage2 == True: #Proceeds to chapter3
                chapter3()
        else:
            print ""
            print "Well my friend it appears you have left without any clothes on."
            print "Today is going to be an interesting day...."
            if stage2 == True:
                chapter3()
            
    elif shower != 'i am ready': #To skip morning routine
        print ""
        print "Well it looks like you are truly in a hurry. But you ended up being in such a hurry you managed to leave your car keys in the house, and dropped your house keys down a sewer"
        print "So it seems like you can't go to work today!"
        print "But because you are so motivated today you decide to walk to work"
        print " "
        print "But by the time you get to the office to get your assignment for the day it's 3 a.m. and the office is closed"
        print "The next day while you are in an internet cafe using a computer because you still can't get inside your house you receive an email saying that you got fired"
        raw_input("It has been a pretty boring experience with you I need a new job... This narration is killing me; you will be recalled to Chapter 2")
        if stage2 == True:
            score = score + 1 #Death Counter
            afterIntro()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def chapter3(): #Beginning of chapter3
    global score #Death Counter
    print ""
    global stage3
    stage3 = True
    print "Chapter 3: The assignment"
    print "When you get to work you are greeted by M"
    print ""
    if clothes == 'Brioni Vanquish II': #How the intro of chapter 3 starts depends on the clothes they are wearing
        print "M:  Hello there Mr. Bond you are looking very fancy in your" , clothes 
        print "M:  You have a serious case today"
        print ""
        mission1 = 'yea'
    elif clothes == 'purple and orange pok a dot pjs with rainbow stripped pants and an obey top hat': #For choice 2 on clothes
        print "M:  Hello Mr. Bond........ What are you wearing....."
        print "M:  Go down to Q and get some real clothes on after we are done talking"
        print "M:  You look like a clown with your " , clothes , " on"
        print "M:  But anyways You have a serious case today"
        print ""
        mission1 = 'yea' #Used as a clean up
    else:  #If they leave without clothes
        print "M:  James... where are your clothes?"
        print "M:  Hurry up and get some clothes on."
        print "M:  Come back when you have some clothes on."
        if stage3 == True: #Because they left without clothes they are given side mission
            chapter3andAHalf()
    if mission1 == 'yea':                        #The continuation of chapter 3
        print "M:  So the president of Faroe Islands has been kidnapped and is being held on Jan Mayen Island."
        print "M:  Your mission is to infiltrate and rescue the president."
        acceptMission1 = raw_input("""M: Now would you like this mission? or should I give it to agent 6?
M: Your other mission is to be a body guard for the president of the U.S. (Type 'yes' To rescue the president of Faroe Islands. Or type anything To be a body guard)""") #Side mission choice
        if acceptMission1 != 'yes': #If they choose the option of a side mission
            Obama1()
        elif acceptMission1 == 'yes':
            presidentOfFaroeIslands() #The main mission
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def chapter3andAHalf(): #Beginning of side mission
    global score #Death Counter
    global ObamaIntro
    ObamaIntro = True                                       #Makes side mission true for call backs if they die
    print ""
    print "M:  Well that's better. You finally got some real clothes on."
    print "M:  Your original case was given to agent 6"
    print "M:  So your case for today is to go and meet the president of the U.S."
    print ""
    print "M:  You will be acting as a body guard for him while he is at a conference for the next 16 hours"
    saveObama = raw_input(""".......Hey Bond... Remember me, Mr. Narrator here.... Well it looks like you have quite a boring case, Want me to send you back in time?
I found a way that you can change your case (Type 'yes' To go back in time, Or type 'no' or anything to go be a body guard)""")
    if saveObama == 'yes':
        print "Well it looks like we are going back in time to the beginning of the day"
        print ""
        if ObamaIntro == True: #Call back to chapter2
            raw_input("You will be recalled to chapter 2")
            score = score + 1 #Death Counter
            afterIntro()
    else:
        print "Well I hope you enjoy standing for nearly 16 hours being a body guard"
        if ObamaIntro == True:
            Obama1()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
def Obama1():        #Side mission
    global score #Death Counter
    global ObamaMeeting
    ObamaMeeting = True #For call back, (Response/ save spot)
    print ""
    print "Side mission: Chapter 3.1, Meeting Obama"                #Text 
    print ""
    print "Well then I guess today is gunna be quite the day"
    print "As you walk into the Pentagon you are greeted by Obama's personal secretary Ashton Carter"
    print ""
    print "Mr. Carter: This is quite the honor getting to meet the legendary Bond!!!.... James Bond!!!"
    print "Mr. Carter: Come right this way Mr. Bond"
    print "Mr. Carter: Mr. Obama will meet you in his office."
    print ""
    print "Obama: Hello my man. I've heard you are the best at what you do."
    print "Obama: So You are familiar with what is happening today?"
    print "Obama: I will be at a 16 hour meeting with some senators."
    print ""
    if ObamaMeeting == True:            #Goes to side mission part 2
        raw_input("Let's get going")
        Obama2()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def presidentOfFaroeIslands(): #Main mission
    global score #Death Counter
    global chapter4
    chapter4 = True
    print ""
    print "Chapter 4: rescuing President Of Faroe Islands, Getting ready"      #The intro
    print ""
    print "Q; Hello there James."
    print "Q: So you will be using the best gadgets I have built for this mission"
    print "Q: But I added something special, remember that car that turns into a sub you destroyed?"
    print "Q: Well I rebuilt it.... again."
    print "Q: You should probably get ready, we have so little time...."
    print ""
    print "As you fly over the Atlantic ocean you are on the phone with M"
    print "M: Bond this is your time to drive off the helicopter"
    print "M: Hurry up and get the car started to get going"
    getOfHele = raw_input("Man you really needa get off this helicopter let's get going, (Type 'jump' to get off the helicopter, or type anything to stay on it)") #Jump off the hele
    getOfHele.lower() #Lower case the input
    if getOfHele == 'jump':
        print ""
        print "YYYYYYAAAAAAAAAAHHHHHHHHOOOOOOOOOO"
        print "Dammmmnnn man that was sweet!!!!"
        print "I've never been in a falling car."
        carIntoSub = raw_input("Hurry up and hit that button the says sub to change into the submarine(type 'sub' to turn into a sub or type anything to wait")  #Turn car into sub
        if carIntoSub == 'sub':
            print ""
            print "As the tires fold in and the car seals to be air tight, a propeller come out of the trunk" 
            print "As you get close to Jan Mayen Island, you notice that it is a highly secure military base."
            choiceOfInfiltration = raw_input("""How would you like to infiltration the base?
1) Get your gun out, run in and try to kill everyone?
2) Stealth?
3) Go to the Pentagon?
or type anything to go home.(Type the number associated with the choice.)""")                       #Choice of infiltration of the base
            choiceOfInfiltration.lower()
            if choiceOfInfiltration == '1': #Rampage
                print ""
                print """ Well my friend you stormed in like a moron and got yourself killed.
well I guess we need to restart this chapter"""
                if chapter4 == True:
                    raw_input("Back to the beginning of the chapter we go!!!!")
                    score = score + 1 #Death Counter
                    presidentOfFaroeIslands()
            elif choiceOfInfiltration == '2':   #Stealth
                print ""
                print "Good choice, stealth is the key to this mission"
                print """As you get closer to the base, you put on your scuba gear.
You eject from the sub, pull out your silencer and pistol.
This is the time to do what you do best.
You get close to the land, you see a guard walking along the beach.
You shoot him, and then drag his body to a cave."""
                if chapter4 == True:
                    presidentOfFaroeIslands2()      #Function near the end
            elif choiceOfInfiltration == '3':           #Pentagon
                print ""
                print "I am really not sure why you would like to go there, but anyways"
                print "To the Pentagon we go!"
                if chapter4 == True:
                    Obama2()
            else:                   #Home
                print ""
                print "Really man you have chosen to go home!!!"
                print "Well you get home but when you step inside there is a man standing there in all black"
                print """He hands you a note and a picture
the picture is of your sub near the island, and the note says 'This Is the end'"""
                print ""
                print "Well my friend I guess this is the end, the man in black is gone when you look up but your room was filled with Carbon Monoxide"
                print "Yup..... that's right you died again!!!!"
                if chapter4 == True:
                    score = score + 1 #Death Counter
                    presidentOfFaroeIslands()
        else:
            print ""
            print "Really man! You drowned because all the air escaped the car"
            print "Here we go back to the beginning of the chapter"
            if chapter4 == True:
                score = score + 1
                presidentOfFaroeIslands()
    else:                                   #If they don't jump
        print ""
        print "Well I guess you cowered out!!!"
        print """But why!!?
You have been fired... and that means I need to perform some magic and send you back in time"""
        if chapter4 == True:
            raw_input("Back in time we go!!!")
            score = score + 1
            presidentOfFaroeIslands()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Obama2(): #Function for side mission continuation
    global score
    global bodyGaurd1
    bodyGaurd1 = True
    print ""
    if ObamaMeeting == True:                        #Side mission main intro
        print "Side mission, Chapter 3.2, The Body Guard"
        print ""
        print "So you've been standing there for 6 hours, you having fun yet?"
    else:                                           #side mission abandon main mission to save Obama
        print "As you walk up to the pentagon you notice it is awfully quite!!!"
        print "You meet up with agent 6 outside the conference room."
    print "Wait..... Do you hear that?"
    print "There was gun shots inside the conference room!!!!!!!"
    saveObama1 = raw_input("""What is your choice of action?
1) To enter the room and do your duty by saving the president? (Type '1' For this choice)
or
2) Wait for reinforcement troops? (Type anything For this choice)""")  #Choices for entering the room
    saveObama1.lower()
    if saveObama1 == '1':             #Go in right away      
        print ""
        print """As you enter the room you are faced with your worst night mare
There is not only a gun man, but standing there are two people that look identical to Barack Obama
But wait, one of them are extremely calm and the other is shaking like a mad man"""
        whatToDo = raw_input("""
Now what is your course of action?
1) Shoot the man shaking?      (Type '1')
2) Shoot the man not shaking?  (Type '2')
or
3) Shoot the man with the gun? (type anything)""")
        if whatToDo == '1': #Shoot the man shaking
            print """
Well You just put a bullet into the president of the united states!!!!
You were then shot by the other man with the gun."""
            while end1 == False:
                print ""
                print "So you shot the president of the United States...."
                if chapter4 == True:
                    print "Not only did Obama, agent 6 and you die, but so did the President of Faroe Island"
                    raw_input("This also means this is the end of the game, you are dead")
                    credits2()
                else:
                    raw_input("Well this is the end..... You are dead, and I am tired of narrating")
                    print "The end, bad ending"
                    credits2()
        elif whatToDo == '2':  #Shoot the man that is calm
            print """
Congratulations you shot the imposter!!!
But at the same time you got shot by the man holding the gun.
So yes you died."""
            if chapter4 == True:
                while end1 == False:
                    print """
But luckily agent 6 had your back and shot him back.
You may have saved the president of the united states.
But at the same time the president of Faroe Island died."""
                    raw_input("You could consider this a good ending, but not everyone lived, you may seem like a hero in the U.S. but not in Faroe island.")
                    credits2()
            else:
                while end1 == False:    
                    print "Right after you got shot reinforcements came to shot the guy that shot you."
                    raw_input("You are now officially a hero of the U.S. You saved Obama, But this is the end, a happy one though")
                    credits2()
        else: #Shot the man with the gun
            print """
So you shot the guy with the gun, right after that the man that was calm that looks like Obama pulls out a knife and tries to stab Obama, But you shoot him too."""
            while end1 == False:
                print"""
So you are now quite the hero, you saved Obama"""
                if chapter4 == True:
                    print """
You may be a hero by saving Obama, But you were fired by M because the president of Faroe Island died."""
                    raw_input("You can consider this a good ending except for the fact that your main mission was a failure. But this is still the end for me.")
                    print "Ending"
                    credits2()
                else:
                    print """
Well Done my friend You single handily saved Obama, You are now the most praised person in the U.S."""
                    raw_input("This is probably one of the best endings you can get!!! Well done my friend")
                    print "Ending is happy"
                    credits2()
    else:               #Wait for reinforcement troops
        print ""
        print """As the reinforcement troops finally get there you guys enter the room in a very tactical manor
But when you guys get there is only two men standing, a man holding a gun, and another that looks identical to Barack Obama.
There is also a body laying on the ground that also looks like Barack Obama"""
        saveObamaMaybe = raw_input("""
You are not sure what to do, and the reinforcement troops are waiting for your single, what should you do?
1) Shoot then man holding the gun (Type '1')
2) Shoot the man that looks identical to Barack Obama (Type '2')
3) Shoot both (Type '3')
or
4) Attempt to arrest both of them (Type anything)""") #When you get inside
        if saveObamaMaybe == '1':       #Shoot the gunner
            print ""
            print "You order then reinforcement troops to shoot the man holding the gun"
            print "Then you walk over to the man that looks like Obama to see if he is okay"
            print "But he will not answer you"
            saveObamaLookALike = raw_input("""
What should you do now?
1) Shoot this man? (Type '1')
2) Arrest this man? (Type '2')
or
3) Approach this man for further questioning? (Type anything) """)
            if saveObamaLookALike == '1':       #Walk up to the man that looks like Obama, shoot him?    
                print """
You repeat yourself again....
But he doesn't answer you again, so you order the men to shoot him."""
                if chapter4 == True:
                    print "Well because you ended up failing 2 missions in one day, Obama died and you did nothing about it and the president of Faroe Island died too"
                    while end1 == False:
                        print ""
                        raw_input("This is an Ending, you are no longer James Bond because he isn't an agent anymore")
                        print "The end"
                        credits2()
                else:
                    while end1 == False:
                        print ""
                        raw_input("This is an Ending, you are no longer James Bond because he isn't an agent anymore")
                        print "The end"
                        credits2()
            else:         #Arrest him
                print"""
As you walk closer to the man you feel something sharp in your gut....
It's a knife, the man had stabbed you.
You then later died in hospital."""
                while end1 == False:
                    print ""
                    print "Well my friend this is an ending, an ending where death was the end of you."
                    raw_input("Being a narrator for this story has been interesting, It truly has been an honor")
                    if chapter4 == True:
                        print "Except for the part you abandoned your main mission, and the president of Faroe Island died."
                        credits2()
                    else:
                        print ""
                        credits2()
        elif saveObamaMaybe == '2':         #Shoot the imposter
            print """
You have decided to shoot the man that looks identical to Obama.
But at that very moment you are shot by the man holding the gun.
This man was obviously a professional at this because the bullet went right through your head...... A kill shot.
So that also means you are dead and you failed the mission, because Obama is dead and so are you."""
            raw_input("Time to restart this chapter again.")
            Obama2()
        elif saveObamaMaybe == '3':         #Shoot both of the men
            print """
So you have decided to shoot both of them. But by doing this you didn't accomplish much"""
            if chapter4 == True:  #Ending
                print """
So in the end you didn't get a very happy ending!!!!
Because you abandoned you main mission the president Of Faroe Islands ended up dying and so did Barack Obama..."""
                while end1 == False:
                    print """
So in the end you got ending Bad, Both your missions where a failure
And you were fired by M"""
                    raw_input("One of The Endings, But still the end")
                    credits2()
            else:
                print """
So your task ended up being a failure
and you were fired by M"""
                while end1 == False:
                    raw_input("this is one of the Endings, But still the end")
                    print "This also means the game has ended"
                    credits2()
                    
        else:   #Arrest both of the men
            print"""
So You managed to arrest both of the men.
But the man that looks like Obama ended up being an imposter"""
            if chapter4 == True:   #If from main mission
                print ""
                print "Not only did you not save Obama, but your main mission ended up being a failure too"
                print "President of Faroe Islands ended up dying too..."
                while end1 == False:  #Ending
                    print ""
                    raw_input("So yes this is an ending, not a pleasant one, but still an end, You were fired by M, and the U.S. shamed you")
                    print "The End"
                    credits2()
            else:               #If from side mission
                 while end1 == False:
                    print ""
                    raw_input("So yes this is an ending, not a pleasant one, but still an end, You were fired by M, and the U.S. shamed you")
                    print "The End"
                    credits2()
            Obama2()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def presidentOfFaroeIslands2():
    global score
    global chapter5
    chapter5 = True
    print ""
    print "Chapter 5: Lets do what you do best, Ending"  #Chapter 5
    print ""
    youHaveABody = raw_input("""So what should you do with this dead body?
1) You can switch clothes with him (Type '1')
or
2) You can leave it there (Type anything)""")   #A fork in the halways
    if youHaveABody == '1':
        print "So you switch clothes with him so now you look like a patrol guard"
        print "Time to now to get the president"
        print "As you go into the base no one questions you being there"
        hallways = raw_input("""You come to a fork in the hall ways but which way should you go?
You can go left which has a stair case going down (Type 'left')
or
you can go right which has a stair case going up. (Type 'right')""")
        hallways.lower()
        if hallways == 'right':     #Right hallway
            print """
So you went up the stairs, but this ended up being the wrong way.
Someone noticed you, so they started questioning you.
But they are speaking a language you do not understand.
They then called security and you where brought to a seller, and was tortured."""
            if chapter5 == True:
                raw_input("You will be brought back to the beginning of the chapter")
                score = score + 1
                presidentOfFaroeIslands2()
        elif hallways == 'left':    #Left hallway
            print """
You go down stairs and is greeted by a guard, you then knock the guard unconscious, and you enter the room to find the president of Faroe Island.
You then get him out of the base."""
            while end1 == False:
                print """
Yes the mission was that easy. But you really don't know what you missed at the Pentagon.
Agent 6 died but he saved Obama's life. He is now a hero of the U.S."""
                raw_input("Well done my friend you saved the president of Faroe Island, you where then given $1 000 000 for his rescue.")
                print "Good ending"
                credits2()
        else:       #Stand and wait
            print "Well you never made up your mind and someone noticed you standing there thinking, you were then captured and tortured."
            raw_input("back in time we go") #Call back
            score = score + 1
            presidentOfFaroeIslands2()  
    else:
        print """
As you start you movement down the beach killing anyone you see that may get in the way.
You then start to near the base, what should you do?"""
        stealth = raw_input("""
You can either go through a small window you notice that is on the very bottom (Type 'window' for this choice)
or you can simply go through the front door. (Type anything for this)""")
        stealth.lower()
        if stealth == 'window':
            print ""
            print "You then sneak through the window by cutting it."
            print "Laying there is the president of Faroe Island, you then untie him and get right out of there"
            while end1 == False:
                print ""
                print "This is a happy ending"
                raw_input("It was that easy to get him. but you don't even know what you missed at the Pentagon, agent 6 died but he saved Obama. He is such a hero.")
                print "Ending"
                credits2()
        else:
            print """
Well you ran through the front door just to get shot right away...
Congrats on the death sentence you preformed."""
            raw_input("Back to the beginning of the chapter we go")
            score = score + 1
            presidentOfFaroeIslands2()
#------------------------------------------------------------------------------------
beginGame()
credits2()

