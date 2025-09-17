#!/usr/bin/env python3
"""
Generic MCP Server for apple-notes-mcp
"""

import json
import logging
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class GenericMCPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "healthy", "server": "apple-notes-mcp"}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass  # Suppress default logging

if __name__ == "__main__":
    server = HTTPServer(('localhost', 9001), GenericMCPHandler)
    print(f"Starting apple-notes-mcp on port 9001")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"Shutting down apple-notes-mcp")
        server.shutdown()
