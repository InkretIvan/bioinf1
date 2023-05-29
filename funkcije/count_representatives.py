import json

def count_representatives(filename):
    
    with open(filename) as file:
        json_data = json.load(file)
    representative_info = {}

    for obj in json_data:
        filename = obj["fileName"]
        representatives = obj["representatives"]

        for representative in representatives:
            if representative in representative_info:
                representative_info[representative]["count"] += 1
                representative_info[representative]["filenames"].append(filename)
            else:
                representative_info[representative] = {
                    "count": 1,
                    "filenames": [filename]
                }

    for representative, info in representative_info.items():
        count = info["count"]
        filenames = "\n".join(info["filenames"])
        print(f"Representative '{representative}' exists in {count} files: \n {filenames}")