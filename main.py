print("Welcome to my first game")

name = input("what is your name? ")
age = int(input("what is your age? "))

print("Hello", name, "you are", age, "years old.")


if age >= 18:
  print("You are old enough to date!")

  wants_to_date = input("Do you want to Date?").lower()
  if wants_to_date == "yes":
    print("Lets Date!")

    yes_or_no = input("Lets decide... (lunch/dinner)? ")
    if yes_or_no == "dinner":
      ans = input("Nice, you agree to pay for dinner... and ill go out with you (sure/yes)? ")

      if ans == "sure":
        print("yay! lets gooo...")

      elif ans == "yes":
        print("ummm... you dont sound sure, so lets just drop it! byeee..")

      ans = input("where are you going to take me out to? (mcdonald's/cesar's palace)?")
      if ans == "mcdonald's":
        print("Never mind")

      else:
        print("i am excited!")
    
    else:
      print("Bye bye...")

  else: 
    print("Cya...")




else:
  print("You're not old enough")
