# INT Course - who_wants_to_be_a_millionaire - Python Project By Or Karp, aka 'Karpo'
import sys
import time
import csv
import pickle
from random import randint
from pygame import mixer

# initializing the mixer
mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
# music file made by me
mixer.music.load("Music_Sound_Files\\theme_for_questions_mp3_MASTERED.mp3")
mixer.music.set_volume(0.1)

# defining the winning sound file
winning_sound_hurray = mixer.Sound("Music_Sound_Files\\You_Win.wav")
winning_sound_hurray.set_volume(0.1)

# defining the cheering crowd sound file
cheering_crowd = mixer.Sound("Music_Sound_Files\\Cheering_Crowd.wav")
cheering_crowd.set_volume(0.1)

def music(stop=None):
    # play's music until stop=="stop"
    if stop == "stop":
        mixer.music.stop()
        return
    mixer.music.play(-1)

def print(self):
    # replaces the regular print with a typing characters one
    for i in self:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.0255)
    sys.stdout.write("\n")


class MyGame:
    def __init__(self):
        # a list that will contain the questions that has already been asked
        self.asked_questions = []

    def main_menu(self):
        print("Welcome to 'Who Wants To Be A Millionaire'!!!\n")
        print("If You'd like to start the game please type 'start'")
        print("If You'd like to see the ScoreBoard type 'sb'")
        print("If You'd like to quit type 'quit'")
        return self.main_menu_cont()

    def main_menu_cont(self):
        main_menu_options = ["START", "SB", "QUIT"]

        # checking if the user wants to start or show the ScoreBoard or quit
        try:
            answer = take_input_from_user("upper")
            if answer not in main_menu_options:
                return self.main_menu_cont()

            if answer == "START":
                return self.signing_in_out_menu()
            elif answer == "SB":
                return self.show_score_board()

        except FileNotFoundError:
            print("ScoreBoard does not exist yet!! please play a game first!\n")
            return self.main_menu_cont()

    def signing_in_out_menu(self):
        print("Before we begin you need to login. (or sign up incase you haven't yet)\n")
        print("In order to login type 'login'")
        print("and in order to sign up type 'sign up'")
        print("You can also play as a guest if you want! in order to do that type 'guest'")
        return self.signing_in_out_menu_cont()

    def signing_in_out_menu_cont(self):
        signing_in_out_menu_options = ["LOGIN", "SIGN UP", "GUEST"]

        # getting the nickname input from the user
        login_or_sign_up_guest = take_input_from_user("upper")
        if login_or_sign_up_guest not in signing_in_out_menu_options:
            return self.signing_in_out_menu_cont()

        if login_or_sign_up_guest == "SIGN UP":
            user_name = username_data_base.sign_up()
        elif login_or_sign_up_guest == "LOGIN":
            user_name = username_data_base.login()
        elif login_or_sign_up_guest == "GUEST":
            user_name = username_data_base.guest()

        return user_name


    def questions_execution(self):
        # welcoming the contestant
        print("Hello %s! Lets! See! Who! Wants! To Be! A Millionaire!! *cheering crowd*\n" % (user_name_account.username))
        cheering_crowd.play()
        time.sleep(4)
        print("...\n")
        time.sleep(5)

        music()

        # for loop's range is between 1 to 11 because there's going to be 10 questions in each playthrough
        for i in range(1, 11):
            # if its the first question which means it's an easy diff question so reset the asked questions
            if i == 1:
                self.asked_questions = []
                difficulty = "easy"

            # if its the fifth question which means it's a medium diff question so reset the asked questions
            elif i == 5:
                self.asked_questions = []
                difficulty = "medium"

            # if its the Eighth question which means it's a hard diff question so reset the asked questions
            elif i == 8:
                self.asked_questions = []
                difficulty = "hard"

            self.questions_template(check_question_number(i),difficulty)

        # after the 10 questions are finished execute the you_win() function
        return self.you_win()


    def questions_template(self,question_number, easy_medium_hard):
        print(question_number + " Question!")
        print("Difficulty: %s\n" % (easy_medium_hard))
        num = generate_random_num()

        # checks if it's a question that has already been asked
        while True:
            if num in self.asked_questions:
                num = generate_random_num()
            else:
                break

        # the system shows the question and also getting info about its answer
        correct_answer_o_question = self.show_questions(num, easy_medium_hard).rstrip()
        # adding the answer to the asked questions list so that it wouldn't come up again
        self.asked_questions.append(num)
        # checking the answer and responds accordingly
        self.check_answer(correct_answer_o_question, easy_medium_hard)

    def show_questions(self,num, easy_medium_hard):
        with open("Questions.txt", "r") as f:
            content = f.readlines()
        column = 5

        while True:
            for i in content:
                find_line_num = content.index(i)

                if len(i.split()) == 0 or ("Question Number") not in i:
                    pass

                elif i.split()[2].rstrip() == str(num) and i.split()[-1].rstrip() == easy_medium_hard:
                    correct_answer = content[find_line_num + 1 + column].rstrip()

                    for i in range(column):
                        print(content[find_line_num + 1 + i].rstrip())
                    return correct_answer

                else:
                    pass

    def check_answer(self, correct_answer, diff):
        # checking the user's answer input and responding accordingly
        user_answer = take_input_from_user("upper")
        if user_answer != correct_answer:
            print(self.wrong_answer(diff))
            return self.check_answer(correct_answer, diff)
        print(self.correct_answer(user_name, diff))

    def correct_answer(self, user_name, diff):
        # adds points to the user's score based on the difficulty of the question
        if diff == "easy":
            user_name_account.score += self.return_points_to_add(diff)
        elif diff == "medium":
            user_name_account.score += self.return_points_to_add(diff)
        elif diff == "hard":
            user_name_account.score += self.return_points_to_add(diff)
            return "Wow!! That was a tough one %s. Nice Job.\n" %(user_name)
        return "Correct answer!!! Way to go %s!\n" %(user_name)

    def wrong_answer(self, diff):
        # lowers the user's score based on the difficulty of the question
        if diff == "easy":
            user_name_account.score -= self.return_points_to_add(diff)
        elif diff == "medium":
            user_name_account.score -= self.return_points_to_add(diff)
        elif diff == "hard":
            user_name_account.score -= self.return_points_to_add(diff)
        return "WRONG!!! Try again please!"

    def return_points_to_add(self,diff):
        if diff == "easy":
            return 5.5
        elif diff == "medium":
            return 7
        elif diff == "hard":
            return 9

    def you_win(self):
        music("stop")
        # playing winning sounds - you won hurray!
        winning_sound_hurray.play()
        # game is finished, congratulating the contestant and telling him how much points he scored, 70 is the highest score possible
        print("Congratulations %s! You've made it to the end of the game! And your score is: %s\n" % (user_name_account.username, str(user_name_account.score)))
        # saving score into the ScoreBoard
        self.put_score_in_scoreboard()

    def put_score_in_scoreboard(self):
        content = []

        try:
            with open("Score_Board.csv", "r") as r:
                # reader reading the csv file
                reader = csv.reader(r)

                # content = all the rows in the csv file
                for row in reader:
                    content.append(row)

                # highest_score becoming a tuple of the name and score only.
                highest_score = (content[0][1], content[0][3])

                # second_score becoming a tuple of the and score only of the second row
                second_score = (content[1][1], content[1][3])

                # third_score becoming a tuple of the and score only of the third row
                third_score = (content[2][1], content[2][3])

                # creating a dict that contains all names : scores that are in the scoreboard file
                scoreBoard_contestants_and_scores = {highest_score[0]:highest_score[1] ,second_score[0]:second_score[1] ,third_score[0]:third_score[1]}

            list_of_scores = [highest_score, second_score, third_score]
            # updates variables according to their values
            for i in range(len(list_of_scores)):
                # checking if the first place at the scoreboard is smaller than the score given to the function
                if float(list_of_scores[i][1]) <= float(user_name_account.score):

                    temp = list_of_scores[i]

                    # checks if the same user has already finished the game with this recurring amount of score
                    for name,score in scoreBoard_contestants_and_scores.items():
                        if user_name_account.username == name and str(user_name_account.score) == score:
                            return

                    # goes in if its the highest_score element
                    if i == 0:
                        # saves second_score's info inside temp_2
                        temp_2 = second_score

                        highest_score = user_name_account.username, user_name_account.score
                        second_score = temp[0], temp[1]
                        third_score = temp_2[0], temp_2[1]
                        break


                    # goes in if it's the second_score element
                    elif i == 1:
                        third_score = temp[0], temp[1]
                        second_score = user_name_account.username, user_name_account.score
                        break

                    # goes in if its the third_score element
                    else:
                        third_score = user_name_account.username, user_name_account.score
                        break

            # recreating list_of_scores so the variables inside would update
            list_of_scores = [highest_score, second_score, third_score]
            with open("Score_Board.csv", "w") as w:
                for i in range(len(list_of_scores)):
                    w.write("%i. ,%s, : ,%s, points" % (i + 1, list_of_scores[i][0], list_of_scores[i][1]))
                    w.write("\n")


        except Exception as e:

            # if there's no scoreboard yet it creates one and putting the contestant in it as first place
            with open("Score_Board.csv", "w") as w:
                w.write("1. ,%s, : ,%s, points\n"
                        "2. ,Empty, : ,0, points\n"
                        "3. ,Empty, : ,0, points" %(user_name_account.username, user_name_account.score))

    def show_score_board(self):
        # printing every row from the Score_Board.csv file
        with open("Score_Board.csv", "r") as r:
            reader = csv.reader(r)
            for row in reader:
                string = ""
                for word in row:
                    string += word
                print(string)

        print("\nIn order to get back to the main menu please type 'main menu'")
        print("or type 'quit' if you want to exit the game")
        answer = take_input_from_user("lower")
        while answer != 'main menu':
            answer = take_input_from_user("lower")
        return self.main_menu()


