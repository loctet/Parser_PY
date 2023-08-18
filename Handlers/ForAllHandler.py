
class ForAllHandler(object):
    def __init__(self, parser):
        self.parser = parser
        self.state = parser.state

    def handle(self, p):
        # ... forall handling logic ...
        c = 0
