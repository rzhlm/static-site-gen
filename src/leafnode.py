from htmlnode import HTMLNode

class LeafNode(HTMLNode):
        # This is an end node in the tree
        #  by implication, it has no children and must have value
        def __init__(self, tag, value, props = None):
            super().__init__(tag, value, children = None, props = props)

        def to_html(self):
            if self.value is None:
                raise ValueError("LeafNode has no value")
            if self.tag is None:
                return self.value
            else:
                output = ""
                # tag
                output += f"<{self.tag}"
                if self.props:
                        for key, val in self.props.items():
                                output += f" {key}={val}"
                if self.props:
                        output += "/>" 
                else:
                        output += ">"

                # props
                output += self.value
                output += f"</{self.tag}>"
                return output


        def __eq__(self, other):
            # super().__eq__(other)
            
            if (self.value == other.value
            and self.tag == other.tag
            and self.props == other.props):
                return True
            return False
            
        def __repr__(self):
            return f"LeafNode: tag: {self.tag}, val: {self.value}, children(None?): {self.children}, props: {self.props}"
