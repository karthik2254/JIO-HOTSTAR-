import os
import re

FETCH_FILE = "fetch.txt"
M3U_FILE = "channels.m3u"

if not os.path.exists(FETCH_FILE):
    raise FileNotFoundError("fetch.txt not found")

if not os.path.exists(M3U_FILE):
    raise FileNotFoundError("channels.m3u not found")

with open(FETCH_FILE, "r", encoding="utf-8") as f:
    new_token = f.read().strip()

if not new_token.startswith("__hdnea__="):
    raise ValueError("Invalid HDNEA token")

HDNEA_REGEX = r"__hdnea__=st=\d+~exp=\d+~acl=.*?~hmac=[a-f0-9]+"

updated_lines = []

with open(M3U_FILE, "r", encoding="utf-8") as f:
    for line in f:
        original = line.rstrip()

        # Replace old token anywhere in the line
        updated = re.sub(HDNEA_REGEX, new_token, original)

        # If URL line & no token present, append it
        if updated.startswith("http") and new_token not in updated:
            if "?" in updated:
                updated += f"&{new_token}"
            else:
                updated += f"?{new_token}"

        updated_lines.append(updated)

with open(M3U_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(updated_lines) + "\n")

print("HDNEA token updated everywhere successfully")
