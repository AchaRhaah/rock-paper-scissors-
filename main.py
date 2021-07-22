import random
guess=int(input("enter 0 for rock, 1 for paper, and 2 for scissors "))
computer_guess=random.randint(0,2)
print(computer_guess)
if computer_guess == 0 and guess == 1:
  print("YOU WIN")
elif computer_guess == 0 and guess ==2 :
  print("you loose")
elif computer_guess == 1 and guess==0:
  print("you loose")
elif computer_guess == 1 and guess==2:
  print("YOU WIN")
elif computer_guess == 2 and guess==0:
  print("YOU WIN")
elif computer_guess == 2 and guess==1:
  print("you loose")


