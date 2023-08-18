

class VariableNameHandler:
    def __init__(self, parser):
        self.parser = parser
        self.state = parser.state

    def handle(self, p):
        self.state.registered_variables[self.parser.key].add(p[1])
        self.state.set_errornotdefinedvar(p[1], self.parser.key)
        return p
