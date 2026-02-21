#!/bin/bash

# Flashcard Web Server Start Script
# Kills any existing server on port 8080 and starts fresh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Flashcard Web Server - Starting up..."
echo ""

# Kill any existing process on port 8080
echo "Checking for existing server on port 8080..."
if command -v lsof &> /dev/null; then
    PID=$(lsof -ti:8080 2>/dev/null)
    if [ ! -z "$PID" ]; then
        echo "Found existing process (PID: $PID), stopping..."
        kill $PID 2>/dev/null
        sleep 1
    fi
elif command -v fuser &> /dev/null; then
    fuser -k 8080/tcp 2>/dev/null
fi

echo ""

# Start the server
cd "$SCRIPT_DIR" || exit 1
python3 server.py
