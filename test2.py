import tkinter as tk 
from tkinter import*
from tkinter import *
from PIL import ImageTk, Image
import random
import mysql.connector

lives = 3
heart_symbol = u'\u2764'
window = Tk()
window.geometry("1000x700+20+10")
window.title('Linear: The Stack Adventure Linked')

def update_score(player_name, game):
    # Connect to MySQL database
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Stressed0ut_Top",
        database="hangman_score"
    )
    cursor = cnx.cursor()

    # Insert the score into the scores table
    cursor.execute("INSERT INTO scores (name, score) VALUES (%s, %s)", (player_name, game.max_correct_answers))
    cnx.commit()

    
class SuicidalMan:
    def __init__(self):
        self.questions = {
            "Array stores data elements in adjacent location.": "True",
            "An Array has 5 classifications.": "False",
            "It is impossible to insert and delete data element in a linked list.": "False",
            "Stack is called last-in, first-out(LIFO).": "True",
            "In queues, the inserted elements is the last to be taken out.": "False"
        }

    def on_true_button(self):
        player_answer = "True"
        if player_answer == self.questions[current_question]:
            print("Well Done!")
        else:
            print("Try Again!")

    def on_false_button(self):
        player_answer = "False"
        if player_answer == self.questions[current_question]:
            print("Congratulations!")
        else:
            print("Mission Failed!")

    def display_question(self):
        global current_question
        current_question = random.choice(list(self.questions.keys()))
        print(current_question)

game = SuicidalMan()
current_question = None

# Start the game
#play_hangman()


def tab1(): #The home page
   def tab2(): #End part of the game
             #The .destroy() is added to destroy the lbl1, btn1, and btn2 of tab1() when it proceed to tab2()
             lbl1.destroy()
             btn1.destroy()
             btn2.destroy()

             lbl2 = Label(window, text = "Thank you for playing with us!!", font=("Times New Roman", 25))
             lbl2.pack(side = "top") #Position of the lbl2

   def tab3(): #Page/tab for instructions
             lbl1.destroy()
             btn1.destroy()
             btn2.destroy()
             img.destroy() #The .destroy() is added to destroy the img of tab1() when it proceed to tab3()
             SuicidalMan() #This will call out the function of the stickman

             #Instructions of the game
             lbl3 = Label(window, text = "The player will respond to the provided trivia, and you will have three", font =("Times New Roman", 18))
             lbl3.place(x=100, y=90) #Position of the lbl3
             lbl4 = Label(window, text = "chances to respond as well. Each incorrect answer will put you one", font = ("Times New Roman", 18))
             lbl4.place(x=100, y=130) #Position of the lbl4
             lbl5 = Label(window, text = "step closer to getting hung and force you to restart the game.", font = ("Times New Roman", 18))
             lbl5.place(x=100, y=170) #Position of the lbl4
             lbl6 = Label(window, text = "This game was design to increase the level of interaction when taking", font = ("Times New Roman", 18))
             lbl6.place(x=100, y=210) #Position of the lbl4
             lbl7 = Label(window, text = "a brainteaser. Examine the lesson you learned this semester once more.", font = ("Times New Roman", 18))
             lbl7.place(x=100, y=250) #Position of the lbl4
             def ext(): #this tab will destroy the labels and button of the tab3 when it proceeds on the next tab [tab4]
                     lbl3.destroy()
                     lbl4.destroy()
                     lbl5.destroy()
                     lbl6.destroy()
                     lbl7.destroy()
                     btn3.destroy()
                     tab4() #This will direct the user to the next tab
             #btn3 which directs the user to def ext() to destroy the labels and buttons of the tab3
             btn3 = Button(window, text = "Continue", font = ("Times New Roman", 16), command = ext)
             btn3.place(x=420, y=400) #Position of the btn3

#The home page
   lbl1 = Label(window, text = "Linear: The Stack Adventure Linked", font=("Times New Roman", 25)) #Name of the page/project
   lbl1.place(x=250, y=50) #Position of the lbl1
   btn1 = Button(window, text = "Start", font = ("Times New Roman", 14), command=tab3) #Start button which is connected to tab3
   btn1.place(x=450, y=500) #Position of the btn1
   btn2 = Button(window, text = "Exit", font = ("Times New Roman", 14), command=tab2) #Exit button which is connected to tab2
   btn2.place(x=450, y=600) #Position of the btn2

def tab4(): 
    #Page/tab for introduction of the game  

    lbl8 = Label(window, text="The New Era of Hangman", font=("Times New Roman", 18))
    lbl8.place(x=300, y=90) #Position of the lbl5
    lbl9 = Label(window, text="(La nueva era del ahorcado)", font=("Times New Roman", 18))
    lbl9.place(x=300, y=130) #Position of the lbl5
    lbl10 = Label(window, text="New Unique Features", font=("Times New Roman", 18))
    lbl10.place(x=300, y=170) #Position of the lbl5
    lbl11 = Label(window, text="(Nuevas caracteristicas unicas)", font=("Times New Roman", 18))
    lbl11.place(x=300, y=210) #Position of the lbl5
    lbl12 = Label(window, text="Created to make taking brain teaser more interactive.", font=("Times New Roman", 18))
    lbl12.place(x=200, y=250) #Position of the lbl5
    lbl13 = Label(window, text="Re-visit the lessonthat you've learned this semester.", font=("Times New Roman", 18))
    lbl13.place(x=200, y=290) #Position of the lbl5
            #Button that should direct the user to the questions
    def ext(): #this tab will destroy the labels and button of the tab3 when it proceeds on the next tab [tab4]
        lbl8.destroy()
        lbl9.destroy()
        lbl10.destroy()
        lbl11.destroy()
        lbl12.destroy()
        lbl13.destroy()
        tab5() #This will direct the user to the next tab
        btn4 = Button(window, text = "Continue", font = ("Times New Roman", 16), command = ext)
        btn4.place(x=420, y=400) #Position of the btn4

