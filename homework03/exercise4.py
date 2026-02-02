import json
import yaml


with open("proteinlist_hw3.json", "r") as f:
    data = json.load(f)


with open("proteins.yaml", "w") as o:
    yaml.dump(
        data,
        o,
        sort_keys=False,      # chatgpt is used here and the following part bc i dont understand this part in the notes
        explicit_start=True,  
        explicit_end=True     
    )