"""
CASE #1 – TCP Client Demo

This script demonstrates the client side of the proposed solution.

The customer already has an asynchronous serial data stream available in a
Delphi application and wants to transmit each incoming line over the Internet
to another Delphi application running on a server with a dedicated static IP
address.

This example represents the sender application. It establishes a TCP
connection to the server, sends sample serial data line by line, waits for
the server acknowledgement after each transmission, and then closes the
connection.

For demonstration purposes, the loopback address (127.0.0.1) is used.
In a production environment, this value should be replaced with the
customer's dedicated static server IP address.
"""

import time
from ipworks import TCPClient

RUNTIME_LICENSE = "3150544A415A3036323632363330574542545231413100594F4D4D504F4E4E535457524253494D00303030303030303000005934524E424E4B46333353500000#IPWORKS#EXPIRING_TRIAL#20260726"

client = TCPClient()
client.set_runtime_license(RUNTIME_LICENSE)

client.remote_host = "127.0.0.1"
client.remote_port = 5000


def on_connected(e):
    print("Connected to TCP server.")


def on_data_in(e):
    response = e.text.decode("utf-8", errors="replace")
    print(f"Server response: {response}")


def on_disconnected(e):
    print("Disconnected from TCP server.")


def on_error(e):
    print(f"Error {e.error_code}: {e.description}")


client.on_connected = on_connected
client.on_data_in = on_data_in
client.on_disconnected = on_disconnected
client.on_error = on_error

client.connect()

for _ in range(20):
    client.do_events()
    time.sleep(0.05)

serial_stream = [
    "COM1 | LINE 001 | VALUE=125",
    "COM1 | LINE 002 | VALUE=127",
    "COM1 | LINE 003 | VALUE=130"
]

for line in serial_stream:
    print(f"Sending serial line: {line}")

    client.send_text(line)

    for _ in range(20):
        client.do_events()
        time.sleep(0.05)

client.disconnect()