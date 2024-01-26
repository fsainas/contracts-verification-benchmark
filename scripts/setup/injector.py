'''
Collection of function to inject code.

Usage:
    python injector.py -b <base_file_path> -i <to_inject_path> [-o <output_dir>]
'''

INDENT_STRING = '    '  # 4 whitespaces


def get_indentation(line: str):
    '''
    Given a line returns the indentation string (whitespaces and tabs).
    '''

    # Find the length of leading white spaces and tabs
    leading_whitespace_length = len(line) - len(line.lstrip())
    # Store the leading white spaces and tabs
    leading_whitespace = line[:leading_whitespace_length]

    return leading_whitespace


'''IMPROVEMENT
The functions inject_before_last_bracket, inject_precond and inject_postcond
handle code as a list of lines, while the other functions operate directly on
files. Consider enhancing coherence.
'''
def inject_before_last_bracket(base_code: list, to_inject_code: list):
    '''
    Injects code after the last closing bracket. 
    Returns None if there is no last bracket.
    '''
    
    last_bracket_index = None
    # Search the match
    for i, line in enumerate(base_code):    # Improve by looking from the bottom
        if '}' in line:
            last_bracket_index = i

    indentation = get_indentation(base_code[last_bracket_index]) + INDENT_STRING

    #print(to_inject_code)
    if last_bracket_index:
        return (base_code[:last_bracket_index] + 
                [indentation + l for l in to_inject_code] + 
                ['\n' if to_inject_code[-1] != '\n' else ''] +  # Make sure to not write inside an existing line
                base_code[last_bracket_index:])
    else: 
        return None


def inject_after(base_code: list, to_inject_code: list, pattern: str) -> list:
    '''
    Finds a line that matches the pattern and injects code after it. 
    Returns None if no match is found.
    '''

    # Search the match
    for i, line in enumerate(base_code):
        if pattern in line:
            indentation = get_indentation(line) + INDENT_STRING
            return (base_code[:i+1] + 
                    [indentation + l for l in to_inject_code] + 
                    ['\n' if to_inject_code[-1][-1] != '\n' else ''] +  # Make sure to not write inside an existing line
                    base_code[i+1:])

    return None


def inject_postcond(base_code: list, to_inject_code: list, pattern: str):
    '''
    Injects a postcondition into a function. 
    Returns None if the operation fails.
    '''

    function_start = None
    function_end = None
    return_line = None
    open_brackets = 0
    open_comment = False

    # Search the match
    for i, line in enumerate(base_code):
        # Handle comments
        if open_comment:
            if '*/' in line:
                open_comment = False
            continue

        if '/*' in line and '*/' not in line:
            open_comment = True
            continue

        if line.startswith('//'):
            continue

        if pattern in line:
            function_start = i

        # If the function has started, increment the bracket counter
        if function_start:
            open_brackets += line.count('{') - line.count('}')

            if open_brackets == 0:
                # Function body is closed, record the index
                function_end = i
                break

            # Check for 'return' statement inside the function
            if 'return ' in line:
                return_line = i
                break

    indentation = ''
    if return_line:
        i = return_line
        indentation = get_indentation(base_code[i])     # Same level of indentation
    elif function_end:
        i = function_end
        indentation = get_indentation(base_code[i]) + INDENT_STRING
    else:
        return None

    return (base_code[:i] +
            [indentation + l for l in to_inject_code] +
            base_code[i:])


def inject_code(base_file: str, to_inject_file: str) -> str:
    '''
    Injects code of a to-inject file before the last bracket of a base file.

    Returns:
        str: updated_file
    '''

    base_code = ''
    to_inject_code = ''

    with open(base_file, 'r') as file:
        base_code = file.read()

    with open(to_inject_file, 'r') as file:
        to_inject_code = file.read()

    to_inject_code = (   # indentation
            '    ' +
            to_inject_code.replace('\n', '\n    ') +
            '\n\n'
    )

    last_brace_index = base_code.rfind('}')
    updated_file = (
            base_code[:last_brace_index] +
            to_inject_code +
            base_code[last_brace_index:]
    )

    return updated_file


def inject_product(base_files: list, to_inject_files: list) -> dict:
    '''
    Returns:
        dict: { filename: file_contents, ...}
    '''

    updated_files = {}

    for b_path in base_files:

        # Extract file name from base path
        file_name = ''.join(b_path.split('/')[-1].split('_')[0:-1])
        file_ext = b_path.split('.')[-1]

        # Extract base id from base path (e.g. v1)
        b_id = b_path.split('/')[-1].split('_')[-1].split('.')[0]

        for i_path in to_inject_files:
            # e.g. p1 for solcmc or getters for certora
            i_id = i_path.split('.')[-2].split('/')[-1].split('_')[0]
            file = inject_code(b_path, i_path)
            filename = file_name + '_' + i_id + '_' + b_id + '.' + file_ext
            updated_files[filename] = file 

    return updated_files
