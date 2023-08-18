
class CheckInHandler(object):
    def __init__(self, parser):
        self.parser = parser
        self.state = parser.state

    def handle(self, p):
        self.state.has_checkin[self.parser.key] = True
        self.state.has_checkins[self.parser.key][p[1] + ' ' + p[3]] = True
        self.state.registered_variables[self.parser.key].add(p[1])

        variable = self.state.get_variable(p[3])
        
        if (variable == None):
            self.state.has_error[self.parser.key] = True
            return
        if (variable['type'] != 'set'):
            print(f'{p[3]} Should be of Type SET But is type "{variable["type"]}"')
            self.state.has_error[self.parser.key] = True

        if not self.state.participants.is_part_of_subset(p[1], p[3]):
            self.state.has_error[self.parser.key] = True
            print(f"Variable '{p[2]}' Not in list '{p[3]}' ")