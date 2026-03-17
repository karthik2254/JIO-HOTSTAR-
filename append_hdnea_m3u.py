import re

print("Reading token...")

# Load token
with open("fetch.txt", "r") as f:
    token = f.read().strip()

if not token.startswith("__hdnea__="):
    print("Invalid token format")
    exit(1)

print("Token:", token)

# Load M3U
with open("channels.m3u", "r", encoding="utf-8") as f:
    content = f.read()

# Replace all tokens
updated = re.sub(r"__hdnea__=[^&\s]+", token, content)

# Save file
with open("channels.m3u", "w", encoding="utf-8") as f:
    f.write(updated)

print("✅ channels.m3u updated successfully")
