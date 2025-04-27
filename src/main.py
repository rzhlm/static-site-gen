from textnode import TextType, TextNode
from leafnode import LeafNode
from enum import Enum
from enum_types import *


""" Structure:
- Delete everything in the /public directory.
- Copy any static assets (HTML template, images, CSS, etc.) to the /public directory.
- Generate an HTML file for each Markdown file in the /content directory. 
	For each Markdown file:
		- Open the file and read its contents.
		- Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
		- Convert each block into a tree of HTMLNode objects. For inline elements (like bold text, links, etc.) we will convert:
			Raw markdown -> TextNode -> HTMLNode
		- Join all the HTMLNode blocks under one large parent HTMLNode for the pages.
		- Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant HTML string and inject it in the HTML template.
		- Write the full HTML string to a file for that page in the /public directory.
"""


def main():	
	testObj = TextNode("text", TextType.NORMAL_TEXT, "https://somewhere")
	print(testObj)
	

def text_node_to_html_node(text_node):
	# TODO: add unittests
	match text_node.text_type:
		case node_type.text:
			# (tag, value, props = None):
			return LeafNode(tag=None, value=text_node.text)
		case node_type.bold:
			# (tag, value, props = None):
			return LeafNode(tag="b", value=text_node.text)
		case node_type.italic:
			return LeafNode(tag="i", value=text_node.text)
		case node_type.code:
			return LeafNode(tag="code", value=text_node.text)
		case node_type.link:
			return LeafNode(tag="a", value=text_node.text, props="href")
		case node_type.image:
			return LeafNode(tag="img", value="", props={"src": text_node.url,
											   "alt": text_node.text})
		case _:
			raise Exception("text_node isn't a defined type")

if __name__ == "__main__":
	main()
