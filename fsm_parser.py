import json
import re
from fsm_table import check_reachable_states, generate_transition_table

internal_action = 1


def get_from_and_to_states(string):
    words = string.split()
    cleaned_words = [re.sub("[^A-Za-z0-9]+", "", word) for word in words]
    cleaned_words = list(filter(None, cleaned_words))
    return cleaned_words[0], cleaned_words[-1]


def has_initial_state(string):
    words = string.split()
    initStates = []
    if words:
        first_word = words[0]
        last_word = words[-1]
        if first_word.startswith("_"):
            cleaned_first_word = re.sub("[^A-Za-z0-9]+", "", first_word)
            initStates.append(cleaned_first_word)

        if last_word.startswith("_"):
            cleaned_last_word = re.sub("[^A-Za-z0-9]+", "", last_word)
            initStates.append(cleaned_last_word)

    return initStates


def has_final_state(string):
    words = string.split()
    finalStates = []
    if words:
        first_word = words[0]
        last_word = words[-1]
        if first_word.endswith("+"):
            cleaned_first_word = re.sub("[^A-Za-z0-9]+", "", first_word)
            finalStates.append(cleaned_first_word)

        if last_word.endswith("+"):
            cleaned_last_word = re.sub("[^A-Za-z0-9]+", "", last_word)
            finalStates.append(cleaned_last_word)

    return finalStates


def get_new_adding_participant(line):
    participants = {}
    matches = re.findall(r"(\w+):([A-Z]+)", line)

    for match in matches:
        participant, participant_type = match
        participants[participant] = participant_type

    return participants


def get_existing_participant(line):
    participants = {}
    matches = re.findall(r"([a-z]+)\||([a-z]+)>", line)

    for match in matches:
        participant, participant_type = match

        if participant == "":
            participant = participant_type

        if participant == "":
            continue
        participants[participant] = ""

    matches = re.findall(r"([a-z]+)\||([a-z]+)<", line)  ## funtion calling external

    for match in matches:
        participant, participant_type = match

        if participant == "":
            participant = participant_type

        if participant == "":
            continue
        participants[participant] = ""

    return participants


def get_action_called(line):
    matches = re.findall(r">([a-zA-Z.]+)", line)
    if matches:
        return matches[0]

    matches = re.findall(r"<([a-zA-Z.]+)", line)
    if matches:
        return matches[0]

    return None


def is_external(line):
    return line.find("<") >= 0


def parse_transition_line(line):
    transition = {}

    from_state, to_state = get_from_and_to_states(line)
    transition["from"] = from_state
    transition["to"] = to_state

    initial_states = has_initial_state(line)
    transition["initialStates"] = initial_states

    final_states = has_final_state(line)
    transition["finalStates"] = final_states

    new_participants = get_new_adding_participant(line)
    transition["newParticipants"] = new_participants

    existing_participants = get_existing_participant(line)
    transition["existingParticipants"] = existing_participants

    action_called = get_action_called(line)
    transition["actionCalled"] = action_called
    transition["precondition"] = ""
    transition["postcondition"] = ""

    transition["externalAction"] = is_external(line)
    if is_external(line):
        global internal_action
        transition["to"] = "I" + str(internal_action)
        transition["externalActionList"] = [
            transition["to"] + " c>OK() " + to_state,
            transition["to"] + " c>NOK() " + from_state,
        ]
        internal_action += 1
    return transition


def parse_transitions(text):
    transitions = []
    lines = text.splitlines()

    for line in lines:
        transition = parse_transition_line(line)
        transitions.append(transition)
        if transition["externalAction"]:
            for nline in transition["externalActionList"]:
                transition = parse_transition_line(nline)
                transitions.append(transition)

    return transitions


def generate_fsm_json(text):
    fsm = {}
    fsm["transitions"] = parse_transitions(text)

    participants = set()
    types = set()
    states = set()
    initial_states = set()
    final_states = set()

    for transition in fsm["transitions"]:
        participants.update(transition["newParticipants"].keys())
        participants.update(transition["existingParticipants"].keys())
        types.update(transition["newParticipants"].values())
        states.add(transition["from"])
        states.add(transition["to"])
        initial_states.update(transition["initialStates"])
        final_states.update(transition["finalStates"])

    fsm["participants"] = list(participants)
    fsm["types"] = list(types)
    fsm["states"] = list(states)
    fsm["initialStates"] = list(initial_states)
    fsm["finalStates"] = list(final_states)

    transition_table = generate_transition_table(fsm)
    reachable_states, unreachable_states = check_reachable_states(
        transition_table,
        [
            index
            for index, item in enumerate(fsm["states"])
            if item in fsm["initialStates"]
        ],
        [
            index
            for index, item in enumerate(fsm["states"])
            if item in fsm["finalStates"]
        ],
    )

    fsm["unreachableStates"] = [fsm["states"][i] for i in unreachable_states]

    return json.dumps(fsm, indent=4)
