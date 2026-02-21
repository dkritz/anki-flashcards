#!/usr/bin/env python3
"""
Anki Flashcards Web Server
Serves the flashcard web app on port 8080
Accessible via Tailscale for mobile devices
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

PORT = 8080
WEB_DIR = Path(__file__).parent

def get_tailscale_ip():
    """Get the Tailscale IP address"""
    try:
        import subprocess
        result = subprocess.run(['tailscale', 'ip', '-4'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    return None

class FlashcardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)
    
    def do_GET(self):
        # Allow CORS for mobile access
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        
        # Re-initialize to actually serve the file
        self.send_response_only(200)
        return super().do_GET()
    
    def log_message(self, format, *args):
        """Custom logging"""
        print(f"[{self.log_date_time_string()}] {args[0]}")

def main():
    os.chdir(WEB_DIR)
    
    with socketserver.TCPServer(("0.0.0.0", PORT), FlashcardHandler) as httpd:
        tailscale_ip = get_tailscale_ip()
        
        print("=" * 60)
        print("🎴 Anki Flashcards Server Started!")
        print("=" * 60)
        print(f"\n📱 Local access:     http://localhost:{PORT}")
        print(f"🌐 Network access:   http://0.0.0.0:{PORT}")
        
        if tailscale_ip:
            print(f"🔒 Tailscale access: http://{tailscale_ip}:{PORT}")
            print(f"\n📲 On your phone, open: http://{tailscale_ip}:{PORT}")
        else:
            print("\n⚠️  Tailscale not detected")
            print("   Install Tailscale for secure mobile access")
        
        print("\n" + "=" * 60)
        print("Press Ctrl+C to stop the server")
        print("=" * 60 + "\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")
            sys.exit(0)

if __name__ == "__main__":
    main()
