import json

def export_project_to_json(result_dict, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result_dict, f, indent=2)