#!/bin/bash

# Generate songs.json
python generate_songs_json.py

# Add all changes to git
git add .

# Commit changes
echo "Enter commit message:"
read commit_message
git commit -m "$commit_message"

# Push to GitHub
git push

echo "Website updated successfully!"
