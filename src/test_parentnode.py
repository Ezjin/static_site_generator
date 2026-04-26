import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
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

    def test_to_html_without_children(self):
        parent_node = ParentNode("body", [])
        with self.assertRaises(ValueError) as ctx:
            parent_node.to_html()
        
        self.assertEqual(str(ctx.exception), "children é obrigatório")

    def test_to_html_with_two_children(self):
        child_node_1 = LeafNode("p", "children 1 paragraph")
        child_node_2 = LeafNode("b", "children 2 paragraph")
        parent_node = ParentNode("body", [child_node_1, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            "<body><p>children 1 paragraph</p><b>children 2 paragraph</b></body>"
        )
