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
                LeafNode("b","something bolded"),
                LeafNode(None,"normal text"),
            ],
        )
        self.assertEqual(node1, node2)
        
        # TODO: also check against a fixed, known output
    
    
    def test_not_eq(self):
        node_a = ParentNode("p", [LeafNode("b","nodea")])
        node_b = ParentNode("p", [LeafNode("b","nodeb")])
        self.assertNotEqual(node_a, node_b)
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )
        
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
