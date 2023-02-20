import json

f = open("data.json")
d = json.load(f)

samples = d["sample_data"]["data"]
var_names = d["variable_labels"]

min_obj = 9999999

for i in range(len(samples)):

    if not d["vectors"]["is_feasible"]["data"][i]:
        continue

    for var_name in var_names:
        print(var_name, end="\t")

    print()

    for var_value in samples[i]:
        print(int(var_value), end="\t\t")

    print()

    print("objective: ", str(d["vectors"]["energy"]["data"][i]))
    print("is_feasible: ", str(d["vectors"]["is_feasible"]["data"][i]))

    if d["vectors"]["energy"]["data"][i] < min_obj:
        min_obj = d["vectors"]["energy"]["data"][i]

    print()

print(min_obj)

pass