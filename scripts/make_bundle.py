import re
from pathlib import Path
from string import Template
import hashlib

main_css_file = Path("main.css")
output_file_template = Template("bundle.$hash.css")

with open(main_css_file) as r:
    main_content = r.read().splitlines()

output_data = []

for line in main_content:
    if line.startswith('@charset'):
        output_data.append(line)
    elif line.startswith('@import'):
        file_ref = line.split('"', 1)[-1].split('"', 1)[0]
        with open(file_ref) as r:
            file_content = r.read()
            output_data.append(file_content)
output_str = "\n".join(output_data)


# Remove comments
print("raw", len(output_str))
output_str = re.sub(r"/\*.*?\*/", '', output_str, 0, re.MULTILINE | re.DOTALL)
print("without comments", len(output_str))
output_str = re.sub(r" +", r' ', output_str, 0, re.MULTILINE | re.DOTALL)
print("only single spaces", len(output_str))
output_str = re.sub(r"\n+ ?", r'\n', output_str, 0, re.MULTILINE | re.DOTALL)
# output_str = re.sub(r"^\s*$", r'\n', output_str, 0, re.MULTILINE | re.DOTALL)
output_str = re.sub(r"\n+", r'\n', output_str, 0, re.MULTILINE | re.DOTALL)
print("only single line breaks", len(output_str))
# output_str = re.sub(r"\s+", r' ', output_str, 0, re.MULTILINE | re.DOTALL)
# print("only single white spaces", len(output_str))

file_hash = hashlib.md5(output_str.encode('utf-8')).hexdigest()
output_file = output_file_template.substitute(hash=file_hash)
print(output_file)
with open(output_file, 'w') as w:
    w.write(output_str)
