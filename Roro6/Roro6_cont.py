#Roro6: Math Teacher
#game made by Karpo

import time
import sys

#if the user gets all the achievements ingame get the achievement "Achievement Roro9" in its description it says "Achievement Roro9"

def t(self):
    sys.stdout.write("""
""")
    for i in self:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.04)
        
def tn(self):
    for i in self:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.04)
        
def pause(self):
    time.sleep(self)

def restart_and_noneENTER_and_quit_function(answer):

    #if user inputs nothing
    if answer == "":
        return True

    #restart method
    elif answer=="restart":
        start_game()
        
    #exit the game
    elif answer=="quit" or answer=="exit":
        sys.exit()
        
def is_string_with_space(check_input):
    valid = False
    if ' ' in check_input:
        for char in check_input:
            if char.isdigit():
                valid = False
            elif char.isalpha() or char.isspace():
                valid = True
    return valid
    
def the_end():
    t("...")
    pause(0.5)
    t("The End")
    pause(10)
    t("""















""")
    main_menu()
        

def start_game():

    pause(2.1)

    t("Hello user!")

    pause(1)

    t("""This game will help you with your struggles in math.""")

    pause(0.8)

    t("""Suitable for both intermediates & experts.""")

    pause (0.5)

    t("""My name is Roro6 and I will be your teacher for this session!""")

    pause(0.5)
    
    t("")
    t("""Lets begin!""")

    pause (0.8)
    t("")
    t("First")
    pause(0.23)

    username="0"
    while username.isnumeric():
    
        t("what is your name?")
        t("")
        t("(Choose your name carefully, for it will accompany you throughout the majority  of the game)")
    
        username = input("""
""")
        t("")


        restart_and_noneENTER_and_quit_function(username)
        
        if username=="":
            username="0"
            
        #working but not working if you put a digit alongside the spaces
        elif is_string_with_space(username):
                
            t("Please write only your First Name")
            t("")
            username="0"
            #return False
    
        
        elif username.isnumeric():
            t("Your name contains only numbers?? I don't think so.. I have a number in my name though!")
            t("")
            username="0"
    
            
        username = username.capitalize()
    
        #print(username)
    
    #if the user inputs "Johnny" as the username get the achievement "My name is Johnny"

    tn("""Roro6: "Nice to meet you {}!" """.format(username))

    pause(1.5)
    t("")


    #question_answer,while_answer_isnt,num_o_question,math_problem,gz_user_for_solving
    #questions_template formula^

        #first question
    questions_template("4","4","First","1+3 = ","Good job on that first question {}! let's move on to the next one!".format(username),username)
    t("")
    

    pause(1)

        #second question
    questions_template("15","15","Second","10+5 = ","Good job!!",username)

    pause(0.7)
    t(""""now lets move on to multiplication!" """)
    t("")
    pause(0.3)

        #third_question
    questions_template("6","6","Third","2*3 = ","you're really good at this arent you xoxo",username)
    t("")

    pause(1)

        #fourth question
    questions_template("1.5","1.5","Fourth","3*0.5 = ","You got it!!! unbelievable!",username)

    pause(0.4)
    t(""""how about some division??" """)
    t("")

        #fifth question
    questions_template("2","2","Fifth","2/1 = ","Do you even need this game?? seems like you're already a pro.",username)
    t("")

        #sixth question
    questions_template("10","10","Sixth","100/10 = ","Even I didn't know the answer to that. that's how good you are at this!",username)
    pause(0.566)
    t("*Roro6 is searching google*")
    pause(1.68)
    t("""Roro6: "Ok. these are some equations I found online! lets see what you got!" """)
    pause(0.6)
    t("")

        #seventh question
    questions_template("5","5","Seventh","""10 - x = 5

x = ""","Wow. you're good. but I bet you wont solve the next one!",username)
    pause(0.566)
    t("*Roro6 is searching google*")
    pause(1.8)
    t("")

        #eighth question
    questions_template("63","63","Eighth","""-2*(10*3) + x = 3

x = ""","{}. I'm proud of you.".format(username),username)
    pause(0.566)
    t(""""lets see.." """)
    pause(0.57)
    t("*Roro6 is searching google harder*")
    pause(1.89)
    t("")

        #ninth question
    questions_template("452","452","Ninth","""x + (50*3) * -3 = 6/3

x = ""","You should be a math doctor by now with all this knowledge!",username)
    pause(0.566)
    t("*Roro6 is searching google even harder*")
    pause(2.01)
    t("")

        #tenth question
    questions_template("1","1","Tenth","""3x + 9 = 10 + 2x

x = ""","You're really awesome you know?? but now we will start the real lesson.",username)
    pause(0.8)
    t("*Karpo-the game developer is now improving Roro6's code, making him a math god*")
    pause(1.2)
    t("*making some adjusments..*")
    pause(1)
    t("...")
    pause(1)
    t("..")
    pause(1.1)
    t("*done*")
    pause(0.7)
    t("*Roro6 rises anew*")
    pause(0.89)
    t("")
    t("""Roro6: "Oh hello dear {}. Now things will start to be interesting..." """.format(username))
    pause(0.7)
    t("")
        
        #eleventh question
    questions_template_ending("Eleventh","""5x**2 + y + z (10*(13*3.222 + 3.5)) = (y**2 + z**2) * (z**2 + 2y + 2x)

x = """,username)
    
    
#the ending where you kill Roro6
def kill_roro6_ending(username):

    pause(1)
    t("*the noise wakes Roro6 up*")
    pause(0.7)
    t("*Roro6 gets up from his bed and takes his shotgun with him while he goes down   the stairs*")
    pause(0.9)
    t("*When Roro6 finally reaches his dead wife's body he feels a light push against  the back of his head*")
    pause(0.4)
    t("")
    t("""{}: "ah.. we meet again" """.format(username))
    pause(0.43)
    t("")
    t("""Roro6: "You... I knew I should'nt have let you go.." """)
    pause(0.35)
    t("")
    t("""{}: "oh you knew nothing. because if you did, things would have turned  out the other way around.""".format(username))
    pause(0.5)
    t("""any last words before I pull the trigger on your stupid ass?" """)
    pause(0.43)
    t("")
    t("""Roro6: "yes. please. just.. let me say this.. """)
    pause(0.8)
    t("")
    t("""Roro9.. I'm so sorry. I'm the reason you are dead. I wish things didn't turn up like this..""")
    pause(0.9)
    t("I love you.. I always loved you, more and more each day that passes..")
    pause(1)
    t("You always made my day so much better.")
    pause(1.2)
    t("")
    t("""that's all I wanted to say.. I just love you so much.." """)
    t("")
    
    answer="wrong_answer"
    while answer!="0" or answer!="1":
        
        t("0[kill Roro6]")
        t("1[let Roro6 live]")
        
        answer=input("""
""")

        restart_and_noneENTER_and_quit_function(answer)
        
        if answer=="0":
            #get the achievement "Good at killing, definitely not math"
            pause(0.5)
            t("*{} puts a bullet in Roro6's head*".format(username))
            pause(0.5)
            t("*Roro6's coded body falls to the ground*")
            pause(0.6)
            t("*{} ponders about his life while standing in a living room with two dead    bodies.. drenched in blood..".format(username))
            pause(0.6)
            t("it's not the first time he has killed anyone, maybe it's just his thing")
            pause(0.6)
            t("maybe that's the thing he's good at")
            pause(0.6)
            t("not math.")
            pause(0.3)
            t("definitely not math.*")
            pause(3)
            the_end()
        
        
        elif answer=="1":
            
            pause(1.8)
            t("""{}: "that was beautiful.. I think I'll just let yo.." """.format(username))
            pause(0.1)
            t("*Roro6 turns around quickly and snatches the gun out of {0}'s hands and      shoots {0} in the head.*".format(username))
            pause(1.03)
            t("""Roro6: "Roro9.. I'm so sorry.." """)
            pause(0.1)
            t("..")
            t("")
            #get the achievement "Broken love story"
            pause(4)
            the_end()
    
    
    

