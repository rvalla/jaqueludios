from PIL import Image as im, ImageDraw as idraw, ImageFont as ifont

class PositionImage():
	"The class to convert a fen chess position in an image..."

	fen_pieces = {"P": [0,0], "N": [0,1], "B": [0,2], "R": [0,3], "Q": [0,4], "K": [0,5],
				"p": [1,0], "n": [1,1], "b": [1,2], "r": [1,3], "q": [1,4], "k": [1,5]}

	def __init__(self, sq_size, size, piece_set, board):
		self.sq_size = sq_size
		self.size = size
		self.board = im.open("img/" + board + ".png").resize((self.size, self.size))
		self.pieces = self.load_pieces(piece_set)

	def position_to_image(self, as_white: boolean, fen: str, filename: str):
		rows = fen.split(" ")[0].split("/")
		image = im.new("RGB", (self.size, self.size))
		image.paste(self.board, (0,0))
		draw = idraw.Draw(image)
		if as_white:
			x = 0
			y = 0
			for r in range(8):
				x = 0
				for c in rows[r]:
					try: 
						x += int(c)
					except:
						coordinates = self.get_piece_index(c)
						piece = self.pieces[coordinates[0]][coordinates[1]]
						image.paste(piece, (x * self.sq_size, y * self.sq_size), mask=piece)
						x += 1
				y += 1
		else:
			x = 0
			y = 0
			for r in range(8):
				x = 0
				for c in rows[r]:
					try: 
						x += int(c)
					except:
						coordinates = self.get_piece_index(c)
						piece = self.pieces[coordinates[0]][coordinates[1]]
						image.paste(piece, (self.size - (x + 1) * self.sq_size, self.size - (y + 1) * self.sq_size), mask=piece)
						x += 1
				y += 1
		image.save(filename, "png", quality=90, optimize=True)

	def get_piece_index(self, p):
		return self.fen_pieces[p]

	def load_pieces(self, piece_set):
		print("Position Image: Loading pieces...", end="\r")
		pieces = []
		white = []
		white.append(im.open("img/" + piece_set + "/wP.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/" + piece_set + "/wN.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/" + piece_set + "/wB.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/" + piece_set + "/wR.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/" + piece_set + "/wQ.png").resize((self.sq_size, self.sq_size)))
		white.append(im.open("img/" + piece_set + "/wK.png").resize((self.sq_size, self.sq_size)))
		black = []
		black.append(im.open("img/" + piece_set + "/bP.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/" + piece_set + "/bN.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/" + piece_set + "/bB.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/" + piece_set + "/bR.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/" + piece_set + "/bQ.png").resize((self.sq_size, self.sq_size)))
		black.append(im.open("img/" + piece_set + "/bK.png").resize((self.sq_size, self.sq_size)))
		pieces.append(white)
		pieces.append(black)
		print("Position Image: All pieces loaded!      ", end="\n")
		return pieces
	
	def get_message_position(self):
		x = self.size // 2
		y = self.size + self.sq_size // 2
		return (x,y)

	def get_font_size(self, size):
		return size // 20

	def __str__(self):
		return "Hi, I am an the class to transform a fen chess position on an image..."
