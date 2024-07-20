from textnode import TextNode
from leafnode import LeafNode
from enum import Enum

node_type = Enum('node_type',["text","bold","italic","code","link","image"])

def main():
	
	testObj = TextNode("text", "type", "https://somewhere")
	print(testObj)
	

def text_node_to_html_node(text_node):
	match text_node.text_type:
		case node_type.text:
			# (tag, value, props = None):
			return LeafNode(tag=None, value=text_node)
		case node_type.bold:
			# (tag, value, props = None):
			return LeafNode(tag="b", value=text_node)
		case node_type.italic:
			return LeafNode(tag="i", value=text_node)
		case node_type.code:
			return LeafNode(tag="code", value=text_node)
		case node_type.link:
			return LeafNode(tag="a", value=text_node, props="href")
		case node_type.image:
			# props= src and alt
			return LeafNode(tag="img", value="", props={text_node})
		case _:
			raise Exception("text_node isn't a defined type")

main()