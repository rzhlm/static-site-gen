from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    # explicitly call init with children = when instantiating
    #	HTMLNode: tag, value, children, props
    def __init__(
    self,
    tag: str,
    children: list,
    props: dict | None = None
    ):
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
            #print(f"{start}{inner}{end}")
            return f"{start}{inner}{end}"
    
    
    def __repr__(self):
    	return f"LeafNode: tag: {self.tag}, val: {self.value}, children: {self.children}, props(None?): {self.props}"
