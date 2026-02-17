from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_header()
        response = {"message": "Hello from http.server API!"}
        self.wfile.write(json.dumps(response).encode())
        if __name__ == "__main__":
            server = HTTPServer(("localhost", 8000), SimpleHandler)
            print("Server running on http://localhost:8000")
            server.serve_forever()