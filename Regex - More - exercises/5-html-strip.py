import re

text = input()

pattern_title = r"(<title>(?P<title>[a-zA-Z0-9\s]+)+</title>)"
pattern_remove = r"<[^>]*>"
pattern_ready = r"\\n"

title = re.findall(pattern_title, text)

new_title = ""
for i in title:
    new_title = i[1]

text = re.sub(pattern_title, "", text)
text = re.sub(pattern_remove, "", text)
text = re.sub(pattern_ready, "", text)

print(f"Title: {new_title}")
print(f"Content: {text}")
