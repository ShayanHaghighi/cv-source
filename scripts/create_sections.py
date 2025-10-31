import yaml

INPUT_FILE = "data/skills.yaml"
OUTPUT_DIR = "sections/skills/parts"

def format_list(k,l:list[str]):
    s = f"\\textbf{{{k.capitalize()}:}}  "
    s += ", ".join(l)
    return s + " \\\\"

with open("data/skills.yaml") as stream:
    try:
        obj = yaml.safe_load(stream)

        for k,v in obj.items():
            filename = k.replace("/","_")
            with open(f"{OUTPUT_DIR}/{filename}.tex",'w+') as output_file:
                output_file.write(format_list(k,v))

    except yaml.YAMLError as exc:
        print(exc)