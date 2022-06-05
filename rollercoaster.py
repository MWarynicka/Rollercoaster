print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height>=120:
  print('You can ride')
  age= int(input("how old are you?"))
  if age >= 18:
    print("cost 20$")
  elif age < 18:
    print("cost 10$")
else:
    print("You can't ride" )
