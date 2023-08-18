
class AssertionHandler(object):
    def __init__(self, parser):
        self.parser = parser
        self.state = parser.state

    def handle(self, p):
        self.state.has_assertion[self.parser.key] = True
        if (p[1] not in [None, 'True', 'False', '(', ')']) :
            self.state.set_errornotdefinedvar(p[1], self.parser.key)
        return p
