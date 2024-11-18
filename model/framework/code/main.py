# imports
import os
import csv
import sys
import requests
import random

# loading CHEESE API key from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
with open(dotenv_path) as f:
    for l in f:
        key, value = l.strip().split("=")
        os.environ[key] = value[1:-1]
if "CHEESE_API_KEY" not in os.environ:
    raise ValueError("Missing CHEESE_API_KEY in .env file")

NUMBER_OF_COMPOUNDS = 100
NUMBER_OF_ATTEMPTS = 10

CHEESE_API_KEY = os.environ["CHEESE_API_KEY"]

DB_NAMES = [
    "ENAMINE-REAL",
    "ZINC15",
    "MCULE-FULL",
    "MCULE-IN-STOCK",
    "EXPLORE-ENUMERATED",
    "CHEMRIYA",
    "EXPLORE-DIVERSE"
]

SEARCH_TYPES = [
    "morgan",
    "espsim_electrostatic",
    "espsim_shape",
    "active_pairs",
    "consensus"
]

FIXED_FILTERS = ["No solvents"]
VARIABLE_FILTERS = ["Murcko scaffold hop", "Regioisomers", "PAINS", "QED", "No rare atoms"]

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run queries
def individual_query(smiles):
    print("Querying CHEESE API for SMILES: ", smiles)
    url = "https://cheesemoldapi.com/api/v1/cheese"
    headers = {"accept": "application/json", "X-API-key": CHEESE_API_KEY}
    url = "https://api.cheese.themama.ai/molsearch"
    data = {
        "search_input": smiles,
        "search_type": random.choice(SEARCH_TYPES),
        "search_quality": "very accurate",
        "db_names": [random.choice(DB_NAMES)],
        "n_neighbors": 30,
        "descriptors": False,
        "properties": False,
        "filter_molecules": True,
        "order_molecules": True,
        "filtering": [FIXED_FILTERS] + [random.choice(VARIABLE_FILTERS)],
        "ordering": "Similarity"
    }
    response = requests.get(url, data, headers=headers)
    data = response.json()
    return data

def repetitive_query(smiles):
    output_smiles = []
    for _ in range(NUMBER_OF_ATTEMPTS):
        data = individual_query(smiles)
        if "neighbors" not in data:
            continue
        print("Found {0} neighbors for SMILES: {1}".format(len(data["neighbors"]), smiles))
        for neigh in data["neighbors"]:
            output_smiles.append(neigh["smiles"])
        output_smiles = list(set(output_smiles))
        if len(output_smiles) >= NUMBER_OF_COMPOUNDS:
            break
    output_smiles = output_smiles[:NUMBER_OF_COMPOUNDS]
    if len(output_smiles) < NUMBER_OF_COMPOUNDS:
        output_smiles += [""] * (NUMBER_OF_COMPOUNDS - len(output_smiles))
    return output_smiles

outputs = []
for smiles in smiles_list:
    outputs += [repetitive_query(smiles)]

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["smiles-{0}".format(str(i).zfill(3)) for i in range(NUMBER_OF_COMPOUNDS)])
    for o in outputs:
        writer.writerow(o)