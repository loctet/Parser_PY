from solc import compile_standard
import json

def generate_fsm_input(contract_source_code):
    compiled_contract = compile_standard(
        {
            "language": "Solidity",
            "sources": {
                "contract.sol": {
                    "content": contract_source_code
                }
            },
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["stateMutability", "name", "inputs"]
                    }
                }
            }
        },
        allow_paths="./"  # Specify the path to your Solidity contract if necessary
    )

    fsm_input = []

    # Iterate over the compiled contracts
    for contract_file, contract_data in compiled_contract["contracts"].items():
        for contract_name, contract_info in contract_data.items():
            # Extract the function information
            for function_name, function_info in contract_info.get("abi", []):
                if function_info["type"] == "function":
                    inputs = []
                    for param in function_info.get("inputs", []):
                        inputs.append(param["type"])
                    fsm_input.append({
                        "contract": contract_name,
                        "function": function_name,
                        "inputs": inputs
                    })

    return fsm_input

# Example usage
contract_source_code = """
pragma solidity ^0.8.0;

contract MyContract {
    function foo(uint256 a, string memory b) public pure returns (bool) {
        // Function body
    }

    function bar(address[] calldata addresses, uint256[] calldata amounts) external {
        // Function body
    }
}
"""

fsm_input = generate_fsm_input(contract_source_code)
print(json.dumps(fsm_input, indent=4))
