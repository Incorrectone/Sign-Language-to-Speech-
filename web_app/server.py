import http.server
import socketserver
import os

# Define the port you want the server to run on.
# 8080 is a common choice for local development.
PORT = 8080

# Get the directory where the script is located.
# The server will serve files from this directory.
web_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(web_dir)

# This is the handler that processes incoming requests.
# SimpleHTTPRequestHandler is a basic handler that serves files from the current directory.
Handler = http.server.SimpleHTTPRequestHandler

# This sets up the TCP server, binding it to all network interfaces ('') on the specified port.
# Using a 'with' statement ensures the server is properly closed when the script stops.
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"You can view your page at http://localhost:{PORT}")
    
    # This starts the server and makes it listen for requests indefinitely.
    # To stop the server, press Ctrl+C in the terminal.
    httpd.serve_forever()