import os
import json as js
from PIL import Image as im
import chess as ch
import chess.pgn as chpgn

class GameImages():
	"The class to convert a chess game in a series of images"

	def __init__(self, config_path):
		print("Starting new series of images...", end="\n")
		self.config = js.load(open(config_path))
		self.period = self.config["period"]
		self.sq_size = self.config["sq_size"]
		self.size = self.config["size"]
		self.game = chpgn.read_game(open(self.config["game_path"]))
		self.pieces = self.load_pieces()
		self.board_state = self.start_board()
		if not os.path.exists(self.config["output_path"]):
			os.mkdir(self.config["output_path"])
		self.game_to_images()
		print("That's all!            ", end="\n")

	def game_to_images(self):
		m = 0
		self.save_board_state(0)
		for move in self.game.mainline_moves():
			print("Working on move " + str(m), end="\r")
			self.make_move(move)
			m += 1
			if m % self.period == 0:
				self.save_board_state(m // self.period)

	def make_move(self, move):
		origin = move.from_square
		destination = move.to_square
		piece_at = self.board_state[origin]
		self.board_state[origin] = None
		self.board_state[destination] = piece_at

	def save_board_state(self, image_n):
		image = im.open(self.config["background"]).resize((self.size, self.size))
		for sq in range(64):
			if not self.board_state[sq] == None:
				f, c = divmod(sq,8)
				piece_image = self.pieces[self.board_state[sq][0]][self.board_state[sq][1]-1]
				image.paste(piece_image, (c * self.sq_size, (7-f) * self.sq_size), mask=piece_image)
		name = self.config["output_name"] + "_" + ("{:03d}").format(image_n) + ".png"
		image.save(self.config["output_path"] + "/" + name, "png", quality=85, optimize=True)

	def load_pieces(self):
		print("Loading pieces...", end="\r")
		pieces = []
		white = []
		white.append(im.open("img/wP.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/wN.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/wB.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/wR.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/wQ.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/wK.png").resize((self.sq_size, self.sq_size)))
		black = []
		black.append(im.open("img/bP.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/bN.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/bB.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/bR.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/bQ.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/bK.png").resize((self.sq_size, self.sq_size)))
		pieces.append(white)
		pieces.append(black)
		return pieces

	def start_board(self):
		squares = [None for sq in range(64)]
		squares[0:15] = [(0,4), (0,2), (0,3), (0,5), (0,6), (0,3), (0,2), (0,4), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1)]
		squares[48:63] = [(1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,1), (1,4), (1,2), (1,3), (1,5), (1,6), (1,3), (1,2), (1,4)]
		return squares

	def __str__(self):
		return "Hi, I am an the class to transform a chess game on a serieas of images..."
