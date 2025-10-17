"""
Webease Compiler - Compiles .ws files to HTML
"""

import re
import os
from pathlib import Path
from . import functions


class WebeaseCompiler:
    def __init__(self):
        self.context = None
        self.libraries = {}
        
    def compile_file(self, ws_file_path):
        """Compile a .ws file to HTML"""
        functions.reset_context()
        self.context = functions.get_context()
        
        with open(ws_file_path, 'r', encoding='utf-8') as f:
            ws_code = f.read()
        
        try:
            self.execute_webease_code(ws_code)
            html = self.generate_html()
            return html, None
        except Exception as e:
            return None, self.format_error(e)
    
    def execute_webease_code(self, code):
        """Execute Webease code"""
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            if not line or line.startswith('#'):
                continue
            
            try:
                if line.startswith('import_library('):
                    lib_match = re.match(r'import_library\(["\'](.+?)["\']\)', line)
                    if lib_match:
                        lib_name = lib_match.group(1)
                        self.load_library(lib_name)
                
                func_match = re.match(r'(\w+)\((.*)\)', line)
                if func_match:
                    func_name = func_match.group(1)
                    args_str = func_match.group(2)
                    
                    if hasattr(functions, func_name):
                        func = getattr(functions, func_name)
                        args, kwargs = self.parse_arguments(args_str)
                        func(*args, **kwargs)
                    elif func_name in self.context.custom_functions:
                        args, kwargs = self.parse_arguments(args_str)
                        functions.use_component(func_name, **kwargs)
                    else:
                        raise NameError(f"Function '{func_name}' is not defined")
                        
            except Exception as e:
                raise SyntaxError(f"Error on line {line_num}: {str(e)}")
    
    def parse_arguments(self, args_str):
        """Parse function arguments"""
        if not args_str.strip():
            return [], {}
        
        args = []
        kwargs = {}
        
        current_arg = ""
        in_string = False
        in_list = False
        in_dict = False
        string_char = None
        bracket_count = 0
        
        for char in args_str:
            if char in ('"', "'") and not in_string:
                in_string = True
                string_char = char
                current_arg += char
            elif char == string_char and in_string:
                in_string = False
                string_char = None
                current_arg += char
            elif char == '[' and not in_string:
                in_list = True
                bracket_count += 1
                current_arg += char
            elif char == ']' and not in_string:
                bracket_count -= 1
                current_arg += char
                if bracket_count == 0:
                    in_list = False
            elif char == '{' and not in_string:
                in_dict = True
                bracket_count += 1
                current_arg += char
            elif char == '}' and not in_string:
                bracket_count -= 1
                current_arg += char
                if bracket_count == 0:
                    in_dict = False
            elif char == ',' and not in_string and not in_list and not in_dict:
                arg = current_arg.strip()
                if '=' in arg and not arg.startswith('[') and not arg.startswith('{'):
                    key, value = arg.split('=', 1)
                    kwargs[key.strip()] = self.parse_value(value.strip())
                else:
                    args.append(self.parse_value(arg))
                current_arg = ""
            else:
                current_arg += char
        
        if current_arg.strip():
            arg = current_arg.strip()
            if '=' in arg and not arg.startswith('[') and not arg.startswith('{'):
                key, value = arg.split('=', 1)
                kwargs[key.strip()] = self.parse_value(value.strip())
            else:
                args.append(self.parse_value(arg))
        
        return args, kwargs
    
    def parse_value(self, value):
        """Parse a value from string to Python type"""
        value = value.strip()
        
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        elif value == 'True':
            return True
        elif value == 'False':
            return False
        elif value == 'None':
            return None
        elif value.startswith('[') and value.endswith(']'):
            list_content = value[1:-1]
            if not list_content.strip():
                return []
            items = []
            current_item = ""
            in_string = False
            string_char = None
            bracket_count = 0
            
            for char in list_content:
                if char in ('"', "'") and not in_string:
                    in_string = True
                    string_char = char
                    current_item += char
                elif char == string_char and in_string:
                    in_string = False
                    string_char = None
                    current_item += char
                elif char in ('[', '{') and not in_string:
                    bracket_count += 1
                    current_item += char
                elif char in (']', '}') and not in_string:
                    bracket_count -= 1
                    current_item += char
                elif char == ',' and not in_string and bracket_count == 0:
                    items.append(self.parse_value(current_item.strip()))
                    current_item = ""
                else:
                    current_item += char
            
            if current_item.strip():
                items.append(self.parse_value(current_item.strip()))
            return items
        elif value.startswith('{') and value.endswith('}'):
            dict_content = value[1:-1]
            if not dict_content.strip():
                return {}
            result = {}
            items = []
            current_item = ""
            in_string = False
            string_char = None
            bracket_count = 0
            
            for char in dict_content:
                if char in ('"', "'") and not in_string:
                    in_string = True
                    string_char = char
                    current_item += char
                elif char == string_char and in_string:
                    in_string = False
                    string_char = None
                    current_item += char
                elif char in ('[', '{') and not in_string:
                    bracket_count += 1
                    current_item += char
                elif char in (']', '}') and not in_string:
                    bracket_count -= 1
                    current_item += char
                elif char == ',' and not in_string and bracket_count == 0:
                    items.append(current_item.strip())
                    current_item = ""
                else:
                    current_item += char
            
            if current_item.strip():
                items.append(current_item.strip())
            
            for item in items:
                if ':' in item:
                    key, val = item.split(':', 1)
                    result[self.parse_value(key.strip())] = self.parse_value(val.strip())
            return result
        else:
            try:
                if '.' in value:
                    return float(value)
                return int(value)
            except ValueError:
                return value
    
    def load_library(self, library_name):
        """Load a .wl library file"""
        library_path = Path(f'libraries/{library_name}.wl')
        
        if not library_path.exists():
            library_path = Path(f'{library_name}.wl')
        
        if not library_path.exists():
            raise FileNotFoundError(f"Library '{library_name}' not found")
        
        with open(library_path, 'r', encoding='utf-8') as f:
            library_code = f.read()
        
        lines = library_code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('component '):
                comp_match = re.match(r'component\s+(\w+)\s*\{', line)
                if comp_match:
                    comp_name = comp_match.group(1)
                    comp_code = []
                    i += 1
                    brace_count = 1
                    
                    while i < len(lines) and brace_count > 0:
                        current_line = lines[i]
                        
                        for char in current_line:
                            if char == '{':
                                brace_count += 1
                            elif char == '}':
                                brace_count -= 1
                        
                        if brace_count > 0:
                            comp_code.append(current_line)
                        elif brace_count == 0 and not current_line.strip() == '}':
                            comp_code.append(current_line.rstrip('}'))
                        
                        i += 1
                    
                    self.context.custom_functions[comp_name] = '\n'.join(comp_code).strip()
            i += 1
    
    def generate_html(self):
        """Generate final HTML output"""
        css = '\n'.join(self.context.css_rules)
        js = '\n'.join(self.context.js_code)
        html_content = '\n'.join(self.context.html_parts)
        head_parts = '\n'.join(self.context.head_parts)
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {head_parts if head_parts else '<title>Webease Page</title>'}
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        {css}
    </style>
</head>
<body>
    {html_content}
    <script>
        {js}
    </script>
</body>
</html>"""
        return html
    
    def format_error(self, error):
        """Format error message for beginners"""
        error_type = type(error).__name__
        error_msg = str(error)
        
        suggestions = {
            'NameError': "Check if the function name is spelled correctly. Available functions are listed in the documentation.",
            'SyntaxError': "Check if your parentheses (), quotes \", and brackets [] are properly closed.",
            'TypeError': "Check if you're passing the right type of values to the function (text in quotes, numbers without quotes).",
            'FileNotFoundError': "The file or library you're trying to load doesn't exist. Check the file path.",
        }
        
        suggestion = suggestions.get(error_type, "Check your code for any mistakes.")
        
        return f"""
╔══════════════════════════════════════════════════════════════╗
║  WEBEASE ERROR                                               ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Error Type: {error_type:<47}║
║                                                              ║
║  Message: {error_msg:<50}║
║                                                              ║
║  💡 Suggestion:                                             ║
║  {suggestion:<59}║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
