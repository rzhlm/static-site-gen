import unittest

from leafnode import LeafNode

#    value: str, tag: str = None, props: dict = None

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("value","tag",{"key": "val"} )
        node2 = LeafNode("value","tag",{"key": "val"} )
        self.assertEqual(node1, node2)

        node_c = LeafNode("value")
        node_d = LeafNode("value")
        self.assertEqual(node_c, node_d)

    def test_not_eq(self):
        node_a = LeafNode("value","tag",{"key": "val"} )
        node_b = LeafNode("value","tag")
        self.assertNotEqual(node_a, node_b)

        node3 = LeafNode("value","tag",{"key": "val"} )
        node4 = LeafNode("value",{"key": "val"} )
        self.assertNotEqual(node3, node4)
	

if __name__ == "__main__":
	unittest.main()