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
    
    def get_formula_check_part_existance(self, participant):
        if (len(self.roles) == 0) :
            return "False"
        
        str = []
        for role in self.roles:
            str.append(f"'{participant}' in {self.roles[role]['name']}_role")

        return " or ".join(str)

    #Participants Adding list
    def add_participants(self, data):
        [self.add_participant(entry["role"], participant) for entry in data for participant in entry["participants"]]

    def get_formula_for_participant_check(self, participants, caller):
        roles_list = list(self.roles.keys())
        result = []

        try:
            user, rolesU = next(iter(caller.items())) if len(caller) == 1 else ["", ""]
            """for p, role in participants["existingParticipants"].items():
                self.add_participant(role, p)
                roles_list.append(role)"""
                
            for p, role in participants["newParticipants"].items():
                self.add_participant(role, p)
            
            roles_list = list(set(roles_list))
            setList = []
            if len(rolesU) > 0:
                for roleU in rolesU:
                    if roleU.strip() == "":
                        result = [f"'{user}' in {role}_role" for role in roles_list]
                        return f"Or({','.join(result) if result else 'False'})" if len(roles_list) > 0 else self.get_formula_check_part_existance(user)
                    else:
                        if roleU not in roles_list:
                            return "False" 
                        setList.append(f"set({roleU}_role)")
                
                strJ = ""
                if len(rolesU) == 1:
                    strJ = f"len({rolesU[0]}_role) > 0 and '{user}' in {rolesU[0]}_role"
                else: 
                    strJ = f"len(list({' & '.join(setList)})) > 0 and  '{user}' in list({' & '.join(setList)})"
                    
                return f" {strJ}" if len(roles_list) > 0 else self.get_formula_check_part_existance(user)
            else:
                result = [f"'{user}' in {role}_role" for role in roles_list]
                return f"Or({','.join(result) if result else 'False'})" if len(roles_list) > 0 else self.get_formula_check_part_existance(user)
            
        except Exception as e:
            print(f"Participant Error: {e}")

        return "True"
                
    
 