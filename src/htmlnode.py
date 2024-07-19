class HTMLNode:
	def __init__(self, tag: str = None,
			 value: str = None,
			 children: list = None,
			 props:dict = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	
	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		output = f""
		for key, value in self.props.items():
			output += f' {key}={"value"}'
		return output

	def __repr__(self):
		return f"tag: {self.tag}, val: {self.value}, chl: {self.children}, props: {self.props}"

	def __eq__(self, other):
		if (self.value == other.value
		and self.tag == other.tag
		and self.children == other.children
		and self.props == other.props):
			return True
		return False