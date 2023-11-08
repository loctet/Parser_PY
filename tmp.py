import re

def extract_functions_and_parameters(input_string):
    # Regular expression to match function definitions
    function_pattern = r'\b(\w+)\(([^()]|(?R))*\)'
    # Find all function definitions in the input string
    function_matches = re.findall(function_pattern, input_string)

    # Extract function names and their parameters
    extracted_functions = []
    for match in function_matches:
        function_name, function_params = match.split('(', 1)
        # Remove any trailing ')' character
        function_params = function_params.rstrip(')')
        # Split parameters by commas while respecting nested parentheses
        params_list = []
        param_buffer = ""
        paren_count = 0
        for char in function_params:
            if char == '(':
                paren_count += 1
            elif char == ')':
                paren_count -= 1
            if char == ',' and paren_count == 0:
                params_list.append(param_buffer.strip())
                param_buffer = ""
            else:
                param_buffer += char
        if param_buffer:
            params_list.append(param_buffer.strip())

        extracted_functions.append((function_name, params_list))

    # Format the extracted functions and parameters
    result = []
    for function_name, params_list in extracted_functions:
        formatted_params = ' '.join(params_list)
        result.append(f"{function_name} {formatted_params}")

    return ', '.join(result)

# Test the function with the provided example
input_string = "forall(M, item > 0), exist(M, len(M) > 4)"
result = extract_functions_and_parameters(input_string)
print(result)
