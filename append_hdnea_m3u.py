import re

# Read token
with open("fetch.txt", "r") as f:
    token_line = f.read().strip()

token = token_line.replace("__hdnea__=", "")

# Read M3U file
with open("channels.m3u", "r") as f:
    content = f.read()

# Replace old token
content = re.sub(r"__hdnea__=[^&\s]+", "__hdnea__=" + token, content)

# Save file
with open("channels.m3u", "w") as f:
    f.write(content)

print("M3U file updated")
