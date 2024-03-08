from pathlib import Path, PurePath
from PIL import Image
from pystray import Icon, Menu, MenuItem

from profiles import Profile

profiles: set[Profile] = set()

PROFILES = Path("profiles")
def update_profiles():
    for path in PROFILES.iterdir():
        if path.is_file():
            profiles.add(Profile(path))

DATA = PurePath("data")
def load_data(filename: str):
    return Image.open(DATA / filename)

def create_menu():
    update_profiles()
    items = [MenuItem(p.text, p.action) for p in profiles]
    items.append(MenuItem("Quit", icon.stop))
    return Menu(*items)

def main():
    global icon
    icon = Icon("rawaccel_profiles", load_data("logo.png"), "Rawaccel Profiles", create_menu())
    icon.run()

if __name__ == "__main__":
    main()
