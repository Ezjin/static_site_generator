import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prt(self):
        node = HTMLNode("<a>", "link")
        self.assertEqual(repr(node), "HTMLNode(tag=<a>, value=link, children=None, props=None)")

    def test_props_to_html(self):
        prop = {"href":"https://vault71", "target":"_blank"}
        node = HTMLNode("<a>", "link", props=prop)
        self.assertEqual(node.props_to_html(), ' href="https://vault71" target="_blank"')

    def test_props_none(self):
        node = HTMLNode("<a>", "link")
        self.assertEqual(node.props_to_html(), "")