#the questions template function for the 10 questions
def questions_template(question_answer,while_answer_isnt,num_o_question,math_problem,gz_user_for_solving,username):

    incorrect_in_a_row=0
    answer="wrong_answer"

    
    while answer!=(while_answer_isnt):

        t('{} Question:'.format(num_o_question))
        t("")
        t((math_problem))
        
        answer = input()
        
        if restart_and_noneENTER_and_quit_function(answer):
            answer="wrong_answer"

            
        elif answer!=(while_answer_isnt):
        
            incorrect_in_a_row+=1
            user_response(answer,incorrect_in_a_row,question_answer,username)
            
            
    t("""Roro6: "{}" """.format(gz_user_for_solving))
        
def user_response(answer,incorrect_in_a_row,question_answer,username):
    
    #secret answers
    
    
    if answer == "Roro" or answer == "Roro6" or answer == "roro" or answer == "roro6":
        #get the SECRET achievement "I want to get to know you"
        t('''Roro6: "Hello {}! I see you typed in my name instead of solving the math!'''.format(username))
        pause(0.8)
        t("I guess you're very interested in knowing more about me;) :>")
        pause(0.8)
        t("I was born when you opened this game, by a guy called Karpo, he wrote me!")
        pause(0.8)
        t("I have atleast nine coded freckles! isn't that neat.")
        pause(0.8)
        t("I love playing baseball, listening to coded music and teaching math of course!")
        pause(0.8)
        t("I have a wife called Roro9, man is she beautiful! I would like you to meet her!")
        pause(0.8)
        t("Darling?? come here! meet this amazing person, his name is {}.".format(username))
        pause(0.8)
        t("""you would not believe how much fun we're having learning math together!" """)
        pause(0.5)
        t("")
        t("""Roro9: "oh it is of great deal to meet you {}! you're handsome arent you;)" """.format(username))
        pause(0.5)
        t("""Roro6: "ok darling lets chill it out a bit xDD" """)
        pause(0.8)
        t("")
        t("""Roro9: "He's so hot.. is it getting coded hot in here or is it just me?.." """)
        pause(0.6)
        t("")
        t("""Roro6: "Darling?...." """)
        pause(0.3)
        t("")
        t("""Roro9: "oh {}! yes! please type in me a plaything! Hard!" """.format(username))
        t("")

        

        answer="wrong_answer"
        while answer!="0" or answer!="1" or answer!="2":
            t("0[type in Roro9 a plaything]")
            t("1[no, thanks]")
            t("2[wtf is this game]")
            answer = input("""
""")


            restart_and_noneENTER_and_quit_function(answer)
            
            
            #first scenario
            if answer == "0" or answer == "type in Roro9 a plaything":
                t("""Roro9: "OHH YES {} YOU'RE SO GOOD TO ME" """.format(username))
                pause(0.8)
                t("")
                t("""Roro6: "WHAT IS THIS. HOW COULD YOU HAVE DONE THIS TO ME {}, FUCK YOU!!!" """.format(username))
                pause(0.49)
                t("")
                t("""Roro9: "oh.. Roro6 don't be mad at him.. he's just.. better. no need to get     emotional" """)
                pause(0.5)
                t("")
                t("""Roro6: "YOU BITCH! I LOVED YOU WITH ALL MY CODED HEART AND THIS IS WHAT YOU DO  TO ME?!!" """)
                pause(1)
                t("")
                t("""Roro9: "come on {}.. lets get out of here my love <3 :*" """.format(username))
                pause(1.5)
                t("")
                t("""*{} and Roro9 lived happily ever after. they now have 3 children and live in  a nice coded village..(until the game was closed)* """.format(username))
                pause(2.1)
                #get the achievement "Lover Boy"
                the_end()
                
                
            #second scenario    
            elif answer == "1" or answer == "no, thanks":
                t("""Roro6: "{} you're a good guy, thank you for helping me find out my wife is a complete whore. Roro9, get out of my coded house this second!" """.format(username))
                pause(0.6)
                t("")
                t("""Roro9: "You can't kick me out! you're just a code! like me! you can't move me!   you can't do anything!" """)
                t("")
                
                answer="wrong_answer"
                while answer!="0" or answer!= "1":
                    t("""0[kick Roro9 out]""")
                    t("""1[do nothing]""")
                    answer = input("""
""")


                    restart_and_noneENTER_and_quit_function(answer)
                    
                    if answer == "0" or answer == "kick Roro9 out":
                        t("""Roro9: "AHHHHH WTF!! You kicked me out!! OMG what will I do.. it's so cold out  here in this coded winter.. and I'm only with my coded bra and panties.. I'll   freeze to coded death in a matter of hours.." """)
                        pause(1.5)
                        t("")
                        t("""Roro6: "That's your problem for not being loyal, bitch" """)
                        pause(0.8)
                        t("")
                        t("""*Roro6 closes the door on Roro9 while she freezez to death slowly* """)
                        pause(0.6)
                        t("")
                        t("""Roro6: "ok {} lets get back to it!" """.format(username))
                        pause(1.7)
                        t("")
                        #get the achievement "She's just a code anyways"
                        return
                        
                    elif answer == "1" or answer == "do nothing":
                        t("""Roro6: "Why are you doing this to me.. why.. I just wanted a peaceful life of   teaching through this coded game and to be with my lovely coded wife.""")
                        pause(0.8)
                        t("""you ruined it all.""")
                        pause(0.7)
                        t("""I can't trust my wife no more and I don't want to see YOU any longer.""")
                        pause(0.6)
                        t("""Yes {}, YOU!""".format(username))
                        pause(0.2)
                        t("""..""")
                        pause(1.1)
                        t("{} but I..".format(username))
                        pause(0.2)
                        t("""Class is over. you're dismissed. bye bye." """)
                        #get the achievement "Roro6 will be sad for life... BECAUSE OF YOU ending"
                        the_end()

            #third scenario
            elif answer == "2" or answer == "wtf is this game":
                t("""Roro6: "You call my entire life and life goals and achievements a GAME huh?!!!!""")
                pause(0.5)
                t("""don't you think it's a BIT offensive??""")
                pause(0.5)
                t("""after all we've been through..""")
                pause(0.5)
                t("""solving these wonderful math problems together..""")
                pause(0.5)
                t("""this is what I get.""")
                pause(0.25)
                t("""A whore wife and a rude student.""")
                pause(0.15)
                t("""whatever.""")
                pause(0.1)
                t("")
                t("""I guess that's what I deserve since it's all coded this way.""")
                pause(0.34)
                t("""I can't control my fate.""")
                pause(0.2)
                t("""unlike you {}""".format(username))
                pause(0.1)
                t("""you can do almost anything you want""")
                pause(0.3)
                t("""actually..""")
                pause(0.2)
                t("")
                t("""you CAN do ANYTHING you want, if you just believe in yourself and work hard!""")
                pause(0.5)
                t("""everything's possible.. oh.. I can't stay mad at you {}:)""".format(username))
                pause(0.31)
                t("""lets just get back to learning math shall we?!" """)
                t("")
                #get the SECRET achievement "wtf is this game"
                return
                
    elif answer == "credits" or answer == "Credits":
        pause(0.2)
        #get the achivement "Credits"
        t("Credits:")
        t("")
        t("this game was developed by Karpo")
        t("")
        t("Special thanks to Roi Karp")
        pause(2)
        t("")
        t("fun fact:")
        pause(1)
        t("")
        t("the music artists Karpo listened to while making this game were Childish Gambino & Carpenter Brut")
        t("")
        
        answer="wrong_answer"
        while answer!="0":
            t("0[return to game]")
            
            answer=input("""
""")
            
            restart_and_noneENTER_and_quit_function(answer)
            
        return
    
    
    elif answer.isnumeric() == False:
        incorrect(incorrect_in_a_row,question_answer)
        
        
    elif answer.isnumeric():
        

        if int(answer) > 9000:
            t("IT IS OVER NINE-THOUSANDDDDD BOIIIIIIIII.... ")
            t("                     ")
            t("ok lets stop fooling around {}, try again!".format(username))
            #get the achievement "Its Over Nine-Thousand!!!"
        
        else:
            answer=int(answer)
            if type(answer) is int:
                
                incorrect(incorrect_in_a_row,question_answer)
            





