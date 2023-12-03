class ParticipantManager:
    def __init__(self):
        self.roles = {}
    
    #add a participant
    def add_participant(self, role, participant):
        if role not in self.roles:
            self.roles[role] = {
                'name': role,
                'declaration': f"{role}_role = []",
                'list': [],
                'participants': [],
            }
        if participant not in self.roles[role]['participants']:
            self.roles[role]['list'].append(f"{role}_role.append('{participant}')")
            self.roles[role]['participants'].append(participant)

    def if_part_in_subset(self, participant, role):
    
        if role not in self.roles:
            return False
        return participant in self.roles[role]['participants']
    
    #Participants Adding list
    def add_participants(self, data):
        [self.add_participant(entry["role"], participant) for entry in data for participant in entry["participants"]]

                
    
