import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_prt(self):
        node = LeafNode("<a>", "link")
        self.assertEqual(repr(node), "LeafNode(tag=<a>, value=link, props=None)")


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link.", {"href":"vault.71"})
        self.assertEqual(node.to_html(), '<a href="vault.71">This is a link.</a>')
