# main script, named like this for the executable name
# try to only concern with the most high-level tasks

from dataclasses import dataclass, field

from pystray import Icon, Menu, MenuItem

from gui import GUI
from profiles import ProfileManager

from utils import load_data

@dataclass # fed up with python global variable declarations, made a dataclass (naturally)
class Main:
    pm: ProfileManager = field(default_factory=ProfileManager)
    gui: GUI = field(default=None, init=False)
    show_gui: bool = False

    def run(self):
        self.icon = Icon("rawaccel_profiles", load_data("logo.png"), "RawAccel Profiles", self.create_menu())
        self.icon.run(self.setup)

    def setup(self, _):
        self.icon.visible = True

        # have to create gui in the same thread as mainloop
        self.gui = GUI(self.pm)
        self.gui.protocol("WM_DELETE_WINDOW", self.delete_window)
        self.gui.start()

    def delete_window(self):
        self.toggle_gui()
        self.refresh()

    def create_menu(self):
        self.pm.update()
        items = [MenuItem(p.text, p.action) for p in self.pm.profiles]
        items.append(Menu.SEPARATOR)
        items.append(MenuItem("Refresh", self.refresh))
        items.append(MenuItem("GUI", self.toggle_gui, lambda _: self.show_gui))
        items.append(MenuItem("Quit", self.quit))
        return Menu(*items)

    def refresh(self):
        self.icon.menu = self.create_menu()

    def toggle_gui(self):
        self.show_gui ^= True
        if self.show_gui:
            self.gui.deiconify()
        else:
            self.gui.withdraw()

    def quit(self):
        if self.gui:
            self.gui.stop()
        self.icon.stop()

def main():
    Main().run()

if __name__ == "__main__":
    main() # this is just so pyinstaller has an entry point to work with, don't run this file
