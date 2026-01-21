from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "**Bold text**"
    ITALIC_TEXT = "_Italic text"
    CODE_TEXT = "`Code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"

class TextNode(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return self.__dict__ == other.__dict__

