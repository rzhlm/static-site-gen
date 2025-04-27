import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node1 = ParentNode(
            "p",
            [
                LeafNode("b","something bolded"),
                LeafNode(None,"normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("b","node1"),
                LeafNode("b","node1"),
            ]
        )
        self.assertEqual(node1, node2)
    
    
    def test_not_eq(self):
        node_a = ParentNode([LeafNode("b","nodea"), LeafNode("b","nodea")])
        node_b = ParentNode([LeafNode("b","nodeb"), LeafNode("b","nodeb")])
        self.assertNotEqual(node_a, node_b)
"""
        node3 = ParentNode()
        node4 = ParentNode()
        self.assertNotEqual(node3, node4)
	
        node4 = ParentNode()
        node5 = ParentNode()
        self.assertNotEqual(node4, node5)
"""    

if __name__ == "__main__":
	unittest.main()