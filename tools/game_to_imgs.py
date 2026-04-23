import os
import random as rd
from PIL import Image as im
import chess as ch
import chess.pgn as chpgn

class GameImages():
	"The class to convert a chess game in a series of images"

	def __init__(self, period, sq_size, size, game_path, output_path, file_name):
		print("Starting new series of images...", end="\n")
		self.period = period
		self.sq_size = sq_size
		self.size = size
		self.game = chpgn.read_game(open(game_path))
		self.pieces = self.load_pieces()
		self.output_path = output_path
		self.file_name = file_name
		self.board = ch.Board()
		self.background = rd.choice(["img/boardR.png", "img/boardG.png", "img/boardB.png"])
		if not os.path.exists(output_path):
			os.mkdir(output_path)
		self.game_to_images()
		print("That's all!            ", end="\n")

	def game_to_images(self):
		m = 0
		self.save_board_state(0)
		for move in self.game.mainline_moves():
			print("Working on move " + str(m), end="\r")
			self.board.push(move)
			m += 1
			if m % self.period == 0:
				self.save_board_state(m // self.period)

	def save_board_state(self, image_n):
		image = im.open(self.background).resize((self.size, self.size))
		for sq in range(64):
			piece = self.board.piece_at(sq)
			if not piece == None:
				f, c = divmod(sq,8)
				color = None
				if piece.color:
					color = 0
				else:
					color = 1
				piece_image = self.pieces[color][piece.piece_type-1]
				image.paste(piece_image, (c * self.sq_size, (7-f) * self.sq_size), mask=piece_image)
		name = self.file_name + "_" + ("{:03d}").format(image_n) + ".png"
		image.save(self.output_path + "/" + name, "png", quality=85, optimize=True)

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

	def __str__(self):
		return "Hi, I am an the class to transform a chess game on a serieas of images..."
