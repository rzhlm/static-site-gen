import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node",TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Text",TextType.NORMAL)
        node2 = TextNode("Text",TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_if_url(self):
        node = TextNode("Text",TextType.NORMAL,"http://someplace")
        node2 = TextNode("Text",TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()

