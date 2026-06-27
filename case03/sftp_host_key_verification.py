"""
CASE #3 – SFTP Host Key Verification using IPWorks SSH

This example demonstrates how to handle SSH server host key verification
using the IPWorks SSH SFTPClient component.

The customer reported the following error:

    "Server's host key has been rejected by user"

For testing purposes, the server host key can be accepted inside the
SSHServerAuthentication event. However, for production environments, the
recommended approach is to verify the server fingerprint against a trusted
fingerprint before accepting the connection.
"""

from ipworksssh import SFTPClient

RUNTIME_LICENSE = "YOUR_RUNTIME_LICENSE"

client = SFTPClient()
client.set_runtime_license(RUNTIME_LICENSE)


def on_ssh_server_authentication(e):
    """
    Handles server host key verification.

    For demonstration purposes, every host key is accepted.
    In production, compare e.fingerprint with the expected
    server fingerprint before setting e.accept = True.
    """

    print("SSH server authentication event triggered.")
    print(f"Server fingerprint: {e.fingerprint}")

    # Accept the host key (testing only)
    e.accept = True

    print("Server host key accepted.")


client.on_ssh_server_authentication = on_ssh_server_authentication

print("SFTPClient configured successfully.")
print("Host key verification is handled through the SSHServerAuthentication event.")
print("For production use, always validate the server fingerprint before accepting it.")