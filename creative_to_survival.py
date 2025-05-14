import json
import os
import sys

def add_type_to_childs(obj):
    """
    Recursively traverse the JSON and add 'type': 0 to any dict that contains a 'childs' key.
    """
    if isinstance(obj, dict):
        if 'childs' in obj and isinstance(obj['childs'], list):
            # Only add if not already present
            if 'type' not in obj:
                obj['type'] = 0
        # Recursively apply to all values
        for key in obj:
            obj[key] = add_type_to_childs(obj[key])
    elif isinstance(obj, list):
        return [add_type_to_childs(item) for item in obj]
    return obj

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_data = add_type_to_childs(data)

    # Save with .blueprint extension
    base, _ = os.path.splitext(filepath)
    new_path = base + '.blueprint'
    with open(new_path, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=2)

    print(f"Blueprint saved as: {new_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python creative_to_survival.py "C:/path to file/blueprint.json"')
        sys.exit(1)

    input_path = sys.argv[1]
    if not input_path.lower().endswith('.json'):
        print("Input file must have blueprint.json")
        sys.exit(1)

    process_file(input_path)
