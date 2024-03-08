# GUI script, needs to be separate so we can just star import tkinter stuff without polluting the namespace

from tkinter import *
from tkinter.ttk import *

from profiles import ProfileManager

PADDING = (16, 16)

class GUI(Tk):
    def __init__(self, pm: ProfileManager):
        super().__init__()
        self.pm = pm

        self.title("RawAccel Profiles maker")
        self.resizable(True, True)

        # Create
        create = LabelFrame(self, text="Create", padding=PADDING)

        create_button = Button(create, command=self.profile_create, text="Create profile")
        create_button.grid(row=0, column=0)

        self.entry_text = StringVar()
        self.entry = Entry(create, textvariable=self.entry_text)
        self.entry.grid(row=1, column=0)

        create.grid(row=0, column=0)

        # Delete
        delete = LabelFrame(self, text="Delete", padding=PADDING)

        delete_button = Button(delete, command=self.profile_delete, text="Delete profile")
        delete_button.grid(row=0, column=0)

        self.profiles = Combobox(delete, postcommand=self.update_combobox_values)
        self.profiles.grid(row=1, column=0)

        delete.grid(row=1, column=0)

        # Size Grip
        sizegrip = Sizegrip(self)
        sizegrip.place(anchor=SE, relx=1, rely=1)

    def start(self):
        self.withdraw()
        try:
            self.mainloop()
        except TclError as e:
            self.destroy()
            print(e)
            return

    def stop(self):
        self.deiconify()
        try:
            self.quit()
        except TclError as e:
            print(e)
            return

    def update_combobox_values(self):
        self.profiles["values"] = [str()] + [p.text for p in self.pm.profiles]

    def profile_create(self):
        if text := self.entry_text.get():
            self.entry_text.set(str())
            self.pm.create(text)

    def profile_delete(self):
        values = list(self.profiles["values"])
        if values[index := self.profiles.current()]:
            self.pm.delete(values.pop(index))
            self.profiles.set(str())
            self.profiles["values"] = values
