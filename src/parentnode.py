from htmlnode import HTMLNode
	#	tag, value, children, props
	
class ParentNode(HTMLNode):
    def __init__(self, tag = None, children, props = None):
        super().__init__(tag = tag, value = None, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode: no tag present")
        if not self.children:
            raise ValueError("ParentNode: no children present")
        else:
            start = f"<{self.tag}>"
            inner = f""
            for child in self.children:
                inner += child.to_html()
            end = f"</{self.tag}>"
            return f"{start}{inner}{end}"