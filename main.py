import requests
from pathlib import Path

link = input("enter steam link: ")

s = requests.get(link).text

l = s.find('>', s.find('id="appHubAppName"')+7) + 1
r = s.find('<', l)


title = s[l:r]

l = link.find('app')+4
r = link.find('/', l)
if r == -1:
    r = len(link)
s_id = link[l:r]

print(f"title: '{title}'")
print(f"id: '{s_id}'")
exit()

with open(Path.home() / f'Desktop/{title}.desktop', 'w') as f:
    f.write(f"""[Desktop Entry]
Name={title}
Comment=Play this game on Steam
Exec=steam steam://rungameid/{s_id}
Icon=steam_icon_{s_id}
Terminal=false
Type=Application
Categories=Game;""")

import os
os.system(f'gio set "$HOME/Desktop/{title}.desktop" metadata::trusted true')
os.system(f'chmod +x "$HOME/Desktop/{title}.desktop"')
