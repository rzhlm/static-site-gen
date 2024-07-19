from htmlnode import HTMLNode

class LeafNode(HTMLNode):
		def __init__(self, value: str, tag: str = None, props:dict = None):
			super().__init__(value: str, tag: str = None, props: dict = None)
			
		def to_html(self):
			if self.value is None:
				raise ValueError("LeafNode has no value")
			if self.tag is None:
				return str(self.value)
			else:
				self.props_to_html()