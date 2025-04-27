import unittest

from leafnode import LeafNode

#    tag, value, props

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode(value="value",tag = "tag",props = {"key": "val"})
        node2 = LeafNode(value="value",tag = "tag",props = {"key": "val"})
        self.assertEqual(node1, node2)

        node_c = LeafNode(None,"value")
        node_d = LeafNode(None,"value")
        self.assertEqual(node_c, node_d)

    def test_not_eq(self):
        node_a = LeafNode("value","tag",{"key": "val"})
        node_b = LeafNode("value","tag")
        self.assertNotEqual(node_a, node_b)

        node3 = LeafNode("value","tag",{"key": "val"})
        node4 = LeafNode("value",{"key": "val"})
        self.assertNotEqual(node3, node4)

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        #print(node)
        #print(node.to_html())
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	

if __name__ == "__main__":
	unittest.main()
