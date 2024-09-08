# Using SAX for XML Processing
import xml.sax

# SAX (Simple API for XML) is an event-driven parser that processes XML data sequentially.
# Unlike DOM, SAX does not load the entire XML document into memory. Instead, it triggers events as it parses.

class GroupHandler(xml.sax.ContentHandler):
    
    def startElement(self, name, attrs):
        """
        Called when an element starts.
        - `name`: The name of the element.
        - `attrs`: A dictionary-like object containing attributes of the element.
        """
        self.current = name
        if self.current == "person":
            print('------PERSON-----')
            print("ID: {}".format(attrs['id']))

    def characters(self, content: str) -> None:
        """
        Called when character data is encountered.
        - `content`: The text content within the element.
        """
        # Assign content based on current element type
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name: str) -> None:
        """
        Called when an element ends.
        - `name`: The name of the element.
        """
        # Print element data based on type
        if self.current == "name":
            print("Name: {}".format(self.name))
        elif self.current == "age":
            print("Age: {}".format(self.age))
        elif self.current == "weight":
            print("Weight: {}".format(self.weight))
        elif self.current == "height":
            print("Height: {}".format(self.height))
        
        # Reset the current element
        self.current = ""
            

# Create a handler and parser instance
handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)

# Parse the XML file
parser.parse('data.xml')
