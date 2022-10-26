from game_data import data
import random
from art import logo, vs
from replit import clear

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers): 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  aRandom = random.choice(data)
  bRandom = random.choice(data)

  while game_should_continue:
    aRandom = bRandom
    bRandom = random.choice(data)

    while aRandom == bRandom:
      account_b = random.choice(data)

    print(f"Compare A: {format_data(aRandom)}.")
    print(vs)
    print(f"Against B: {format_data(bRandom)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = aRandom["follower_count"]
    b_follower_count = bRandom["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()