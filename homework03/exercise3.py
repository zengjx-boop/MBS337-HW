import json
import xmltodict

with open("proteinlist_hw3.json", "r") as f:
    data = json.load(f)


root = {}
root["proteins"] = {}
root["proteins"]["protein"] = data["protein_list"]


with open("proteins.xml", "w") as o:
    o.write(xmltodict.unparse(root, pretty=True)) #chatgpt is used here to understand the examples in the notes