import re

print("Reading token...")

# Read token
with open("fetch.txt", "r") as f:
    token = f.read().strip()

print("Token:", token)

# Read M3U file
with open("channels.m3u", "r") as f:
    lines = f.readlines()

updated_lines = []

for line in lines:
    line = line.strip()

    # If it's a URL line
    if line.startswith("http"):
        # Remove old token
        line = re.sub(r'__hdnea__=[^&]*', '', line)

        # Add new token
        if "?" in line:
            line = line + "&" + token
        else:
            line = line + "?" + token

    updated_lines.append(line)

# Write updated file
with open("channels.m3u", "w") as f:
    f.write("\n".join(updated_lines))

print("channels.m3u updated successfully!")
