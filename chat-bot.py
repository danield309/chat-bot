from random import choice

print("Welcome to voter bot!")
print("I will help you with steps on how to register, check if you're registered or update your current registration")
print("You may press done to exit the program at anytime.")

def get_vote_bot_response(user_response):

  bot_response_YES = ["Great! You can update your registration at https://www.vote.org/ if you need to."]
  bot_response_NO = ["Please head to https://www.vote.org/register-to-vote/ to register."]
  bot_response_IDK = ["No problem! Please head to https://www.vote.org/am-i-registered-to-vote/ to check if you are currently registered."]

  if user_response == "YES":
    return choice(bot_response_YES)
  elif user_response == "NO":
    return choice(bot_response_NO)
  elif user_response == "IDK":
    return choice(bot_response_IDK)
  else:
    return "Uh.. I didn't quite understand that."

user_response = ""

while True:
  user_response = input("Are you registered to vote? (YES/NO/IDK): ").upper()

  if user_response == 'done'.upper():
      break

  bot_response = get_vote_bot_response(user_response)
  print(bot_response)
