from enum import Enum, auto

class TextType(Enum):
	NORMAL = auto()
	BOLD = auto()
	ITALIC = auto()
	CODE = auto()
	ANCHOR = auto()

class TextNode:

	def __init__(self, text:str, text_type: TextType, url: None| str=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		if self.text == other.text and \
		self.text_type == other.text_type and \
		self.url == other.url:
			return True
		return False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"
