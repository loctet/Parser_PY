
class DeclarationHandler(object):
    def __init__(self, parser):
        self.parser = parser
        self.state = parser.state

    def handle(self, p):
        self.state.has_declaration[self.parser.key] = True
        # Return the extracted data
        if len(p) <= 3 or (len(p) > 3 and p[3] != ':'):
            self.register_var(p[2], p[1])
            return p

        if (p[1] == 'address') :
            self.state.tobe_in_checkins[self.parser.key].append(p[2] + ' '+ p[4])
            if not self.state.participants.is_part_of_subset(p[2], p[4]):
                self.state.participants.add_element(p[2], p[4])
            else:
                self.state.has_error[self.parser.key] = True
                print(f"Participant '{p[2]}' is already in list '{p[4]}' ")
        else:
            self.state.has_error[self.parser.key] = True

        return p

    # Custom function to handle assignation rule
    def handle_assignation(self, p):
        self.state.has_assignation[self.parser.key] = True

        # Check if the variable has been registered
        self.state.set_errornotdefinedvar(p[1], self.parser.key)
        return p[1], p[3]

    def register_var(self, v, t, value = None):
        if v in self.state.registered_variables:
            print(f"Variable '{v}' has already been registered.")
            self.state.has_error[self.parser.key] = True
            return
        
        if (not v in self.state.registered_variables):
            if t != 'set':
                self.state.registered_variables[v] = {
                    'type': t,
                    'value': value
                }
            else :
                self.state.registered_variables[v] = {
                    'type': t,
                    'value':  set()
                }

        if t == 'set' :
            if (value != None):
                self.state.registered_variables[v]['value'].add(value)
        else :
            self.state.registered_variables[v] = {
                'type': t,
                'value': value
            }