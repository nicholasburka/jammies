import os
import json
import re

def check_file_exists(filepath):
    if not os.path.exists(filepath):
        print(f"ERROR: {filepath} does not exist!")
    else:
        print(f"OK: {filepath} exists.")

def check_directory_exists(dirpath):
    if not os.path.isdir(dirpath):
        print(f"ERROR: {dirpath} directory does not exist!")
    else:
        print(f"OK: {dirpath} directory exists.")

def check_json_structure(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        if isinstance(data, dict) and all(isinstance(v, list) for v in data.values()):
            print(f"OK: {filepath} has the correct structure.")
        else:
            print(f"ERROR: {filepath} does not have the expected structure!")
    except json.JSONDecodeError:
        print(f"ERROR: {filepath} is not a valid JSON file!")
    except FileNotFoundError:
        print(f"ERROR: {filepath} does not exist!")

def check_numeric_prefix(filename):
    return bool(re.match(r'^\d+_', filename))

def main():
    print("Checking project structure...")
    
    # Check main files
    check_file_exists('index.html')
    check_file_exists('songs.json')
    check_file_exists('generate_songs_json.py')
    
    # Check directories
    check_directory_exists('audio')
    check_directory_exists('sheets')
    
    # Check audio subdirectories
    for subdir in ['pre-show', 'intros', 'music set']:
        check_directory_exists(os.path.join('audio', subdir))
        check_directory_exists(os.path.join('sheets', subdir))
    
    # Check songs.json structure
    check_json_structure('songs.json')
    
    print("\nChecking audio files...")
    with open('songs.json', 'r') as f:
        songs_data = json.load(f)
    
    for section, songs in songs_data.items():
        for song in songs:
            audio_path = os.path.join('audio', section, f"{song['file']}.mp3")
            check_file_exists(audio_path)
            
            if not check_numeric_prefix(f"{song['file']}.mp3"):
                print(f"WARNING: {audio_path} does not have a numeric prefix!")
            
            sheet_path = os.path.join('sheets', section, f"{song['file']}.pdf")
            check_file_exists(sheet_path)

if __name__ == "__main__":
    main()
