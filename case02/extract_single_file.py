"""
CASE #2 – Extract a Single File from a ZIP Archive using IPWorks ZIP

This script demonstrates how to extract one specific file from an existing ZIP
archive without extracting the entire archive.

The target file is searched by filename only, even if it is stored inside an
unknown folder level within the ZIP archive.
"""

import os
from ipworkszip import Zip

RUNTIME_LICENSE = "315A544A415A30363237323633305745425452314131005344534242575952434E524A504B425800303030303030303000004353434D474A374B4D4447500000#IPWORKSZIP#EXPIRING_TRIAL#20260727"

ARCHIVE_PATH = "case02/input/sample_archive.zip"
OUTPUT_DIR = "case02/output"
TARGET_FILENAME = "invoice.txt"

os.makedirs(OUTPUT_DIR, exist_ok=True)

zip_component = Zip()
zip_component.set_runtime_license(RUNTIME_LICENSE)

zip_component.set_archive_file(ARCHIVE_PATH)
zip_component.set_extract_to_path(OUTPUT_DIR)
zip_component.set_overwrite_files(True)

print(f"Scanning archive: {ARCHIVE_PATH}")
print(f"Looking for file: {TARGET_FILENAME}")

zip_component.scan()

matches = []

for index in range(zip_component.get_file_count()):
    compressed_name = zip_component.get_file_compressed_name(index)

    if compressed_name.endswith("/"):
        continue

    if os.path.basename(compressed_name) == TARGET_FILENAME:
        matches.append((index, compressed_name))

if not matches:
    print(f"File not found: {TARGET_FILENAME}")

elif len(matches) > 1:
    print("Multiple files with the same name were found:")
    for _, compressed_name in matches:
        print(f"- {compressed_name}")
    print("Please specify the exact archive path before extracting.")

else:
    file_index, compressed_name = matches[0]
    output_path = os.path.join(OUTPUT_DIR, TARGET_FILENAME)

    print(f"Found file inside archive: {compressed_name}")
    print(f"Extracting only this file to: {output_path}")

    zip_component.set_file_decompressed_name(file_index, TARGET_FILENAME)
    zip_component.extract(compressed_name)

    print("Extraction completed successfully.")