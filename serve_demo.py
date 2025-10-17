#!/usr/bin/env python3
"""
Simple HTTP server to demonstrate compiled Webease files
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 5000

os.chdir('output')

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"🌐 Serving compiled Webease files at http://0.0.0.0:{PORT}")
    print(f"📁 Directory: {Path.cwd()}")
    print("\nAvailable files:")
    for file in Path('.').glob('*.html'):
        print(f"  - http://0.0.0.0:{PORT}/{file.name}")
    print("\n Press Ctrl+C to stop")
    httpd.serve_forever()
