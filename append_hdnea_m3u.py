import re

print("Reading token...")

# Read token
with open("fetch.txt", "r") as f:
    token = f.read().strip()

print("Token:", token)

# Read M3U
with open("channels.m3u", "r") as f:
    lines = f.readlines()

updated_lines = []

for line in lines:
    line = line.strip()

    if line.startswith("http"):
        # Remove old token
        line = re.sub(r'(\?|&)__hdnea__=[^&]*', '', line)

        # Clean trailing ? or &
        line = re.sub(r'[?&]$', '', line)

        # Add new token
        if "?" in line:
            line = line + "&" + token
        else:
            line = line + "?" + token

    updated_lines.append(line)

# Save file
with open("channels.m3u", "w") as f:
    f.write("\n".join(updated_lines))

print("Updated successfully!")
