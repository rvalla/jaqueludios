from game_to_imgs import GameImages
from position_image import PositionImage

pieces = "cburnett"
board = "boardBWL"
lastp = 1
filename = "output/positions/triunfalismo"
aswhite = True

PI = PositionImage(135, 1080, pieces, board)
fens = open("input/positions.txt", "r").readlines()

for fen in fens:
  newfile = filename + "_" + str(lastp).zfill(2) + ".png"
  PI.position_to_image(aswhite, fen, newfile)
  lastp += 1

print("I saved " + str(lastp) + " positions!", end="\n")