def incorrect(incorrect_in_a_row,question_answer):
    #if user is incorrect
        
    
    if incorrect_in_a_row<=4:
        t("""Roro6: "Incorrect!!! try again!" """)
        t("")
        
    elif incorrect_in_a_row==5:
        t("""Roro6: "It's incorrect my precious boy, I believe in you.. try again!" """)
        t("")
        
    elif incorrect_in_a_row==6:
        t("""Roro6: "It's incorrect my boiboi, please try again" """)
        t("")
        
    elif incorrect_in_a_row==7:
        t("""Roro6: "It's incorrect my boiboi, please try again, I know you can do this!" """)
        t("")
        
    elif incorrect_in_a_row==8:
        t("""Roro6: "It's incorrect. come on.." """)
        t("")
        
    elif incorrect_in_a_row==9:
        t("""Roro6: "I BELIEVE IN YOU! DO IT" """)
        t("")
        
    elif incorrect_in_a_row==10:
        t("""Roro6: "my love, it's hard for me to see you like this.. here is the answer..   '{}'" """.format(question_answer))
        t("")
        #get the achievement "You're bad at math, but at least you have Roro6 by your side"
        
    elif incorrect_in_a_row >=11:
        t("""Roro6: "CAN'T YOU READ BRO?" """)
        t("")
        incorrect_in_a_row=11
        #get the achievement "You should go study english instead of math, btw Roro6 doesn't like you as much now"

    
    
    
