
class ExistentialHandler(object):
    def __init__(self, parser):
        self.parser = parser
        self.state = parser.state

    def handle(self, p):
        self.state.has_existential[self.parser.key] = True
        self.state.has_existentials[self.parser.key][p[2] + ' ' + p[3]] = True
        
        variable = self.state.get_variable(p[3])
        
        if (variable == None):
            self.state.has_error[self.parser.key] = True
            return
        if (variable['type'] != 'set'):
            print(f'{p[3]} Should be of Type SET But is type "{variable["type"]}"')
            self.state.has_error[self.parser.key] = True
        
        if (p[2] not in self.state.registered_variables[self.parser.key]):
            self.state.has_error[self.parser.key] = True
            print(f'"{p[2]}" Should be in the assertion')