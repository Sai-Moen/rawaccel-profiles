from pathlib import Path

import PyInstaller.__main__ as pyi

PRODUCTION = True

def freeze():
    root = Path.cwd()
    script = f"{root / "src" / "rawaccel_profiles.py"}"
    options = [
        "-y",
        "--paths",    f"{root / "src"}",
        "--add-data", f"{root / "data"}:data",
        "--distpath", f"{root / "dist"}",
        "--workpath", f"{root / "build"}",
        "--specpath", f"{root / "build"}",
    ]
    if PRODUCTION:
        options.append("--noconsole")
    pyi.run((script, *options))

if __name__ == "__main__":
    freeze()
