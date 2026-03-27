import re

# Read token
with open("fetch.txt", "r") as f:
    token = f.read().strip()

# Read channels
with open("channels.m3u", "r") as f:
    data = f.read()

# Replace old token or append new
data = re.sub(r'__hdnea__=[^&"\n]*', token, data)

# Save updated file
with open("channels.m3u", "w") as f:
    f.write(data)

print("Updated channels.m3u successfully")