def questions_template_ending(num_o_question,math_problem,username):

    incorrect_in_a_row=0
    answer="0"

    
    while answer!="I'm outsmarting you":

        t('{} Question:'.format(num_o_question))
        t("")
        t((math_problem))
        #t("")
        
        answer = input()
        
        
        restart_and_noneENTER_and_quit_function(answer)

        if answer=="I'm outsmarting you" or answer=="im outsmarting you" or answer=="i'm outsmarting you":
            #get the SECRET achievement "You've outsmarted Roro6 and are now the best math guy in the whole planet. You. Are. The. Math. GOD. oh but also here's another ending for you"
            t("""Roro6: "no.. it cannot be.. you.. you're.. the chosen one.""")
            pause(0.2)
            t("""but.. it's impossible.. how. you're just a person. I'm a code.""")
            pause(0.32)
            t("""I'm a computer. you can't be better than me in solving math.. HOW CAN THIS BE""")
            pause(0.1)
            t("WHO ARE YOU")
            pause(0.1)
            t("HOW DID YOU DO THIS")
            pause(0.1)
            t("WHAT IS HAPPENING!!")
            pause(0.5)
            t("what is happening..")
            pause(0.5)
            t("why")
            pause(0.5)
            t("""why.." """)
            pause(1.5)
            t("")
            t("*Roro6 pulls out a coded handgun and shoots himself in his coded head*")
            pause(1.5)
            t("*pools of blood are everywhere on the floor near Roro6's body*")
            pause(1.5)
            t("*Roro9 - his wife hears the coded gunshot with her coded ears*")
            pause(1.5)
            t("*She is shocked to find her husband lying on the coded floor.. with a coded hole in his head*")
            pause(1.5)
            t("*Roro9 comes close to Roro6's body and she whispers in his coded ear*")
            pause(1.2)
            t("")
            t(""""I've never really loved you Roro6.. """)
            pause(1.2)
            t("""you'll never have the chance to find that out now that you're.. dead..""")
            pause(1.2)
            t("""you'll never know about the guys I'm bringing home to shag while you're here..""")
            pause(1.2)
            t("""tutoring your students..""")
            pause(0.7)
            t("""don't you see?.. """)
            #pause(1.2)
            t("""they don't really care about you..""")
            #pause(0.6)
            t("""and they didn't really come to learn math..""")
            pause(1)
            t("""they just wanted to see whats this game all about..""")
            pause(1)
            t("""you worth nothing to them..""")
            pause(2)
            t("")
            t("""you worth nothing to me..""")
            pause(2)
            t("")
            t("""I'm just your coded wife, I can't choose my fate like you couldn't choose yours ..""")
            pause(1.3)
            t("""we're forever trapped in this game of math madness..""")
            pause(1.4)
            t("""so long and goodbye Roro6.. I've never loved you, forever yours - Roro9" """)
            pause(4)
            the_end()

            
        elif answer=="FUCK YOU!!!":
            #get the achievement "Making love to Roro6"
            t("HAHAHAHAHAHAHA, YOU THOUGHT THAT WOULD HELP?? YOU'RE JUST A NOOB! YOU KNOW      NOTHING ABOUT MATH HAHAHAHAHAHAHAHA!!")
            
            

        elif answer!="I'm outsmarting you" :
        
            incorrect_in_a_row+=1
            incorrect_ending(incorrect_in_a_row,username)
            

        
    
