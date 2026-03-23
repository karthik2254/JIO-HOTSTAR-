import re

# Read token
with open("fetch.txt", "r") as f:
    token = f.read().strip()

# Read existing playlist
with open("channels.m3u", "r", encoding="utf-8") as f:
    content = f.read()

# Replace old token or append if missing
def update_url(match):
    url = match.group(0)

    # Remove old token if exists
    url = re.sub(r'__hdnea__=[^&]*', '', url)

    # Clean trailing symbols
    if url.endswith('?') or url.endswith('&'):
        url = url[:-1]

    # Add new token
    if '?' in url:
        url = url + '&' + token
    else:
        url = url + '?' + token

    return url

# Apply only on URLs (http/https lines)
updated_content = re.sub(r'https?://[^\s]+', update_url, content)

# Save updated playlist
with open("channels.m3u", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("✅ channels.m3u updated successfully!")
