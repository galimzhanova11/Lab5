import re

text="abbbaaaa"
for line in text:
    if re.search('^a(b*)$',text):
        print(line)