import yaml
from os import getcwd

CWD = getcwd()
INPUT_FILE = f"{CWD}/assets/skills.yaml"
OUTPUT_DIR = f"{CWD}/src/sections/skills/parts"

def format_list(key:str, l:list[str]):
    s = f"\\textbf{{{key.capitalize()}:}}  "
    s += ", ".join(l)
    return s + " \\\\"

with open(INPUT_FILE) as stream:
    try:
        obj = yaml.safe_load(stream)

        for k,v in obj.items():
            filename = k.replace("/","_")
            with open(f"{OUTPUT_DIR}/{filename}.tex",'w+') as output_file:
                output_file.write(format_list(k,v))

    except yaml.YAMLError as exc:
        print(exc)