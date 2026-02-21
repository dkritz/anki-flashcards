#!/usr/bin/env python3
"""
Flashcard Web Server
Serves the flashcard web app on port 8080
"""

import http.server
import socketserver
import socket
import os
import subprocess
import sys

PORT = 8080


def get_tailscale_ip():
    """Try to get Tailscale IP address"""
    try:
        # Try using tailscale command
        result = subprocess.run(
            ['tailscale', 'ip', '-4'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.CalledProcessError):
        pass
    
    # Try to find tailscale interface
    try:
        result = subprocess.run(
            ['ip', 'addr', 'show', 'dev', 'tailscale0'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                if 'inet ' in line:
                    ip = line.split()[1].split('/')[0]
                    return ip
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.CalledProcessError):
        pass
    
    return None


def get_local_ip():
    """Get local IP address"""
    try:
        # Create a socket to get the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Suppress default logging
        pass


def main():
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Get IP addresses
    local_ip = get_local_ip()
    tailscale_ip = get_tailscale_ip()
    
    print("=" * 60)
    print("  Flashcard Web Server")
    print("=" * 60)
    print()
    print(f"  Server starting on port {PORT}...")
    print()
    print("  Access URLs:")
    print(f"    Local:   http://localhost:{PORT}")
    print(f"    Local:   http://127.0.0.1:{PORT}")
    print(f"    Network: http://{local_ip}:{PORT}")
    if tailscale_ip:
        print(f"    VPN:     http://{tailscale_ip}:{PORT}")
    print()
    print("  Press Ctrl+C to stop")
    print("=" * 60)
    print()
    
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n  Server stopped.")
            sys.exit(0)


if __name__ == "__main__":
    main()
