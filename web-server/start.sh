#!/bin/bash
# Start Anki Flashcards Server

cd /home/dave/git/anki-flashcards

# Kill any existing server on port 8080
fuser -k 8080/tcp 2>/dev/null
sleep 1

# Start server from parent directory so it can access all files
python3 -m http.server 8080 --bind 0.0.0.0 &

sleep 2

echo "✅ Anki Flashcards Server Started!"
echo ""
echo "📱 Access URLs:"
echo "   Local:    http://localhost:8080/web-server/"
echo "   Tailscale: http://100.116.183.50:8080/web-server/"
echo ""
echo "📲 On your phone (with Tailscale connected):"
echo "   http://100.116.183.50:8080/web-server/"
