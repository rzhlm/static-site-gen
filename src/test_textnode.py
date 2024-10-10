import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", "bold")
		node2 = TextNode("This is a text node","bold")
		self.assertEqual(node, node2)

	def test_not_eq(self):
		node = TextNode("Text","Type")
		node2 = TextNode("Text","Other")
		self.assertNotEqual(node, node2)

	def test_not_eq_if_url(self):
		node = TextNode("Text","Type","http://someplace")
		node2 = TextNode("Text","Type")
		self.assertNotEqual(node, node2)

if __name__ == "__main__":
	unittest.main()

