from random import choice

print("Welcome to voter bot!")
print("I will help you with steps on how to register, check if you're registered or update your current registration")
print("You may press done to exit the program at anytime.")

def get_vote_bot_response(user_response):

  bot_response_YES = ["Great! You can update your registration at https://www.vote.org/ if you need to."]
  bot_response_NO = ["Please head to https://www.vote.org/ to register."]
  bot_response_IDK = ["No problem! Please head to https://www.vote.org/ to check if you are currently registered."]
