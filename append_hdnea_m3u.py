import re

# Read token
with open("fetch.txt", "r") as f:
    token_line = f.read().strip()

token = token_line.replace("__hdnea__=", "")

# Read M3U
with open("channels.m3u", "r") as f:
    content = f.read()

# Replace old token or append if missing
def replace_token(url):
    if "__hdnea__=" in url:
        return re.sub(r'__hdnea__=[^&"\']+', f'__hdnea__={token}', url)
    else:
        if "?" in url:
            return url + f"&__hdnea__={token}"
        else:
            return url + f"?__hdnea__={token}"

# Process all URLs
lines = content.splitlines()
new_lines = []

for line in lines:
    if line.startswith("http"):
        new_lines.append(replace_token(line))
    else:
        new_lines.append(line)

# Save updated M3U
with open("channels.m3u", "w") as f:
    f.write("\n".join(new_lines))

print("✅ M3U updated successfully")
