import json
import pandas as pd

# JSON data (replace with your actual JSON data)
json_data = {
  "id": "c",
  "initialState": "S0",
  "statesDeclaration": "int price ; bool state; array M := [1,2,3,4,5]; int x := 0",
  "states": [
    "S0",
    "S1",
    "S2"
  ],
  "finalStates": [
    "S1"
  ],
  "transitions": [
    {
      "from": "_",
      "to": "S0",
      "initialStates": [],
      "finalStates": [],
      "newParticipants": {
        "c": "C"
      },
      "existingParticipants": {},
      "actionLabel": "start",
      "preCondition": "True",
      "postCondition": "state==True",
      "input": "",
      "varUpdate": "",
      "externalAction": False
    },
    {
      "from": "S0",
      "to": "S1",
      "initialStates": [
        "S0"
      ],
      "finalStates": [],
      "newParticipants": {
        "b": "B"
      },
      "existingParticipants": {},
      "actionLabel": "makeoffer",
      "preCondition": "And(_p > 0, state == True)",
      "postCondition": "price == _p",
      "input": "int _p",
      "varUpdate": "",
      "externalAction": False
    },
    {
      "from": "S1",
      "to": "I1",
      "initialStates": [],
      "finalStates": [
        "S2"
      ],
      "newParticipants": {},
      "existingParticipants": {
        "o": ""
      },
      "actionLabel": "acceptoffer",
      "preCondition": "state",
      "postCondition": "Not(state)",
      "input": "",
      "varUpdate": "",
      "externalAction": True,
      "externalActionList": [
        "I1 c>OK() S2",
        "I1 c>NOK() S1"
      ]
    },
    {
      "from": "I1",
      "to": "S2",
      "initialStates": [],
      "finalStates": [],
      "newParticipants": {},
      "existingParticipants": {
        "c": ""
      },
      "actionLabel": "OK",
      "preCondition": "True",
      "postCondition": "And(Not(state), And(forall(M, item > 0), exist(M, item > 0)))",
      "input": "",
      "varUpdate": "M[-1] := -5", 
      "externalAction": False,
      "Comment": "The model will fail because we update table with a value that will make the model having error"
    },
    {
      "from": "I1",
      "to": "S1",
      "initialStates": [],
      "finalStates": [],
      "newParticipants": {},
      "existingParticipants": {
        "c": ""
      },
      "actionLabel": "NOK",
      "preCondition": "True",
      "postCondition": "And(state, x <= 10)",
      "input": "",
      "varUpdate": "x := 0",
      "externalAction": False
    },
    {
      "from": "S1",
      "to": "S3",
      "initialStates": [],
      "finalStates": [
        "S3"
      ],
      "newParticipants": {},
      "existingParticipants": {
        "o": ""
      },
      "actionLabel": "rejectoffer",
      "preCondition": "state",
      "postCondition": "Not(state)",
      "input": "",
      "varUpdate": "",
      "externalAction": False
    }
  ],
  "rPAssociation": [
    {
      "role": "O",
      "participants": [
        "o"
      ]
    },
    {
      "role": "B",
      "participants": [
        "b"
      ]
    },
    {
      "role": "D",
      "participants": [
        "d"
      ]
    }
  ]
}

# Create a dictionary to store transitions grouped by "to" state
transitions_by_to_state = {}
# Group transitions by "to" state
for transition in json_data["transitions"]:
    to_state = transition["from"]
    if to_state not in transitions_by_to_state:
        transitions_by_to_state[to_state] = []
    transitions_by_to_state[to_state].append(transition)

# Print the grouped transitions
for from_state, transitions in transitions_by_to_state.items():
    print(f"Transitions to state '{from_state}':")
    for transition in transitions:
        print(f"  - From: {transition['from']}, Action: {transition['actionLabel']} - To : {transition['to']}")
    print()