class UsernameDatabase(MyGame):
    def __init__(self):
        self.users = {}
        self.list_of_login_sign_up_guest = ["Login", "Sign up", "Guest"]

    def add_to_Usernames_pickle_file(self, account="Demo_User_1$%3@3!", password="Demo_Password_2$@1%6$%"):
        try:
            with open("Usernames.txt", "rb") as r:
                content = pickle.load(r)
                content = list(content)
                for i in content:
                    self.users[i[0]] = i[1]

            if account != "Demo_User_1$%3@3!":
                with open("Usernames.txt", "wb") as w:
                    content.append([account, password])
                    pickle.dump(content, w)
                self.users[account] = password

        except Exception as e:
            # print(e)
            with open("Usernames.txt", "wb") as w:
                pickle.dump([account, password], w)

    def check_signup_login_or_guest(self,user_answer):
        if user_answer == "Login":
            return self.login()
        elif user_answer == "Sign up":
            return self.sign_up()
        elif user_answer == "Guest":
            return self.guest()

    def sign_up(self):
        # asking for a username from the user
        print("Signing Up:\n")
        print("Please enter your Username: ")
        username = take_input_from_user("cap")

        # checking if user wants to login or be a guest
        if username in self.list_of_login_sign_up_guest:
            return self.check_signup_login_or_guest(username)

        # checking if the username already exists in the database, and if it isn't it asks for a password
        elif not self.check_if_user_exists(username):
            print("Please enter your password: ")
            password = input()
            # adds the user to the system and goes to the login menu with the login() function
            # self.users[username] = password
            self.add_to_Usernames_pickle_file(username,password)
            print("Congratulations %s! Your account was made. Transfering you to the login menu."%(username))
            return self.login()

        # if the username is already taken it relaunches the function
        print("This username is already taken!! please use a different username."
              " or type 'login' in order to log into your existing account"
              "or type 'guest' if you'd prefer not to sign up")
        return self.sign_up()

    def login(self):
        print("\nLogging in:\n")

        # user typing in his username
        print("Please enter your Username: ")
        username = take_input_from_user("cap")

        # checking if user wants to sign up or be a guest instead of logging in
        if username in self.list_of_login_sign_up_guest:
            return self.check_signup_login_or_guest(username)

        # making sure the username the user types in does in fact exist
        elif not self.check_if_user_exists(username):
            print("This account doesn't exist in the user database!\n"
                  "please type a different username or type 'sign up' if you havent signed up yet"
                  " or type 'guest' if you'd prefer not to sign up")
            return self.login()

        # user typing in his password
        print("Please enter your password: ")
        password = input()

        # making sure the username and password does match up and exist in the username database
        for user,pin in self.users.items():
            if user == username and pin == password:
                return username

        print("Wrong password!! Please try logging in again.")
        return self.login()

    def guest(self):
        # takes a nickname from the user
        print("Please enter your guest name(nickname): \n")
        username = take_input_from_user("cap")

        # checking if user wants to sign up or login
        if username in self.list_of_login_sign_up_guest:
            return self.check_signup_login_or_guest(username)

        # if the name is taken:
        elif self.check_if_user_exists(username):
            print("This nickname already exists in the user database!\n"
                  "please type a different nickname or type 'sign up'"
                  " if you haven't signed up yet or type 'login' if you wish to log into your existing account\n")
            return self.guest()

        return username

    def check_if_user_exists(self,user):
        if user in self.users.keys():
            return True
        return False


