import os
import json

def generate_songs_json(audio_dir, sheets_dir):
    songs = {}
    for section in sorted(os.listdir(audio_dir)):
        section_path = os.path.join(audio_dir, section)
        sheets_section_path = os.path.join(sheets_dir, section)
        if os.path.isdir(section_path):
            songs[section] = []
            for file in sorted(os.listdir(section_path)):
                if file.endswith('.mp3'):
                    title = ' '.join(file[:-4].split('_')).lstrip('0123456789_ ').title()
                    file_name = file[:-4]
                    sheet_music_exists = os.path.exists(os.path.join(sheets_section_path, f"{file_name}.pdf"))
                    songs[section].append({
                        "title": title,
                        "file": file_name,
                        "sheet_music": sheet_music_exists,
                        "notes": ""  # Initialize with empty notes
                    })
    
    with open('songs.json', 'w') as f:
        json.dump(songs, f, indent=2)

    print("songs.json has been generated successfully.")

# Specify the paths to your audio and sheets directories
audio_directory = './audio'
sheets_directory = './sheets'

# Generate the songs.json file
generate_songs_json(audio_directory, sheets_directory)
