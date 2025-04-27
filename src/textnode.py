from enum import Enum, auto
from leafnode import LeafNode

class TextType(Enum):
    NORMAL = auto()
    BOLD = auto()
    ITALIC = auto()
    CODE = auto()
    ANCHOR = auto()
    IMAGE = auto()

class TextNode:

    def __init__(self, text:str, text_type: TextType, url: None| str=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def text_node_to_html_node(self, text_node):
        try:
            TextType(text_node.text_type)
            match text_node.text_type:
                case TextType.NORMAL:
                    return LeafNode(tag=None, value=text_node.text)
                case TextType.BOLD:
                    return LeafNode(tag='b', value=text_node.text)
                case TextType.ITALIC:
                    return LeafNode(tag='i', value=text_node.text)
                case TextType.CODE:
                    return LeafNode(tag="code", value=text_node.text)
                case TextType.ANCHOR:
                    return LeafNode(tag="a", value=text_node.url , prop="href")
                case TextType.IMAGE:
                    return LeafNode(
                        tag="img",
                        value="",
                        props={"src":None, "alt":None}
                        )
                case _:
                    raise ValueError("not a valid TextType")
	        
        except ValueError as e:
            raise ValueError("text_node.TextType not valid", e)

    def __eq__(self, other):
        if self.text == other.text and \
        self.text_type == other.text_type and \
        self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
