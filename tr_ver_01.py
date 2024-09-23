import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

# Lexer for breaking down Python code into tokens
def lexer(python_code):
    tokens = []
    python_code = python_code.strip().splitlines()

    patterns = {
        'VAR_ASSIGN': r'(\w+)\s*=\s*(.+)',
        'IF': r'if\s+(.+):',
        'FOR': r'for\s+(\w+)\s+in\s+range\((.+)\):',
        'WHILE': r'while\s+(.+):',
        'DEF_FUNC': r'def\s+(\w+)\((.*)\):',
        'RETURN': r'return\s+(.+)',
        'PRINT': r'print\s*\((.*)\)',
    }

    for line in python_code:
        matched = False
        for token_type, pattern in patterns.items():
            match = re.match(pattern, line.strip())
            if match:
                tokens.append((token_type, match.groups()))
                matched = True
                break
        if not matched:
            if line.strip() == "":
                tokens.append(('NEWLINE', ''))
            else:
                tokens.append(('UNKNOWN', line.strip()))
    return tokens

# Parser for turning tokens into a simple syntax representation
def parser(tokens):
    parsed_code = []
    indent_level = 0

    for token in tokens:
        token_type, token_value = token
        if token_type == 'VAR_ASSIGN':
            parsed_code.append(('VAR_ASSIGN', token_value))
        elif token_type == 'IF':
            parsed_code.append(('IF', token_value, indent_level))
            indent_level += 1
        elif token_type == 'FOR':
            parsed_code.append(('FOR', token_value, indent_level))
            indent_level += 1
        elif token_type == 'WHILE':
            parsed_code.append(('WHILE', token_value, indent_level))
            indent_level += 1
        elif token_type == 'DEF_FUNC':
            parsed_code.append(('DEF_FUNC', token_value, indent_level))
            indent_level += 1
        elif token_type == 'RETURN':
            parsed_code.append(('RETURN', token_value))
        elif token_type == 'PRINT':
            parsed_code.append(('PRINT', token_value))
        elif token_type == 'NEWLINE':
            parsed_code.append(('NEWLINE', ''))

    return parsed_code

# Generator to convert Python code to Java code
def generate_java(parsed_code):
    java_code = []
    indent = "    "  # 4 spaces for indentation
    current_indent_level = 0

    for statement in parsed_code:
        statement_type = statement[0]

        if statement_type == 'VAR_ASSIGN':
            var_name, value = statement[1]
            # Simple variable type inference
            if re.match(r'^\d+$', value):
                java_code.append(f"int {var_name} = {value};")
            elif re.match(r'^\d+\.\d+$', value):
                java_code.append(f"double {var_name} = {value};")
            elif re.match(r'^\".*\"$', value) or re.match(r'^\'[^\']+\'$', value):
                java_code.append(f"String {var_name} = {value};")
            else:
                java_code.append(f"String {var_name} = \"{value}\";")  # Treat other cases as string

        elif statement_type == 'IF':
            condition = statement[1][0]
            condition = condition.replace("== None", "== null")
            condition = condition.replace("!=", "!=")
            indent_level = statement[2]
            java_code.append(indent * indent_level + f"if ({condition}) " + "{")
            current_indent_level = indent_level + 1

        elif statement_type == 'FOR':
            var_name, range_value = statement[1]
            indent_level = statement[2]
            java_code.append(indent * indent_level + f"for (int {var_name} = 0; {var_name} < {range_value}; {var_name}++) " + "{")
            current_indent_level = indent_level + 1

        elif statement_type == 'WHILE':
            condition = statement[1][0]
            indent_level = statement[2]
            java_code.append(indent * indent_level + f"while ({condition}) " + "{")
            current_indent_level = indent_level + 1

        elif statement_type == 'DEF_FUNC':
            func_name, params = statement[1]
            params_list = params.split(",") if params else []
            formatted_params = ', '.join(f'String {param.strip()}' for param in params_list)  # Assuming all params are strings
            indent_level = statement[2]
            java_code.append(indent * indent_level + f"void {func_name}({formatted_params}) " + "{")
            current_indent_level = indent_level + 1

        elif statement_type == 'RETURN':
            value = statement[1][0]
            java_code.append(indent * current_indent_level + f"return {value};")

        elif statement_type == 'PRINT':
            value = statement[1][0].strip()
            java_code.append(indent * current_indent_level + f'System.out.println({value});')

        elif statement_type == 'NEWLINE':
            java_code.append("")

    java_code.append("}" * current_indent_level)  # Close all open blocks
    return "\n".join(java_code)

class TranslatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_code = TextInput(size_hint=(1, 0.7), multiline=True, hint_text="Enter Python code here...")
        self.output_code = TextInput(size_hint=(1, 0.2), multiline=True, readonly=True, hint_text="Translated Java code will appear here...")

        translate_button = Button(text="Translate", size_hint=(1, 0.1))
        translate_button.bind(on_press=self.translate_code)

        layout.add_widget(self.input_code)
        layout.add_widget(self.output_code)
        layout.add_widget(translate_button)

        return layout

    def translate_code(self, instance):
        python_code = self.input_code.text
        tokens = lexer(python_code)
        parsed_code = parser(tokens)
        java_code = generate_java(parsed_code)
        self.output_code.text = java_code

if __name__ == "__main__":
    TranslatorApp().run()
