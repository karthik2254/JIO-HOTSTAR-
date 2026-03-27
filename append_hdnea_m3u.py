import re

# Read token
with open("fetch.txt") as f:
    token = f.read().strip()

# Read cookie
try:
    with open("cookie.txt") as f:
        cookie = f.read().strip()
except:
    cookie = ""

# Read M3U
with open("channels.m3u", "r") as f:
    data = f.read()

# Replace old token
data = re.sub(r'__hdnea__=[^"& ]+', token, data)

# Add cookie if exists
if cookie:
    data = re.sub(r'#EXTINF:-1', f'#EXTINF:-1\n#EXTVLCOPT:http-cookie={cookie}', data)

# Save back
with open("channels.m3u", "w") as f:
    f.write(data)

print("✅ M3U Updated with Token & Cookie")