class Username(UsernameDatabase):
    def __init__(self,username):
        self.username = username
        self.score = 0


def take_input_from_user(lower_upper_cap):
    string = input()

    if string.lower() == "quit":
        print("Bye Bye now! Until next time.")
        sys.exit()

    if lower_upper_cap == "cap":
        return string.capitalize()
    elif lower_upper_cap == "lower":
        return string.lower()
    elif lower_upper_cap == "upper":
        return string.upper()

def generate_random_num():
    # the randint is between 1 and 15 because there's only 15 questions in each difficulty section
    num = randint(1, 15)
    return num

def check_question_number(num):
    if num == 1:
        return "First"
    if num == 2:
        return "Second"
    if num == 3:
        return "Third"
    if num == 4:
        return "Fourth"
    if num == 5:
        return "Fifth"
    if num == 6:
        return "Sixth"
    if num == 7:
        return "Seventh"
    if num == 8:
        return "Eighth"
    if num == 9:
        return "Ninth"
    if num == 10:
        return "Tenth"


# creating the Game object
mygame = MyGame()
# creating the username database
username_data_base = UsernameDatabase()
# calling the function that reads the Usernames.txt file and updates the username_data_base.users accordingly
username_data_base.add_to_Usernames_pickle_file()

# actual start of the game
while True:
    # main_menu, also getting the nickname of the user
    user_name = mygame.main_menu()

    # creating the Username object
    user_name_account = Username(user_name)

    # starting the game with the contestant
    mygame.questions_execution()
    # going back to main menu after the loop finished
