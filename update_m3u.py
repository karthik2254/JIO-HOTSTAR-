# update_m3u.py

# Read token
with open("fetch.txt", "r") as f:
    token = f.read().strip()

# Read M3U
with open("channels.m3u", "r") as f:
    content = f.read()

# Replace OLD token line (simple logic)
import re

updated = re.sub(r"hdntl=.*?(?=\s|$)", token, content)

# Save file
with open("channels.m3u", "w") as f:
    f.write(updated)

print("✅ M3U updated successfully")
