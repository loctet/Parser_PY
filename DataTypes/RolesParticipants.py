class RolesParticipants(object):

    def add_element(self, participant, role):
        if role not in self.roles:
            self.roles[role] = set()
        
        self.roles[role].add(participant)

    def is_part_of_subset(self, participant, role):
        if role not in self.roles:
            return False

        return participant in self.roles[role]
    
    def add_multiple_elements(self, data):
        for entry in data:
            self.add_element(entry["role"], entry["participants"][0])

    def __init__(self):
        self.roles= {}