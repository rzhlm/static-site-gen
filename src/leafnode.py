from htmlnode import HTMLNode

class LeafNode(HTMLNode):
        def __init__(self, tag, value, props = None):
            super().__init__(tag, value, children = None, props = props)

        def to_html(self):
            if self.value is None:
                raise ValueError("LeafNode has no value")
            if self.tag is None:
                return str(self.value)
            else:
                self.props_to_html()

        def __eq__(self, other):
            # super().__eq__(other)
            
            if (self.value == other.value
            and self.tag == other.tag
            and self.props == other.props):
                return True
            return False