def tab5()  -> None: #This tab is for the questions or the main game
         print(" ------------------------------")
         print(" |                            |")
         print(" |    -Welcome ADVENTURER!-   |")
         print(" |                            |")
         print(" ______________________________")
         print("                             ")
         print("       ---ARE YOU READY?---")
         print("                                ") 
         print("         ---GOOD LUCK---   ") 
         print("______________________________")
         print("                                ") 

class HangingMan:
    def __init__(self, player_name):
        self.player_name = player_name
        self.questions = {
            "Array stores data elements in adjacent location.": "True",
            "An Array has 5 classifications.": "False",
            "It is impossible to insert and delete data element in a linked list.": "False",
            "Stack is called last-in, first-out (LIFO).": "True",
            "In queues, the inserted elements are the last to be taken out.": "False"
        }
        self.current_question = None
        self.wrong_answers = 0
        self.correct_answers = 0
        self.max_wrong_attempts = 3
        self.max_correct_answers = 5
        self.used_questions = set()

        self.stickman_parts = [
            """
              --------
              |      |
              |      O
              |     \\|/
              |      |
              |     / \\
           """,
           """
              --------
              |      |
              |      O
              |     \\|/
              |      |
              |     
           """,
           """
              --------
              |      |
              |      O
              |     
              |      
              |
           """
        ]

    def on_true_button(self):
        player_answer = "True"
        if player_answer == self.questions[self.current_question]:
            print("Well Done!")
            self.correct_answers += 1
        else:
            print("Try Again!")
            self.handle_wrong_answer()

        if self.correct_answers == self.max_correct_answers:
            print("Congratulations, Adventurer! Thank you for playing.")
            self.end_game()

    def on_false_button(self):
        player_answer = "False"
        if player_answer == self.questions[self.current_question]:
            print("Congratulations!")
            self.correct_answers += 1
        else:
            print("Mission Failed!")
            self.handle_wrong_answer()

        if self.correct_answers == self.max_correct_answers:
            print("Congratulations, Adventurer! Thank you for playing.")
            self.end_game()

    def display_question(self):
        remaining_questions = list(set(self.questions.keys()) - self.used_questions)
        if remaining_questions:
            self.current_question = random.choice(remaining_questions)
            self.used_questions.add(self.current_question)
            print(self.current_question)
        else:
            print("No more questions available. Game Over.")
            self.end_game()

    def handle_wrong_answer(self):
        self.wrong_answers += 1
        if self.wrong_answers == self.max_wrong_attempts:
            print("This is the end, Adventurer. Thank you for playing.")
            self.display_stickman()
            self.end_game()
        else:
            print(f"Wrong answer! You have {self.max_wrong_attempts - self.wrong_answers} attempts left.")
            self.display_stickman()

    def display_stickman(self):
        print(self.stickman_parts[self.wrong_answers - 1])

    def end_game(self):
        print("GAME OVER.")
        # Call the update_score function to update the score in the database
        update_score(self.player_name, self)

class QuizPage(tk.Frame):
    def __init__(self, master, game):
        super().__init__(master)
        self.game = game
        self.question_label = tk.Label(self, text="", font=("Arial", 16))
        self.question_label.pack(pady=50)
        self.true_button = tk.Button(self, text="True", command=self.game.on_true_button)
        self.true_button.pack()
        self.false_button = tk.Button(self, text="False", command=self.game.on_false_button)
        self.false_button.pack()
        self.next_button = tk.Button(self, text="Next", command=self.display_next_question)
        self.next_button.pack()

        self.display_next_question()

    def display_next_question(self):
        self.game.display_question()
        self.question_label.config(text=self.game.current_question)

def start_game(player_name):
    if player_name:
        print(f"Let's start the game, {player_name}!")
        game = HangingMan(player_name)
        start_page.destroy()
        show_quiz_page(game)
    else:
        print("Please enter your name.")

def show_quiz_page(game):
    quiz_page = QuizPage(root, game)
    quiz_page.pack()

root = tk.Tk()
root.title("Linear: The Stacked Adventure Linked")
root.geometry("1000x700+20+10")

start_page = tk.Frame(root)
start_page.pack()

start_label = tk.Label(start_page, text="Enter your name:", font=("Arial", 16))
start_label.pack()
name_entry = tk.Entry(start_page, font=("Arial", 16))
name_entry.pack()
start_button = tk.Button(start_page, text="Start", command=lambda: start_game(name_entry.get()))
start_button.pack() 

image_path = r"C:\Users\Mary Chelsea Magleo\Downloads\DSA\Database1\7.png"
pil_image = Image.open(image_path)
if pil_image.mode == 'RGB':
    pil_image = pil_image.convert('RGB')
image = ImageTk.PhotoImage(pil_image)
img = Label(window, image=image)
img.pack(side="top")

tab1() #To print out all the tabs
window.mainloop() #Loop


# Close the database connection
cursor.close()
cnx.close()