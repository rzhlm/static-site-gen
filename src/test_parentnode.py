import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node1 = ParentNode()
        node2 = ParentNode()
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node_a = HTMLNode("notag","novalue","nochildren","noprops")
        node_b = HTMLNode("tag","value","children","props")
        self.assertNotEqual(node_a, node_b)

        node3 = HTMLNode("tag","value","children","props")
        node4 = HTMLNode("tag","value","children")
        self.assertNotEqual(node3, node4)
	
        node4 = HTMLNode("tag","value","children")
        node5 = HTMLNode("tag","value")
        self.assertNotEqual(node4, node5)
        
if __name__ == "__main__":
	unittest.main()