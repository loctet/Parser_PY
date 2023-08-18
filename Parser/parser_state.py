# parser_state.py

class ParserState:
    def __init__(self, participants):
        self.has_error = {}
        self.has_declaration = {}
        self.has_assignation = {}
        self.has_assertion = {}
        self.has_existential = {}
        self.has_existentials = {}
        self.tobe_in_existential = {}
        self.tobe_in_checkins = {}
        self.registered_variables = {}
        self.has_checkin = {} 
        self.has_checkins = {} 
        self.participants = participants

    def reset(self, key):
        self.has_error[key] = None
        self.has_declaration[key] = None
        self.has_assignation[key] = None
        self.has_assertion[key] = None
        self.has_existential[key] = None
        self.has_existentials[key] = {}
        self.has_checkin[key] = None
        self.has_checkins[key] = {}
        self.tobe_in_existential[key] = []
        self.tobe_in_checkins[key] = []
        self.registered_variables[key] = set()

    def set_error(self, key, value = True):
        self.has_error[key] = value

    def set_declaration(self, key):
        self.has_declaration[key] = True

    def set_assignation(self, key):
        self.has_assignation[key] = True

    def set_assertion(self, key):
        self.has_assertion[key] = True

    def set_existential(self, key):
        self.has_existential[key] = True

    def set_existentials(self, key, value):
        self.has_existentials[key] = value

    def set_tobe_in_existential(self, key, value):
        self.tobe_in_existential[key] = value

    def register_variable(self, key, v, t, value=None):
        if v in self.registered_variables:
            print(f"Variable '{v}' has already been registered.")
            self.has_error[key] = True
            return

        if t != 'set':
            self.registered_variables[v] = {
                'type': t,
                'value': value
            }
        else:
            self.registered_variables[v] = {
                'type': t,
                'value': set()
            }

        if t == 'set' and value is not None:
            self.registered_variables[v]['value'].add(value)
        
        if key not in self.registered_variables:
            self.registered_variables[key] = {}
            
        self.registered_variables[key].add(v)

    def get_variable(self, v):
        return self.registered_variables.get(v)
    
    def set_errornotdefinedvar(self, p, key):
        if p not in self.registered_variables:
            print(f"Variable '{p}' has not been registered yet.")
            self.has_error[key] = True

