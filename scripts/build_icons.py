import re
from urllib.parse import quote
from pathlib import Path
from string import Template
import yaml

icons_dir = Path(r"C:\Users\admin\Code\THIRD_PARTY\tabler-icons\svg\outline")
icon_filename_template = Template("$name.svg")
spec_file = Path("icon_sets.yml")
out_dir = Path('.')
out_filename_template = Template("icons_$group.css")
css_var_name_template = Template("--brick-icon-$name")
css_var_template = Template('    $varname: url("$content");')
css_attr_template = Template("""
[data-icon="$name"] {
    --_icon: var($varname);
}
""")
css_template = Template("""
:root {
$icons
}
$attrs
""".strip())


def encode_svg(text: str) -> str:
    text = text.replace('\n', ' ')
    text = re.sub(r"\s+", " ", text, re.MULTILINE)
    text = re.sub(r'class=".+?"', "", text)
    text = text.strip().replace('  ', ' ').replace('"', "'").lower()
    text = text.replace("stroke='currentColor'", "stroke='rgb(0,0,0)'")
    text = quote(text, safe="!~*'() /=:")
    return f'data:image/svg+xml,{text}'

def build_icon_file(group: str, icons: dict[str, str]):
    outfile = out_dir / out_filename_template.safe_substitute(group=group)
    print(group)
    css_vars = []
    css_attrs = []
    for icon_name, icon_filename in icons.items():
        icon_path = icons_dir / icon_filename_template.safe_substitute(name=icon_filename)
        if not icon_path.exists():
            print("ERROR: could not find icon.", icon_path)
            continue
        with open(icon_path) as r:
            icon_content = r.read()
        css_content = encode_svg(icon_content)
        varname = css_var_name_template.substitute(name=icon_name)
        css_vars.append(
            css_var_template.substitute(
                varname=varname, content=css_content))
        css_attrs.append(
            css_attr_template.substitute(
                name=icon_name, varname=varname
            )
        )
    css_output = css_template.substitute(
        icons="\n".join(css_vars),
        attrs="\n".join(css_attrs))
    with open(outfile, 'w') as w:
        w.write(css_output)



def main():
    with open(spec_file) as r:
        spec = yaml.safe_load(r.read())
    for group, icons in spec.items():
        build_icon_file(group, icons)

if __name__ == '__main__':
    main()