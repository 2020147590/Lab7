import re

file_path = 'input_7_1.txt'
def find_functions(file_path):
    functions = {}
    # Define a regular expression pattern
    pattern_def = re.compile(r'def\s+([a-zA-Z0-9_]*)\(')

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_num, line in enumerate(lines, start=1):
            func_definition = pattern_def.search(line)
            if func_definition:
                name = func_definition.group(1)
                functions[name] = {'def': line_num, 'calls': []}
            for func_name, info in functions.items():
                if len(func_name) > 0:
                    call = re.compile(rf'{func_name}\(').search(line)
                    if call and line_num != info['def']:
                        functions[func_name]['calls'].append(line_num)
    for func_name, info in functions.items():
        calls = ', '.join(str(call) for call in info['calls'])
        print(f"{func_name}: def in {info['def']}, calls in [{calls}]")

find_functions(file_path)
