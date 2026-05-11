import json
import os
import re

def process_all():
    with open('pending_audit.json', 'r') as f:
        data = json.load(f)
    ids = data.get('pending', [])
    success = 0
    skipped = 0

    for pip in ids:
        filepath = f"archive/scripts/make_standard_{pip}.py"
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'    boilerplate\s*=\s*\{.*?\n    \}', content, flags=re.DOTALL)
        if not match:
            skipped += 1
            print(f"Skipped {pip} (no boilerplate block found)")
            continue

        boiler_str = match.group(0)
        
        py_match = re.search(r'"python"\s*:\s*"(.*?)"', boiler_str, flags=re.DOTALL)
        cpp_match = re.search(r'"cpp"\s*:\s*"(.*?)"', boiler_str, flags=re.DOTALL)

        if not py_match or not cpp_match:
            skipped += 1
            print(f"Skipped {pip} (missing python/cpp boilerplate string)")
            continue

        py_code = py_match.group(1).encode('utf-8').decode('unicode_escape')
        cpp_code = cpp_match.group(1).encode('utf-8').decode('unicode_escape')

        sig_match = re.search(r'([\w\:\<\>\*]+)\s+(\w+)\s*\((.*?)\)\s*\{', cpp_code)
        if not sig_match:
            sig_match = re.search(r'([\w\:\<\>\*]+)\s+(\w+)\s*\((.*?)\)\s*[\{;]', cpp_code)
        
        if not sig_match:
            skipped += 1
            print(f"Skipped {pip} (could not parse C++ signature)")
            continue
            
        ret_type, func_name, args_str = sig_match.groups()
        if 'ListNode' in cpp_code or 'TreeNode' in cpp_code or 'class ' in py_code:
            skipped += 1
            print(f"Skipped {pip} (OOP/Tree/List detected)")
            continue

        args = []
        if args_str.strip():
            for arg in args_str.split(','):
                arg = arg.strip()
                if not arg: continue
                parts = arg.split()
                name = parts[-1].replace('&', '').replace('*', '')
                t = " ".join(parts[:-1]).replace('&', '').strip()
                args.append((t, name))
        
        if not args:
            skipped += 1
            print(f"Skipped {pip} (no arguments)")
            continue
            
        is_unsupported = False
        for t, n in args:
            if t not in ['int', 'string', 'vector<int>', 'vector<vector<int>>']:
                is_unsupported = True
        
        if is_unsupported:
            skipped += 1
            print(f"Skipped {pip} (unsupported args type)")
            continue
            
        new_cpp = generate_cpp(ret_type, func_name, args)
        new_java = generate_java(ret_type, func_name, args)
        new_js = generate_js(ret_type, func_name, args)
        new_py = generate_py(ret_type, func_name, args)
        new_c = generate_c(ret_type, func_name, args)

        def escape_for_dict(s):
            return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

        new_boiler_str = f'''    boilerplate = {{
        "python": "{escape_for_dict(new_py)}",
        "cpp": "{escape_for_dict(new_cpp)}",
        "java": "{escape_for_dict(new_java)}",
        "javascript": "{escape_for_dict(new_js)}",
        "c": "{escape_for_dict(new_c)}"
    }}'''

        new_content = content.replace(boiler_str, new_boiler_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        success += 1

    print(f"Done. Processed: {success}, Skipped: {skipped}")

def generate_cpp(ret_type, func_name, args):
    args_str = ", ".join([f"{t}& {n}" if "vector" in t or "string" in t else f"{t} {n}" for t, n in args])
    code = f"""#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

{ret_type} {func_name}({args_str}) {{
    // User logic here
    return {{}};
}}

int main() {{
    string input;
    while (getline(cin, input)) {{
        if (input.empty()) continue;
        string cleaned = "";
        for (char c : input) {{
            if (c != '[' && c != ']' && c != ' ') cleaned += c;
        }}
        stringstream ss(cleaned);
        string item;
"""
    call_args = []
    has_2d = False
    has_1d = False
    
    for t, n in args:
        if t == "vector<vector<int>>":
            code += f"""
        vector<int> flat_{n};
        while (getline(ss, item, ',')) {{ flat_{n}.push_back(stoi(item)); }}
        vector<vector<int>> {n};
        for (size_t i = 0; i < flat_{n}.size(); i += 2) {{
            {n}.push_back({{flat_{n}[i], flat_{n}[i+1]}});
        }}"""
            call_args.append(n)
            has_2d = True
        elif t == "vector<int>":
            code += f"""
        vector<int> {n};
        while (getline(ss, item, ',')) {{ {n}.push_back(stoi(item)); }}"""
            call_args.append(n)
            has_1d = True
        elif t == "int":
            code += f"""
        int {n};
        cin >> {n};"""
            call_args.append(n)
    
    # simplistic logic for single vector arguments:
    if len(args) == 1:
        code += f"""
        auto res = {func_name}({call_args[0]});
        cout << res << endl; // Simplistic output mapping
"""
    else:
         code += f"        // Call function properly mapped\n"
         
    code += "    }\n    return 0;\n}"
    return code

def generate_java(ret_type, func_name, args):
    java_ret = ret_type
    if java_ret == "vector<int>": java_ret = "int[]"
    elif java_ret == "vector<vector<int>>": java_ret = "int[][]"
    elif java_ret == "string": java_ret = "String"
    
    args_str = ", ".join([f"int[] {n}" if t == "vector<int>" else (f"int[][] {n}" if t == "vector<vector<int>>" else (f"String {n}" if t=="string" else f"int {n}")) for t, n in args])
    
    code = f"""import java.util.*;

public class Main {{
    public static {java_ret} {func_name}({args_str}) {{
        // User logic here
        return null;
    }}
    
    public static void main(String[] args) {{
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {{
            String input = sc.nextLine().trim();
            if (input.isEmpty()) continue;
"""
    call_args = []
    
    for t, n in args:
        if t == "vector<int>":
            code += f"""
            input = input.replaceAll("\\\\[", "").replaceAll("\\\\]", "").replaceAll("\\\\s+", "");
            String[] nums_{n} = input.split(",");
            int[] {n} = new int[nums_{n}.length];
            if(!input.isEmpty()) for (int i = 0; i < nums_{n}.length; i++) {n}[i] = Integer.parseInt(nums_{n}[i]);"""
            call_args.append(n)
        elif t == "vector<vector<int>>":
            code += f"""
            input = input.replaceAll("\\\\[", "").replaceAll("\\\\]", "").replaceAll("\\\\s+", "");
            String[] nums_{n} = input.split(",");
            int[][] {n} = new int[nums_{n}.length / 2][2];
            if(!input.isEmpty()) for (int i = 0; i < nums_{n}.length / 2; i++) {{
                {n}[i][0] = Integer.parseInt(nums_{n}[2 * i]);
                {n}[i][1] = Integer.parseInt(nums_{n}[2 * i + 1]);
            }}"""
            call_args.append(n)
        elif t == "int":
            code += f"\n            int {n} = Integer.parseInt(sc.nextLine().trim());"
            call_args.append(n)
        elif t == "string":
             code += f"\n            String {n} = input;"
             call_args.append(n)
            
    if len(args) == 1:
        code += f"\n            System.out.println({func_name}({call_args[0]}));"
        
    code += "\n        }\n    }\n}"
    return code

def generate_js(ret_type, func_name, args):
    code = f"""const fs = require('fs');

function {func_name}({", ".join([n for _, n in args])}) {{
    // User logic here
    return 0;
}}

const input = fs.readFileSync(0, 'utf-8').trim().split('\\n');
if (input.length > 0 && input[0]) {{
"""
    call_args = []
    for i, (t, n) in enumerate(args):
        if "vector" in t:
             code += f"    const {n} = JSON.parse(input[{i}]);\n"
             call_args.append(n)
        else:
             code += f"    const {n} = input[{i}];\n"
             call_args.append(n)
             
    if len(args) == 1:
         code += f"    console.log({func_name}({call_args[0]}));"
         
    code += "\n}"
    return code

def generate_py(ret_type, func_name, args):
    code = f"""import sys, json

def {func_name}({", ".join([n for _, n in args])}):
    # User logic here
    pass

if __name__ == '__main__':
    data = sys.stdin.read().strip().splitlines()
    if data:
"""
    call_args = []
    for i, (t, n) in enumerate(args):
        if "vector" in t:
             code += f"        {n} = json.loads(data[{i}])\n"
             call_args.append(n)
        else:
             code += f"        {n} = data[{i}]\n"
             call_args.append(n)
             
    if len(args) == 1:
         code += f"        print({func_name}({call_args[0]}))"
    return code

def generate_c(ret_type, func_name, args):
    code = f"""#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int {func_name}() {{
    // User logic here
    return 0;
}}

int main() {{
    char input[1000000];
    if (fgets(input, sizeof(input), stdin)) {{
        // C Parsing generic
        printf(\"0\\n\");
    }}
    return 0;
}}"""
    return code

if __name__ == "__main__":
    process_all()
