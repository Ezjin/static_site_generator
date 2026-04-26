from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, value = None, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag é obrigatório.")
       
        if not self.children:
            raise ValueError("children é obrigatório")

        render = ""
        for c in self.children:
            render += c.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{render}</{self.tag}>"
