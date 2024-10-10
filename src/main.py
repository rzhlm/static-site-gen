from textnode import TextNode
from leafnode import LeafNode
from enum import Enum
from enum_types import *



def main():
	
	
	testObj = TextNode("text", "type", "https://somewhere")
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