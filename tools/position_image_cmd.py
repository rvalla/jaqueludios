import random as rd
from game_to_imgs import GameImages
from position_image import PositionImage

pieces = None
board = None
lastp = 1
filename = None
aswhite = True

print("Welcome to chess positions to image tool!", end="\n")
print("Let's create chess boards from fen strings...", end="\n")

#First we need to decide the piece set...
print("Please select your preferred piece set telling me a number:\n1. Cburnett\n2. Gioco", end="\n\n")

p = input()
if p == "1":
  pieces = "cburnett"
else: 
  pieces = "gioco"

#Now we need to decide the board...
print("Now select your preferred board telling me a number:\n1. Red\n2. Green\n3. Blue\n4. Monochrome\n5. Line pattern", end="\n\n")

p = input()
if p == "1":
  board = "boardR"
elif p == "2":
  board = "boardG"
elif p == "2":
  board = "boardB"
elif p == "2":
  board = "boardBW"
else: 
  board = "boardBWL"

#Loading the tool to make board images with fen strings...
PI = PositionImage(135, 1080, pieces, board)

#We need to know the color perspective...
print("Should I draw the board from white's point of view?\n1. Yes\n2. No", end="\n\n")
p = input()
if p == "2":
  aswhite = False

#The last thing we need is a name for our files...
print("One last thing. Please give me a filename for your board positions", end="\n\n")
filename = "output/positions/" + input()

#We are ready now...
print("All set! Wainting your fen strings. Type 'exit' to quit.", end="\n\n")

while True:
  fen = input()
  if fen == "exit":
    break
  else:
    try:
      newfile = filename + "_" + str(lastp).zfill(2) + ".png"
      PI.position_to_image(aswhite, fen, newfile)
      lastp += 1
      print(rd.choice(["The image was saved.", "Done!", "Your positions was saved.", "The image is ready!"]), end="\n")
    except:
      print("That's not a correct formated fen string!", end="\n\n")
      pass
