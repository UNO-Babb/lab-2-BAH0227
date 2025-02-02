#Magic8Ball.py
#Name: Brock Hoover
#Date: 1/29/2025
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  input("Enter a Prompt Here: ")
  answers = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
             "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.",
             "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", 
             "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes, definitely.", "You may rely on it"]  
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * length
  
  r = int(r) #cut off any decimal values
  response = answers[r]
  print(response)
if __name__ == '__main__':
  main()
