class ParticipantManager:
    def __init__(self):
        self.roles = {}
    
    #add a participant
    def add_participant(self, role, participant, index):
        if role not in self.roles:
            self.roles[role] = {
                'name': role,
                'declaration': f"role_{role} = Array('{role}',IntSort() , StringSort())",
                'list': []
            }
        self.roles[role]['list'].append(f"Store(role_{role}, {index}, String('{participant}'))")

    def if_part_in_subset(self, participant, role):
        if role not in self.roles:
            return False
        return participant in self.roles[role]
    
    #Participants Adding list
    def add_participants(self, data):
        for entry in data:
            index = 0
            for participant in entry["participants"]:
                self.add_participant(entry["role"], participant, index)
                index += 1
    
