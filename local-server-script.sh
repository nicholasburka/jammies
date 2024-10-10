#!/bin/bash

# Navigate to your project directory
# cd /path/to/your/project

# Start the Python HTTP server
if command -v python3 &>/dev/null; then
    python3 -m http.server 8000
elif command -v python &>/dev/null; then
    python -m SimpleHTTPServer 8000
else
    echo "Python is not installed on this system."
    exit 1
fi
