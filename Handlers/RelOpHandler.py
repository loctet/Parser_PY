

class RelOpHandler(object):
    def __init__(self, parser):
        self.parser = parser
        self.state = parser.state

    def handle(self, p):
        # Perform necessary handling for relational operator
        # For example, you can check if the variables are defined and valid
        # Update the parser state if needed
        # Handle any errors or validations

        # Example: Check if variables are defined before using them
        # print(p[1:])

        return p
