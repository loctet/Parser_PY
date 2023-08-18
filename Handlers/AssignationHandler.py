

class AssignationHandler(object):
    def __init__(self, parser):
        self.parser = parser
        self.state = parser.state

    def handle(self, p):
        self.state.has_assignation[self.parser.key] = True

        print(p[1:])
        # Check if the variable has been registered
        self.state.set_errornotdefinedvar(p[1], self.parser.key)
        
        return p[1], p[3]
