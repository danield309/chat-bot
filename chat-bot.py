from random import choice #import will give access to random module/library - choice will randomly return an element in list
#Welcome to Vote Bot
print("Welcome to voter bot!")
print("I will help you with steps on how to register, check if you're registered or update your current registration.")
print("You may press done to exit the program at anytime.")
#Function that responds to user input
def get_vote_bot_response(user_response):

  bot_response_YES = ["Great!", "Cool! You can update your registration at https://www.vote.org/ if you need to.", "Awesome make sure to vote!"]
  bot_response_NO = ["Please head to https://www.vote.org/register-to-vote/ to register.", "Oh no! Register @ https://www.vote.org/register-to-vote/ your vote matters <3.", "Biden or Trump won't get elected without your say head to https://www.vote.org/register-to-vote/ to register." ]
  bot_response_IDK = ["No problem! Head to https://www.vote.org/am-i-registered-to-vote/ to check if you are currently registered.", "To know if you are or aren't registered head to https://www.vote.org/am-i-registered-to-vote/", "No worries you can check your registration status at https://www.vote.org/am-i-registered-to-vote/ ."]

#Takes user input and ties it to the correct bot reponse above

  if user_response == "YES":
    return choice(bot_response_YES)
  elif user_response == "NO":
    return choice(bot_response_NO)
  elif user_response == "IDK":
    return choice(bot_response_IDK)
  else:
    return "Uh.. I didn't quite understand that."

user_response = ""

#Loop that keeps the function running until the user inputs 'done'

while True:

  user_response = input("Are you registered to vote? (YES/NO/IDK): ").upper()

#Quits the program if the user inputs 'done'

  if user_response == 'done'.upper():
      break
#Prints bot and user response
  bot_response = get_vote_bot_response(user_response)
  print(bot_response)
