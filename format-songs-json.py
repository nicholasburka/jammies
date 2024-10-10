import json
import re

def format_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace newlines within quotes with \n
    content = re.sub(r'(?<!\\)"[^"]*"', lambda m: m.group(0).replace('\n', '\\n'), content)

    # Parse the modified content
    data = json.loads(content)

    # Write formatted JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Formatted JSON has been written to {output_file}")

# Use the script
format_json('songs_raw.json', 'songs.json')
