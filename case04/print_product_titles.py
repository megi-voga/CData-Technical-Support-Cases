import json
from ipworks import HTTP

RUNTIME_LICENSE = "3150544A415A30363237323633305745425452314131004D485553464E49454354444742544659003030303030303030000032593550473742594A3732460000#IPWORKS#EXPIRING_TRIAL#20260727"
URL = "https://dummyjson.com/products"

http = HTTP()
http.set_runtime_license(RUNTIME_LICENSE)

response_parts = []


def on_transfer(e):
    response_parts.append(e.text.decode("utf-8", errors="replace"))


http.on_transfer = on_transfer

print(f"Requesting data from: {URL}")

http.get(URL)

response_text = "".join(response_parts)
data = json.loads(response_text)

print("\nProduct Titles:")

for product in data["products"]:
    print(f"- {product['title']}")