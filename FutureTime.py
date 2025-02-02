#FutureTime.py
#Name: Brock Hoover
#Date: 2/01/25
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  inputhours = input("hours (must be an integer): ")
  #Ask user for minutes
  inputminutes = input("minutes (must be an integer): ")
  moreMins = (60 * int(inputhours) + int(inputminutes) )
  

  FutureMins = (currentMinute + moreMins ) % 60
  extraHour = ( (currentHour + (currentMinute + moreMins ) // 60) % 24)

  print(str(extraHour) +":" +str(FutureMins))
        
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"

if __name__ == '__main__':
  main()
