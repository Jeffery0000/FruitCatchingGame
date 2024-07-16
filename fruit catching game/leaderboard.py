#tkinter imports for UI
import tkinter
import tkinter.font as font
#Importing my other python files to access their functions
import my_login
import data_tool

#Function that creates the leaderboard menu
def create_leaderboard():
    #Creating the tkinter window
    leaderboard_menu = tkinter.Tk()
    leaderboard_menu.geometry("800x600")
    leaderboard_menu.title("Leaderboard")
    leaderboard_menu.resizable(False, False)

    users = data_tool.read() #Getting all users and storing them
    highest_scores = {}
    highest_user = "No one"
    #Loops through all users 5 times to find the 5 highest scores
    for i in range (5):
        highest_score = 0
        for user in users:
            if not (user["user"] in highest_scores) and (user["score"] > highest_score):
                highest_user = user["user"]
                highest_score = user["score"]
        highest_scores[highest_user] = highest_score

    #Creating the leaderboard text
    leaderboard_text = tkinter.Text(leaderboard_menu, wrap="word", width=800, height=600)
    leaderboard_text.insert(tkinter.END, "Rank\tUser\tScore\n")

    #Adding each highest score to the leaderboard text
    for i, (user, score) in enumerate(highest_scores.items(), 1):
        leaderboard_text.insert(tkinter.END, f"{i}\t{user}\t{score}\n")

    leaderboard_text.config(state=tkinter.DISABLED)
    leaderboard_text.place(x=0, y=0)

    #Function that closes this window and opens the main menu
    def to_main_menu():
        leaderboard_menu.destroy()
        my_login.create_main_menu()

    #Creating the back button
    text_font = font.Font(family="Eccentric Std", size=20, weight="bold")
    back_button = tkinter.Button(leaderboard_menu, text="Back", command=to_main_menu, font=text_font)
    back_button.place(x=700, y=10)