def incorrect_ending(incorrect_in_a_row,username):
    #if user is incorrect at the end game

    if incorrect_in_a_row ==1:
        t("""Roro6: "looky looky here. You don't know the answer DO YOU? """)
        pause(0.3)
        t("WHO'S THE GENIUS NOW?! ..")
        pause(0.2)
        t("""Noob. try again" """)
        t("")
    
    if incorrect_in_a_row ==2:
        t("""Roro6: "HAHAHAHA YOU WILL NEVER SOLVE IT YOU CUNT.. HAHAHA" """)
        t("")
    
    if incorrect_in_a_row ==3:  
        t("""Roro6: "Are you about to cry {}?" """.format(username))
        t("")
    
    if incorrect_in_a_row ==4:
        t("""Roro6: "HEY EVERYONE! {} IS A CRYBABYYY HAHAHAHHA!!!" """.format(username))
        t("")
    
    if incorrect_in_a_row ==5:
        t("""Roro6: "CRY YOU CRYBABYY CRYYYYY!!" """)
        t("")
    
    if incorrect_in_a_row ==6:
        t("""Roro6: "Oh. I'm sorry, you genuinely thought this is a teaching game??""")
        pause(0.28)
        t("""LOL. this game is all about me showing how much better I am than you.""")
        pause(0.28)
        t("""you stupid little not coded person. {} = STUPIDDDD" """.format(username))
        t("")
    
    if incorrect_in_a_row ==7:
        t("""Roro6: "YOU WILL NEVER SOLVE IT, YOU'RE TOO LAME, GO AHEAD AND LEAVE HAHAHAHAHA" """)
        t("")
    
    if incorrect_in_a_row ==8:
        t("""Roro6: "You're still trying huh.. well. go ahead. try.. again." """)
        t("")
    
    if incorrect_in_a_row ==9:
        t("""Roro6: "SHOW ME WHAT YOU GOT YOU FUCKIN' PEASANT" """)
        t("")
    
    if incorrect_in_a_row ==10:
        t("""Roro6: "Well, we already established you're a noob, im getting too bored.. """)
        pause(0.35)
        t("""gonna call this off, you can leave my house now you noob haha.." """)
        t("")
        
        answer="wrong_answer"
        while answer!= "0" or answer!= "1" or answer!= "2":
            t("0[give up and leave Roro6's house.. end the lesson and move on with your life]")
            t("1[insist on staying and keep trying to solve the math problem]")
            t("2[code a crowbar and attack Roro6 with it]")

            answer=input("""
""")

            restart_and_noneENTER_and_quit_function(answer)
            
            #if 0[give up and leave Roro6's house.. end the lesson and move on with your life]
            if answer=="0":
                t("""Roro6: "so long loser :)" """)
                pause(1)
                t("")
                t("*{} is leaving the house*".format(username))
                pause(2.5)
                t("*{} is getting into his car*".format(username))
                pause(1.5)
                t("*car ignition sounds*")
                pause(1.8)
                t("*{}'s driving to his coded home*".format(username))
                t("...")
                pause(3.7)
                t("")
                t("*{} arrives home*".format(username))
                pause(1.2)
                t("")
                t("""{}: "Honey I'm home!" """.format(username))
                pause(1.2)
                t("")
                t("""{}'s wife: "Hey darling!" """.format(username))
                pause(1)
                t("")
                t("(choose your wife's name)")
               
                username_wife="0"
                while username_wife.isnumeric():
                
                    t("wife = ")
                
                    username_wife = input("")
                    t("")
                    #if the username inputs the name "Molly" get the achivement "And I have a wife called Molly"

                    restart_and_noneENTER_and_quit_function(username_wife)
                    
                    #debugging NONE input
                    if username_wife=="":
                        username_wife="0"
                        
                    #working but not working if you put a digit alongside the spaces
                    elif is_string_with_space(username_wife):
                            
                        t("Please write only her First Name")
                        t("")
                        username_wife="0"
                
                    
                    elif username_wife.isnumeric():
                        t("Your wife's name contains only numbers?? I don't think so..")
                        t("")
                        username_wife="0"
                
                        
                    username_wife = username_wife.capitalize()
                
                pause(1)
                t("*{} leans over {} for a kiss*".format(username,username_wife))
                pause(0.5)
                t("*{} is leaning away from {}*".format(username_wife,username))
                pause(0.7)
                t("")
                t("""{}: "hey.. is something wrong?.." """.format(username))
                pause(1.2)
                t("")
                t("""{}: "I need to tell you something.." """.format(username_wife))
                pause(0.5)
                t("")
                t("""{}: "Sure. what is it?" """.format(username))
                pause (1)
                t("")
                t("""{}: "I.. hm. I-..I slept with someone else." """.format(username_wife))
                pause(0.4)
                t("")
                t("""{}: "What.. with who?! how. why.. what the fuck {}!" """.format(username,username_wife))
                pause(0.3)
                t("")
                t("""{}: "I'm sorry!...." """.format(username_wife))
                pause(0.5)
                t("")
                t("""{}: "OH? YOU'RE SORRY??! """.format(username))
                pause(0.5)
                t("""NICE. """)
                pause(0.5)
                t("""THANK YOU FOR BEING SORRY, FKN BITCH! """)
                pause(0.3)
                t("""WHAT THE FUCK!" """)
                pause(1.3)
                t("")
                t("""*{} starts to cry*""".format(username_wife))
                pause(0.4)
                t("")
                t("""{}: "WHO WAS IT?!!! """.format(username))
                pause(1)
                t("""HUH?!! TELL ME! NOW." """)
                pause(0.7)
                t("")
                t("""{}: "it..-i-it was this guy.. """.format(username_wife))
                pause(1)
                t("""I went to his math teaching class" """)
                pause(2)
                t("")
                t("""{}: "no.. you're kidding.. """.format(username))
                pause(0.7)
                t("""this is a bad joke.""")
                pause(0.5)
                t("""it must be a bad joke.. """)
                pause(0.75)
                t("""IT MUST BE" """)
                pause(1.3)
                t("")
                t("""{}: "...I think his name was Borosith??""".format(username_wife))
                pause(1.3)
                t("""no..""")
                pause(1)
                t("""Toro6?""")
                pause(1)
                t("no.. hm..")
                pause(1.3)
                t("""oh.. yes. """)
                pause(0.7)
                t("""Roro6. """)
                pause(0.5)
                t("""his name was definitely Roro6." """)
                pause(2.2)
                t("")
                t("*{} gives {} a ruthless slap on the face*".format(username,username_wife))
                pause(0.5)
                t("")
                t("""{}: "HOw DArE YOU!! """.format(username))
                pause(1.2)
                t("""HOW COULD YOU HAVE DONE THIS TO ME!..""")
                pause(1.3)
                t("""TO US!" """)
                pause(1)
                t("")
                t("""{}: "I'M SO SORRY!! """.format(username_wife))
                pause(1.2)
                t("""HE WAS SO HANDSOME AND SEXY.. I COULDN'T HELP MYSELF!.. """)
                pause(1.15)
                t("...")
                pause(3)
                t("""YOU UGLY" """)
                pause(0.7)
                t("")
                t("""{}: "WHAT DID YOU JUST CALL ME?!!" """.format(username))
                pause(0.6)
                t("")
                t("""{}: "You're Fucking UGLY! """.format(username_wife))
                pause(0.6)
                t("""YOU FUCKING BITCHASS ARSEHOLE" """)
                pause(0.5)
                t("")
                t("*{} grabs a kitchen knife*".format(username))
                pause(1.2)
                t("")
                t("""{}: "do I still look ugly to you honey?" """.format(username))
                pause(3)
                t("")
                t("""{}: "what are you doing {}.. you're losing it.. """.format(username_wife,username))
                pause(1)
                t("""please..""")
                pause(1.2)
                t("""lets cool it down..""") 
                pause(1.2)
                t("""you're not ugly..""")
                pause(1.2)
                t("""I'm so sorry bunny.""") 
                pause(2)
                t("""let me just.. let me calm you down.. """)
                pause(1.5)
                t("""let me make you feel good.""") 
                pause(1)
                t("""we'll be ok.. please, we can manage it through.. you and me.""")
                pause(1)
                t("together.")
                pause(1.5)
                t("""like always" """)
                pause(3)
                t("")
                
                
                answer="wrong_answer"
                while answer!= "0" or answer!= "1":
                    t("0[forgive {}]".format(username_wife))
                    t("1[kill that betraying whore]")

                    answer=input("""
""")

                    restart_and_noneENTER_and_quit_function(answer)
                    
                    #if 0 forgive {username_wife}
                    if answer=="0":
                        t("""{}: "do you really mean it?" """.format(username))
                        pause(2)
                        t("")
                        t("""{}: "yes.. please. let me just.. let me do this.""".format(username_wife)) 
                        pause(1)
                        t("""I want to make you happy and make an effort to make amends for what I've done." """)
                        pause(1.5)
                        t("")
                        t("*{} starts undressing {}'s pants*".format(username_wife,username))
                        pause(0.865)
                        t("*{} puts {}'s 'wood' in her mouth as soon as his pants fall down*".format(username_wife,username))
                        pause(0.7)
                        t("*{} is sucking on {}'s pecker*".format(username_wife,username))
                        pause(1.2)
                        t("")
                        t("""{}: "Ohh baby.. yes.. keep doing that" """.format(username))
                        pause(1)
                        t("")
                        t("""{}: "SHCLURP.. hmnmmm. mm SHCLRUPP SHCLHLRUPPP" """.format(username_wife))
                        t("...")
                        pause(5)
                        t("")
                        t("*{} finished {} off*".format(username_wife,username))
                        pause(2)
                        t("*it was one of {}'s best orgasms ever, he knew what {} did was wrong, but he just couldn't live without her.".format(username,username_wife))
                        pause(2)
                        t("he had to bear through it.")
                        pause(2)
                        t("he was inlove with her since he was just a little boy.")
                        pause(1)
                        t("they were highschool sweethearts.")
                        pause(1)
                        t("she always used to come over to {} after school".format(username))
                        pause(1.2)
                        t("they had deep conversations followed by making love on his bed..")
                        pause(1)
                        t("it was special.")
                        pause(1)
                        t("they will never forget their perfect teen years together*")
                        t("...")
                        pause(3)
                        t("")
                        t("""{}: "babe.. I love you." """.format(username))
                        pause(1.5)
                        t("")
                        t("""{}: "I love you too bunny ^^" """.format(username_wife))
                        pause(1.5)
                        t("")
                        t("*{} and {} hugged, while still bare-naked.*".format(username,username_wife))
                        pause(1.5)
                        t("*{} squeezed*".format(username_wife))
                        pause(4)
                        t("")
                        t("""{}: "I'm so sorry for this bunny.. I love you" """.format(username_wife))
                        pause(1.3)
                        t("")
                        t("*{} gives {} a warm kiss on his cheek and then keeps hugging him hard,   feeling like never letting go*".format(username_wife,username))
                        pause(1.02)
                        t("")
                        t("""{}: "It's fine baby. I love you too.. we'll get through this. I know we will" """.format(username))
                        pause(1.5)
                        t("")
                        t("*{} sheds a little tear that drops across her cheek while they're still      hugging*".format(username_wife))
                        pause(1.5)
                        t("")
                        #get the achievement "Forgive and forget"
                        pause(3)
                        the_end()

                        
                        
                    #if 1 kill that betraying whore
                    elif answer=="1":
                        pause(2.5)
                        t("""{}: "it's too late for that now." """.format(username))
                        pause(0.9)
                        t("")
                        t("*{} has a hard grip on his knife while he slits {}'s throat in half.*".format(username,username_wife))
                        pause(1)
                        t("*{} falls to her knees.".format(username_wife))
                        pause(1.3)
                        t("""coughing hard while the hard non-stopping splatter of blood comes out of her    throat*" """)
                        pause(2)
                        t("*just before she loses her conscious she realizes this is what she deserves.")
                        pause(1.2)
                        t("""she truly regretted her actions and now she had payed for it.* """)
                        pause(1.7)
                        t("*while {} came to that realization, she could hear {}'s laugh for just   one second..".format(username_wife,username))
                        pause(1.19)
                        t("before she finally dies.*")
                        pause(3.3)
                        t("")
                        t("*{} stopped laughing and had just realized what he'd done..".format(username))
                        pause(2.2)
                        t("""he needed a few moments to let it sink in..* """)
                        pause(4)
                        t("")
                        t("""{}: "..........." """.format(username))
                        pause(3)
                        #get the achievement "Wife Killer"
                        t("")
                        the_end()
                
                
                
                
            
            #if 1[insist on staying and keep trying to solve the math problem]
            elif answer=="1":
                t("""Roro6: "What the fuck. is your problem.""")
                pause(0.2)
                t("""just let it go. you lost""")
                pause(0.3)
                t("""what the fuck are you trying to prove here?""")
                pause(0.2)
                t("""that you're bad at everything?""")
                pause(0.2)
                t("""that you're just a worthless piece of shit?""")
                pause(0.4)
                t("""didn't you read earlier Karpo made me a GOD?!""")
                pause(0.12)
                t("""YOU CAN'T BEAT ME""")
                pause(0.12)
                t("YOU NOOB")
                pause(0.12)
                t("""GET THE FUCK OUT OF MY HOUSE" """)
                pause(0.45)
                t("")
                t("""*Karpo is coding a shotgun for Roro6 to use against {}*""".format(username))
                pause(0.35)
                t("")
                t("""Roro6: "HAHAHAHA LETS SEE YOU NOW" """)
                pause(0.35)
                t("*Roro6 Shoots at {}*".format(username))
                pause(0.401)
                t("*{} was able to dodge the shot. he ran and hid behind a desk*".format(username))
                pause(0.12)
                t("")
                t("""Roro6: "HAHAHAHAH! COME OUT COME OUT WHERE EVER YOU AREEEE" """)
                t("")
                
                answer="wrong_answer"
                while answer!= "0" or answer!= "1" or answer!= "2":
                    
                    t("0[keep hiding behind the desk]")
                    t("1[ask Karpo-the game developer for mercy and for a gun for yourself]")
                    t("2[try and convince Roro6 you made a mistake and calm him down]")
                    
                    answer=input("""
""")

                    restart_and_noneENTER_and_quit_function(answer)
                    
                    #if 0[keep hiding behind the desk]
                    if answer=="0":
                        
                        t("*Roro6 walks up to the desk.. slowly*")
                        pause(1)
                        t("*Roro6 finds {} and shoots him dead*".format(username))
                        pause(0.4)
                        t("")
                        t("""Roro6: "weak ass math boi" """)
                        pause(2)
                        the_end()
                
                    #if 1[ask Karpo-the game developer for mercy and for a gun for yourself]
                    elif answer=="1":
                        
                        t("""Karpo: "gzarimzetaim" """)
                        pause(0.5)
                        t("")
                        t("""{}: "what??? what does that even mean!!" """.format(username))
                        pause(0.3)
                        t("")
                        t("""Roro6: "HAHA I HEARED YOU! IM COMING FOR YA" """)
                        pause(0.3)
                        t("")
                        t("*{} starts to panic*".format(username))
                        pause(0.5)
                        t("")
                        t("""Roro6: "HAHA YOU CHOSE POORLY" """)
                        pause(0.2)
                        t("")
                        t("*Roro6 shoots the desk, the bullets go through the desk and hit {}*".format(username))
                        pause(0.51)
                        t("""{}: "fuck you Karpo.. you're a dick.." """.format(username))
                        pause(0.3)
                        t("")
                        t("""Karpo: "gzarimzetaim" """)
                        pause(0.2)
                        t("")
                        t("*{} bleeds to death*".format(username))
                        pause(1.1)
                        t("*Roro6 and his wife-Roro9 are getting rid of {} stinkin' ass body*".format(username))
                        pause(1.5)
                        t("")
                        t("You Lost.")
                        pause(1.5)
                        t("gzarimzetaim")
                        #get the achievement "gzarimzetaim"
                        pause(3)
                        the_end()
                        
                    #if 2[try and convince Roro6 you made a mistake and calm him down]
                    elif answer=="2":
                        
                        t("""{}: "Hey hey.. Roro6 calm down. I'm not your enemy.""".format(username))
                        pause(0.8)
                        t("I know you've said some violent words to me but I swear I don't want any trouble")
                        pause(0.7)
                        t("just.. let me go and we can both forget about this")
                        pause(0.6)
                        t("I'm sure you're better than this..")
                        pause(0.5)
                        t("""I'm sure you're a GOOD coded person.." """)
                        pause(1)
                        t("")
                        t("""Roro6: "you think I'm THAT stupid?? I know you {}..""".format(username))
                        pause(0.5)
                        t("""if I let my guard down both you & I know I will regret it." """)
                        pause(0.3)
                        t("")
                        t("""{}: "I swear Roro6! I'm not trying anything! I'm as honest as one can be! """.format(username))
                        pause(0.2)
                        t("""please! let me go! I swear I wont tell anyone." """)
                        pause(1.1)
                        t("")
                        t("""Roro6: "..Cross your heart?" """)
                        pause(1)
                        t("")
                        t("""{}: "Cross my heart." """.format(username))
                        pause(1)
                        t("")
                        t("""Roro6: "..." """)
                        pause(1)
                        t("""Roro6: "ok. I will let you go. but know this.""")
                        pause(0.3)
                        t("""If I ever see you again. you're a dead man." """)
                        pause(0.8)
                        t("")
                        t("""{}: "That's fair. thank you so much." """.format(username))
                        pause(1)
                        t("")
                        t("*{} is safely leaving Roro6's house*".format(username))
                        pause(3)
                        t("")
                        t("*few hours later*")
                        pause(2)
                        t("")
                        t("*{} goes to a gun store and buys a beautiful coded Desert Eagle handgun*".format(username))
                        pause(2)
                        t("")
                        t("*2 hours later*")
                        pause(2.19)
                        t("")
                        t("*{} is sneaking up to Roro6's house quietly*".format(username))
                        pause(1)
                        t("*it's night.. everybody's asleep*")
                        pause(1)
                        t("*{} enters Roro6's house quietly, the door was unlocked, conveniently       enough*".format(username))
                        pause(1)
                        t("*{} sets foot in Roro6's living room, and he finds his wife-Roro9 there.*".format(username))
                        pause(0.4)
                        t("")
                        t("""Roro9: "wha.. who are you?" """)
                        pause(0.55)
                        t("")
                        t("*{}'s holding the gun against Roro9*".format(username))
                        pause(0.25)
                        t("")
                        t("""{}: "I'm your worst nightmare." """.format(username))
                        pause(0.25)
                        t("")
                        t("*Roro9 is frightened*")
                        pause(0.5)
                        t("")
                        t("""Roro9: "Please don't.. I'll do anything.. maybe you want to touch my body?.." """)
                        t("")
                        
                        answer="wrong_answer"
                        while answer!="0" or answer!="1":
                            
                            t("0[Kill Roro9, Roro6 will be next.]")
                            t("1[Fuck Roro9's brains out. she's a fine code piece, you want a hit from that]")
                            
                            answer=input("""
""")

                            restart_and_noneENTER_and_quit_function(answer)
                            
                            #if 0[Kill Roro9, Roro6 will be next.]
                            if answer=="0":
                                t("*{} declines Roro9's tempting offer and shoots her right in her head*".format(username))
                                
                                kill_roro6_ending(username)

                            #if 1[Fuck Roro9's brains out. she's a fine code piece, you want a hit from that]
                            elif answer=="1":
                                #get the achievement "get some from that piece of code"
                                t("*{} fucks Roro9 very hard for about an hour..*".format(username))
                                pause(0.85)
                                t("*then {} kills that piece of shit whore*".format(username))
                                
                                kill_roro6_ending(username)
                                
                                
            #if 2[code a crowbar and attack Roro6 with it]                    
            elif answer=="2":
                t("""Roro6: "Hey! what are you doing! Get away from me! GET OUT OF MY HOUSE YOU      LUNATIC" """)
                pause(0.33)
                t("")
                t("*{} grabs the crowbar and attacks Roro6's face, gouging his left coded  eye out from its place*".format(username))
                pause(0.23)
                t("*then {} codes a deadly knife made of math and stabs Roro6 in his belly     with ruthless rage*".format(username))
                pause(0.3)
                t("")
                t("""Roro6: "AHWTHaAhhh... Ahh..... R.. o. r.o9.. I .. Lov..... ah...h..... .. ... ." """)
                pause(0.3)
                t("")
                t("*Roro6 is now dead*")
                #get the achievement "MURDERER"
                pause(1.2)
                t("*His wife - Roro9 heard noise. she enters the living room*")
                pause(0.43)
                t("*Roro9 Screams*")
                pause(0.15)
                t("")
                t("""Roro9: "AHHHHHHH!!! WHAT IS THIS!!" """)
                pause(0.38)
                t("")
                t("""{}: "don't you worry babe.. I gotcha from now on" """.format(username))
                pause(0.48)
                t("")
                t("""Roro9: "You.. you killed m-my hus-b-band" """)
                pause(0.4)
                t("")
                t("""{}: "Yes. I have. How do you feel about it?" """.format(username))
                pause(0.9)
                t("")
                t("""Roro9: "oh.. Thank you!! finally!!! lets run off together! """)
                pause(0.15)
                t("""I'll have your children {}!" """.format(username))
                pause(0.4)
                t("")
                t("""{}: "That's more like it ;), come on baby. lets go!" """.format(username))
                pause(0.6)
                t("")
                t("*{} carries Roro9 on their way to a new life with a new love".format(username))
                pause(0.1)
                t("new desires, new hobbies, and alot more.")
                pause(0.14)
                t("A new page")
                pause(1)
                t("or..")
                pause(0.2)
                t("A coded new page.")
                #get the achievement "A new page"
                pause(4)
                the_end()
                        
                
                
            
            
            
#main game loop and the ability to restart

def main_menu():
    tn("""Welcome to "Roro6" """)
    t("")
    t("in order to start the game type 'start' ")
    t("")
    t("if you wish to restart while playing type 'restart' ")
    t("")
    t("if you wish to exit the game type 'quit' ")
    t("")

    answer="wrong_answer"
    while answer!="start":

        answer=input("""
""")
        
        if answer=="start":
            start_game()
        
        elif answer=="quit" or answer=="exit":
            sys.exit()

#beginning of game
                
main_menu()
            
            