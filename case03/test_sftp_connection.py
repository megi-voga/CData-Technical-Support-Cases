from ipworksssh import SFTPClient

RUNTIME_LICENSE = "3148544A415A30363237323633305745425452314131004C45415143464545584245544D574A4200303030303030303000004A4A4130444D31334D5054380000#IPWORKSSSH#EXPIRING_TRIAL#20260727"

client = SFTPClient()
client.set_runtime_license(RUNTIME_LICENSE)


def on_ssh_server_authentication(e):
    print("\n=== SSH Server Authentication ===")
    print("Fingerprint:", e.fingerprint)

    e.accept = True

    print("Host key accepted for testing.\n")


client.on_ssh_server_authentication = on_ssh_server_authentication

client.set_ssh_user("demo")
client.set_ssh_password("password")

print("Connecting...")

try:
    client.ssh_logon("test.rebex.net", 22)
    print("Connected successfully!")

    client.ssh_logoff()
    print("Disconnected.")

except Exception as ex:
    print(ex)