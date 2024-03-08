# rawaccel-profiles

Allows you to easily save and load profiles for RawAccel (Windows 10+ 64-bit).

## Installation

1. Download the .zip from the releases page.
2. Extract the `rawaccel_profiles` folder.
3. Place the `rawaccel_profiles` folder inside the RawAccel folder (where you installed it).

Now it should be good to go.
You should now have an executable named `rawaccel_profiles.exe` placed something like the following path.

`RawAccel/rawaccel_profiles/rawaccel_profiles.exe`

Where RawAccel represents your RawAccel installation folder.

## Usage

When the executable is run, you will get a small icon in the system tray, which is the RawAccel logo.
Upon right-clicking it, you will see multiple options:

First, a list of profiles (can be 0 to many profiles).
This list is based on the `profiles` folder which the program will make inside the RawAccel folder if necessary.
Inside this folder, new profiles can be created (and deleted) by the program.

Then, a separator, and lastly 3 permanent buttons:

1. Refresh - for refreshing the system tray list of profiles
2. GUI - to toggle the profile creation/deletion Graphical User Interface
3. Quit - to exit the program entirely

If you create a profile, that profile will be a copy of `settings.json`.
By applying certain settings in the RawAccel grapher (RawAccel.exe), you can update `settings.json`.

### Note on the RawAccel grapher

As of now, the grapher will not know that the settings changed when you apply,
so you have to reopen it if you want to see the changes.

In the future, there may come an extra permanent button to restart the grapher.

## Build From Source

Should you want to build the program from the source code (not necessary for normal usage),
then you will need python, 3.12+ is recommended, but 3.9+ is likely to work as well.

Run the following from the root directory once (in a .venv if you wish):
`pip install -r requirements.txt`

Then, to actually build:
`python build.py`

This build script uses pyinstaller to make the executable.
