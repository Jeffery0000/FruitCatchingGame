#tkinter imports for UI
import tkinter
from tkinter import messagebox
import tkinter.font as font
#Importing my other python files to access their functions
import game
import data_tool as data
import leaderboard
import shop

#Function that verifies logins
def login():
    #Creates a global variable to make the current user accessible anywhere
    global current_user
    #Getting the text in the entries
    username = entry_username.get()
    password = entry_password.get()
    users = data.read() #Storing all user information after reading json file with data tool
    wrong = True
    counter = 0 #Counter used to count which user is currently being worked on
    #Loops through each users
    for user in users:
        #Checks if the username and password entered matches existing ones
        if user["user"] == username and user["pass"] == password:
            messagebox.showinfo("Login", "Login successful!")
            wrong = False
            current_user = counter
            login_window.destroy()
            create_main_menu()
        counter += 1
    #If the username and password matches no existing ones, an error is shown
    if wrong:
        messagebox.showerror("Login", "Invalid username or password.")
    return

#Function that verifies signups
def signup():
    #Getting the text in the entries
    username = new_username.get()
    password = new_password.get()
    users = data.read() #Storing all user information after reading json file with data tool
    #Looping through each user to check if the username already exists
    for user in users:
        #Error message is shown if the username already exists
        if user["user"] == username:
            messagebox.showerror("Signup", "Username already exists.")
            return
    #If username doesn't exist, the new account is created and written to json file
    data.new_account(username, password)
    messagebox.showinfo("Signup", "Signup successful!")
    signup_window.destroy()
    create_login_menu()

#Function that creates the window for login
def create_login_window():
    login_menu.destroy() #Deletes login menu to replace it
    global login_window, entry_username, entry_password #Creating global variables so they can be accessed anywhere
    #Creating tkinter window
    login_window = tkinter.Tk()
    login_window.geometry("800x600")
    login_window.title("Login")

    #Font for buttons and texts
    text_font = font.Font(family="Eccentric Std", size=20, weight="bold")

    #Creating labels, entries and buttons
    label_username = tkinter.Label(login_window, text="Username", font=text_font)
    label_username.place(x=335, y=80)

    entry_username = tkinter.Entry(login_window, width=15, font=text_font, borderwidth=2)
    entry_username.place(x=285, y=120, height=40)

    label_password = tkinter.Label(login_window, text="Password", font=text_font)
    label_password.place(x=335, y=180)

    entry_password = tkinter.Entry(login_window, show="*", font=text_font, borderwidth=2, width=15)
    entry_password.place(x=285, y=220, height=40)

    login_button = tkinter.Button(login_window, text="Login", command=login, font=text_font, borderwidth=4)
    login_button.place(x=350, y=270)

    #Function that closes this window and replaces it with the login menu
    def back_from_login():
        login_window.destroy()
        create_login_menu()

    back_button = tkinter.Button(login_window, text="Back", command=back_from_login, font=text_font, borderwidth=4)
    back_button.place(x=354, y=340)
    login_window.mainloop()

#Function that creates the window for signup
def create_signup_window():
    login_menu.destroy() #Deletes login menu to replace it
    global signup_window, new_username, new_password #Creating global variables so they can be accessed anywhere
    #Creating the tkinter window
    signup_window = tkinter.Tk()
    signup_window.geometry("800x600")
    signup_window.title("Signup")

    #Font for buttons and texts
    text_font = font.Font(family="Eccentric Std", size=20, weight="bold")

    #Creating labels, entries and buttons
    label_username = tkinter.Label(signup_window, text="Username", font=text_font)
    label_username.place(x=335, y=80)

    new_username = tkinter.Entry(signup_window, width=15, font=text_font, borderwidth=2)
    new_username.place(x=285, y=120, height=40)

    label_password = tkinter.Label(signup_window, text="Password", font=text_font)
    label_password.place(x=335, y=180)

    new_password = tkinter.Entry(signup_window, show="*", font=text_font, borderwidth=2, width=15)
    new_password.place(x=285, y=220, height=40)

    signup_button = tkinter.Button(signup_window, text="Sign up", command=signup, font=text_font, borderwidth=4)
    signup_button.place(x=335, y=270)

    #Function that closes this window and replaces it with the login menu
    def back_from_signup():
        signup_window.destroy()
        create_login_menu()

    back_button = tkinter.Button(signup_window, text="Back", command=back_from_signup, font=text_font, borderwidth=4)
    back_button.place(x=354, y=340)
    signup_window.mainloop()

#Function that creates the login menu
def create_login_menu():
    global login_menu #Making the menu a global varible so it can be accessible anywhere
    #Creating the tkinter window
    login_menu = tkinter.Tk()
    login_menu.geometry("800x600")
    login_menu.title("Login Menu")

    #Font for buttons and texts
    text_font = font.Font(family="Eccentric Std", size=20, weight="bold")

    #Creating the buttons
    login_button = tkinter.Button(login_menu, text="Login", command=create_login_window
                                  , width=7, height=1, borderwidth=5, font=text_font)
    login_button.place(x=335, y=150)

    signup_button = tkinter.Button(login_menu, text="Signup", command=create_signup_window
                                   , width=7, height=1, borderwidth=5, font=text_font)
    signup_button.place(x=335, y=230)

    login_menu.mainloop()

#Function that creates the main menu
def create_main_menu():
    global main_menu #Making the menu a global varible so it can be accessible anywhere
    #Creating the tkinter window
    main_menu = tkinter.Tk()
    main_menu.geometry("800x600")
    main_menu.title("Main Menu")

    #Font for buttons and texts
    text_font = font.Font(family="Eccentric Std", size=20, weight="bold")

    #Function that closes this menu and runs the game
    def play():
        main_menu.destroy()
        game.show_game(current_user)
    #Creating the buttons
    play_button = tkinter.Button(main_menu, text="Play", command=play
                                 , width=7, height=1, borderwidth=5, font=text_font)
    play_button.place(x=335, y=150)

    #Function that closes this menu and opens the shop
    def open_shop():
        main_menu.destroy()
        shop.create_shop(current_user)
        pass
    shop_button = tkinter.Button(main_menu, text="Shop", command=open_shop
                                 , width=7, height=1, borderwidth=5, font=text_font)
    shop_button.place(x=335, y=230)

    #Function that closes this menu and opens the leaderboard
    def open_leaderboard():
        main_menu.destroy()
        leaderboard.create_leaderboard()
    leaderboard_button = tkinter.Button(main_menu, text="Leaderboard", command=open_leaderboard
                                        , width=14, height=1, borderwidth=5, font=text_font)
    leaderboard_button.place(x=275, y=310)

    #Function that closes this menu and opens the login menu
    def logout():
        main_menu.destroy()
        create_login_menu()
    logout_button = tkinter.Button(main_menu, text="Logout", command=logout
                                        , width=7, height=1, borderwidth=5, font=text_font)
    logout_button.place(x=335, y=380)

    #Getting the user's coins and high score to show on the menu
    users = data.read()
    coins = users[current_user]["coin"]
    coins_text = tkinter.Label(main_menu, text="Coins: " + str(coins), font=text_font)
    coins_text.place(x=550, y=10)

    highscore = users[current_user]["score"]
    highscore_text = tkinter.Label(main_menu, text="High score: " + str(highscore), font=text_font)
    highscore_text.place(x=550, y=50)

    main_menu.mainloop()