class HTMLNode:
	def __init__(self, tag: str = None,
			 value: str = None,
			 children: list['HTMLNode'] = None,
			 props: dict = None
		):
		
		self.tag = tag # No tag = raw text, eg end node (leaf node)
		self.value = value # no val --> has children (not a leaf node)
		self.children = children # no children --> has values (leaf node)
		self.props = props # no props --> has no attribs
	
	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		output = ""
		if self.props:
			for key, val in self.props.items():
				output += f" {key}={val}"
				
		"""
		output = ""
		# tag
		if self.tag:
			output += f"<{self.tag}"
			if self.props:
				for key, val in self.props.items():
					output += f" {key}={val}"
			output += "/>"
			if self.children:
				for child in self.children:
					output += child
		
		# props
			if self.value:
				output += self.value
			output += f"</{self.tag}>"
		return output
		"""

	def __repr__(self):
		return f"tag: {self.tag}, val: {self.value}, children: {self.children}, props: {self.props}"

	def __eq__(self, other):
		if (self.value == other.value
		and self.tag == other.tag
		and self.children == other.children
		and self.props == other.props):
			return True
		return False
