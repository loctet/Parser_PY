def generate_smart_contract(input_file):
    smart_contract = "// SPDX-License-Identifier: MIT\n"
    smart_contract += "pragma solidity ^0.8.0;\n\n"
    smart_contract += "contract MockupContract {\n"
    smart_contract += "    address public owner;\n\n"
    smart_contract += "    modifier onlyOwner() {\n"
    smart_contract += "        require(msg.sender == owner, 'Only the contract owner can call this function.');\n"
    smart_contract += "        _;\n"
    smart_contract += "    }\n\n"
    smart_contract += "    constructor() {\n"
    smart_contract += "        owner = msg.sender;\n"
    smart_contract += "    }\n\n"

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(' ')
                action = parts[1]

                if action.startswith('o<'):
                    function_name = action[3:]
                    smart_contract += f"    function {function_name}() public onlyOwner {{\n"
                    smart_contract += f"        // Function logic\n"
                    smart_contract += f"    }}\n\n"
                elif action.endswith('>'):
                    function_name = action[:-1]
                    smart_contract += f"    function {function_name}() public {{\n"
                    smart_contract += f"        // Function logic\n"
                    smart_contract += f"    }}\n\n"
                elif action.endswith(')'):
                    parts = action.split('>')
                    caller = parts[0]
                    function_name = parts[1][:-1]
                    smart_contract += f"    function {function_name}() public {{\n"
                    smart_contract += f"        require(msg.sender == {caller}, 'Only caller can execute this function');\n"
                    smart_contract += f"        // Function logic\n"
                    smart_contract += f"    }}\n\n"

    smart_contract += "}\n"
    return smart_contract


input_file = 'input.txt'
output_contract = generate_smart_contract(input_file)
print(output_contract)
