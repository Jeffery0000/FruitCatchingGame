#tkinter imports for UI
import tkinter
import tkinter.font as font
#Importing my other python files to access their functions
import my_login
import data_tool

#Function that creates the shop menu
def create_shop(current_user):
    #Creating the tkinter menu
    shop_menu = tkinter.Tk()
    shop_menu.geometry("800x600")
    shop_menu.title("Shop")
    shop_menu.resizable(False, False)

    #Function that closes this menu and opens the main menu
    def to_main_menu():
        shop_menu.destroy()
        my_login.create_main_menu()

    #Font for texts and buttons
    text_font = font.Font(family="Eccentric Std", size=20, weight="bold")
    #Creating the back button
    back_button = tkinter.Button(shop_menu, text="Back", command=to_main_menu, font=text_font, borderwidth=5)
    back_button.place(x=10, y=10)

    users = data_tool.read() #Getting user information
    #Creating arrays of item information
    items = ["Wooden Basket", "Bronze Basket", "Silver Basket", "Gold Basket", "Emerald Basket", "Diamond Basket"]
    items_info = ["5 Lives\n+1 coin\n+1 score",
                  "6 Lives\n+1 coin\n+1 score",
                  "7 Lives\n+2 coin\n+2 score",
                  "7 Lives\n+3 coin\n+2 score",
                  "8 Lives\n+4 coin\n+2 score",
                  "10 Lives\n+5 coin\n+3 score"]
    items_cost = [0, 30, 80, 145, 200, 1000]

    #Setting the items informations to the user's and their next item
    user_item = users[current_user]["item"]
    item_text = items[user_item]
    item_info = items_info[user_item]
    item_cost = items_cost[user_item]
    if user_item < 5:
        next_item = items[user_item + 1]
        next_info = items_info[user_item + 1]
        next_cost = items_cost[user_item + 1]
    else:
        next_item = "None"
        next_info = "None"
        next_cost = 123456789

    #Creating the texts
    item_label = tkinter.Label(shop_menu, text="Current Item: ", font=text_font)
    item_label.place(x=130, y=130)
    item_title = tkinter.Label(shop_menu, text=item_text, font=text_font)
    item_title.place(x=130, y=160)
    item_info = tkinter.Label(shop_menu, text=item_info, font=text_font)
    item_info.place(x=130, y=210)
    cost_label = tkinter.Label(shop_menu, text="Cost: " + str(item_cost), font=text_font)
    cost_label.place(x=130, y=370)

    next_label = tkinter.Label(shop_menu, text="Next Item: ", font=text_font)
    next_label.place(x=475, y=130)
    next_title = tkinter.Label(shop_menu, text=next_item, font=text_font)
    next_title.place(x=475, y=160)
    next_info = tkinter.Label(shop_menu, text=next_info, font=text_font)
    next_info.place(x=475, y=210)
    next_costlabel = tkinter.Label(shop_menu, text="Cost: " + str(next_cost), font=text_font)
    next_costlabel.place(x=475, y=370)

    coins = users[current_user]["coin"]
    coins_label = tkinter.Label(shop_menu, text="Coins: " + str(coins), font=text_font)
    coins_label.place(x=360, y=55)

    #Function that upgrades the user's item
    def upgrade():
        nonlocal coins
        #User's item is upgraded if they have enough coins and the item isn't the last one
        if next_cost <= coins and user_item < 5:
            users[current_user]["coin"] -= next_cost
            users[current_user]["item"] = user_item + 1
            data_tool.update_items(users)
            shop_menu.destroy()
            create_shop(current_user)

    #Creating the upgrade button
    upgrade_button = tkinter.Button(shop_menu, text="Upgrade", command=upgrade, font=text_font, borderwidth=5)
    upgrade_button.place(x=335, y=450)

    shop_menu.mainloop()