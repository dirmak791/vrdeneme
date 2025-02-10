import http.server
import ssl
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

handler = Handler
httpd = socketserver.TCPServer(("", PORT), handler)

print(f"Serving HTTPS on port {PORT}")
print("Visit https://localhost:8000 or https://[your-ip]:8000")

httpd.socket = ssl.wrap_socket(
    httpd.socket,
    server_side=True,
    certfile='cert.pem',
    keyfile='key.pem',
    ssl_version=ssl.PROTOCOL_TLS
)

httpd.serve_forever()
