from tkinter import *
from tkinter import messagebox
import random

# Set random number and lives based on level
def set_number(level):
    if level == "easy":
        return "1-20", 4, random.randint(1, 20)
    elif level == "medium":
        return "1-50", 5, random.randint(1, 50)
    else:
        return "1-100", 7, random.randint(1, 100)

# End screen after win/loss
def forth_page():
    def yes_action():
        root.destroy()
        first_page()

    def no_action():
        root.destroy()
        exit()

    root = Tk()
    root.title("Play Again?")
    root.geometry("400x300")
    root.configure(bg='#856ff8')

    Label(root, text="Do you want to play again?", font=('Helvetica 16 bold'), bg='#856ff8', fg='#18122B').pack(pady=50)
    Button(root, text='Yes', command=yes_action, font=('Helvetica 10'), bg="#443C68", fg="#ffffff").pack(pady=10)
    Button(root, text='No', command=no_action, font=('Helvetica 10'), bg="#cc3549", fg="#ffffff").pack()

    root.mainloop()

# Game logic screen
def third_page(level, player_name):
    HEARTS = []
    heading_text, hearts, number = set_number(level)
    HEARTS.append(hearts)

    def write_to_file(status):
        with open("log.txt", "a") as file:
            file.write(f"{player_name} {status}\n")

    def play_game(guess):
        if int(guess) == number:
            return 1
        HEARTS[0] -= 1
        hearts_text['text'] = str(HEARTS[0])
        if int(guess) > number:
            return 2
        else:
            return 3

    def submit():
        guess = inputtxt.get(1.0, "end-1c")
        if not guess.isdigit():
            messagebox.showerror("Error", "Enter a valid number.")
            return
        result = play_game(guess)
        if HEARTS[0] <= 0 and result != 1:
            messagebox.showerror("Game Over", f"You lost! The number was {number}")
            write_to_file("lost")
            root.destroy()
            forth_page()
        elif result == 1:
            messagebox.showinfo("Congrats!", "You won!")
            write_to_file("won")
            root.destroy()
            forth_page()
        elif result == 2:
            messagebox.showinfo("Try Again", "Go down!")
        else:
            messagebox.showinfo("Try Again", "Go up!")

    root = Tk()
    root.title("Guessing Game")
    root.geometry("400x400")
    root.configure(bg='#856ff8')

    Label(root, text=f"Hi {player_name}", font=('Helvetica 18 bold'), bg='#856ff8', fg='#18122B').place(y=30, relx=0.5, anchor='center')
    Label(root, text=f"Choose a number between {heading_text}", font=('Helvetica 12'), bg='#856ff8', fg='#18122B').place(y=70, relx=0.5, anchor='center')
    
    Label(root, text="❤️", font=('Helvetica 14'), bg='#856ff8', fg='#18122B').place(x=5, y=10)
    hearts_text = Label(root, text=str(hearts), font=('Helvetica 12'), bg='#856ff8', fg='#18122B')
    hearts_text.place(x=30, y=10)

    inputtxt = Text(root, height=2, width=20)
    inputtxt.place(y=120, relx=0.5, anchor='center')

    Button(root, text='Submit', command=submit, font=('Helvetica 10'), bg="#443C68", fg="#ffffff").place(y=170, width=80, relx=0.5, anchor='center')
    root.mainloop()

# Level selection screen
def second_page(player_name):
    def game_window(level):
        root.destroy()
        third_page(level, player_name)

    root = Tk()
    root.title("Select Difficulty")
    root.geometry("400x400")
    root.configure(bg='#856ff8')

    Label(root, text=f"Hi {player_name}", font=('Helvetica 18 bold'), bg='#856ff8', fg='#18122B').place(y=40, relx=0.5, anchor='center')
    Label(root, text='Choose difficulty level:', font=('Helvetica 12'), bg='#856ff8', fg='#18122B').place(y=80, relx=0.5, anchor='center')

    Button(root, text='Easy', command=lambda: game_window("easy"), font=('Helvetica 10'), bg="#443C68", fg="#ffffff").place(y=130, width=80, relx=0.5, anchor='center')
    Button(root, text='Medium', command=lambda: game_window("medium"), font=('Helvetica 10'), bg="#443C68", fg="#ffffff").place(y=170, width=80, relx=0.5, anchor='center')
    Button(root, text='Hard', command=lambda: game_window("hard"), font=('Helvetica 10'), bg="#443C68", fg="#ffffff").place(y=210, width=80, relx=0.5, anchor='center')

    root.mainloop()

# Entry screen
def first_page():
    def submit():
        name = inputtxt.get(1.0, "end-1c").strip()
        if name:
            root.destroy()
            second_page(name)
        else:
            messagebox.showerror("Input Error", "Please enter your name.")

    root = Tk()
    root.title("Welcome")
    root.geometry("400x400")
    root.configure(bg='#856ff8')

    Label(root, text='Welcome to the Guessing Game!', font=('Helvetica 16 bold'), bg='#856ff8', fg='#18122B').place(y=50, relx=0.5, anchor='center')
    Label(root, text='Enter your name:', font=('Helvetica 12'), bg='#856ff8', fg='#18122B').place(y=100, relx=0.5, anchor='center')

    inputtxt = Text(root, height=2, width=20)
    inputtxt.place(y=140, relx=0.5, anchor='center')

    Button(root, text='Start', command=submit, font=('Helvetica 10'), bg="#443C68", fg="#ffffff").place(y=190, width=80, relx=0.5, anchor='center')

    root.mainloop()

# Run the game
first_page()
