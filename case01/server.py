"""
CASE #1 – TCP Server Demo

Customer scenario:
The customer has an asynchronous serial data stream in one location.
They want to send each line of that stream over the internet from one Delphi
application to another Delphi application running on a server.

Recommended solution:
Use IPWorks TCPClient on the sending side and IPWorks TCPServer on the server side.

This file represents the server-side application.
It listens on a fixed TCP port, accepts incoming client connections, receives
each line/message, prints it, and sends back an acknowledgement.
"""

import time
from ipworks import TCPServer

RUNTIME_LICENSE = "3150544A415A3036323632363330574542545231413100594F4D4D504F4E4E535457524253494D00303030303030303000005934524E424E4B46333353500000#IPWORKS#EXPIRING_TRIAL#20260726"

server = TCPServer()
server.set_runtime_license(RUNTIME_LICENSE)
server.local_port = 5000


def on_connection_request(e):
    e.accept = True


def on_connected(e):
    print(f"Client connected (ID: {e.connection_id})")


def on_data_in(e):
    message = e.text.decode("utf-8", errors="replace")
    print(f"Received: {message}")
    server.send_text(e.connection_id, f"ACK: {message}")


def on_disconnected(e):
    print("Client disconnected")


def on_error(e):
    print(f"Error {e.error_code}: {e.description}")


server.on_connection_request = on_connection_request
server.on_connected = on_connected
server.on_data_in = on_data_in
server.on_disconnected = on_disconnected
server.on_error = on_error

server.start_listening()
print("Server listening on port 5000...")

try:
    while True:
        server.do_events()
        time.sleep(0.01)
except KeyboardInterrupt:
    server.shutdown()