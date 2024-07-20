from htmlnode import HTMLNode

	#	self.tag = tag
	#	self.value = value
	#	self.children = children
	#	self.props = props
	

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children, props = None):
        super().__init__(tag = tag, value = None, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode: no tag present")
        if not self.children:
            raise ValueError("ParentNode: no children present")
        else:
            
            return f""