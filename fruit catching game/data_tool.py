import json #Importing json to work with the json file

#Function that creates a new account
def new_account(username, password):
  #Opens json file and stores the information in data
  try:
    with open("stats.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    data = []

  #Adding a new user to the data array
  data.append({"user": username, "pass": password, "score": 0, "coin": 0, "item": 0})

  #Writing the new data to the json file
  with open("stats.json", "w") as file:
    json.dump(data, file, indent=2)

#Function that updates user's high score
def update_score(user, score):
  #Opens json file and stores the information in data
  try:
    with open("stats.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    print("File not found.")

  #Updating the user's score
  data[user]["score"] = score

  #Writing the new data to the json file
  with open("stats.json", "w") as file:
    json.dump(data, file, indent=2)

#Function that updates user's coins
def update_coin(user, coin):
  #Opens json file and stores the information in data
  try:
    with open("stats.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    print("File not found.")

  #Updating the user's coins
  data[user]["coin"] = coin

  #Writing the new data to the json file
  with open("stats.json", "w") as file:
    json.dump(data, file, indent=2)

#Function that updates user's items
def update_items(users):
  #Taking in all users' informations and storing it
  data = users

  #Writing the new data to the json file
  with open("stats.json", "w") as file:
    json.dump(data, file, indent=2)

#Function that reads the json file
def read():
  #Opens json file and storing it in data
  try:
    with open("stats.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    return []
  #Returning the data
  return data