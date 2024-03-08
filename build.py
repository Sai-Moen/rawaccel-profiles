from pathlib import Path

import PyInstaller.__main__ as pyi

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
    pyi.run((script, *options))

if __name__ == "__main__":
    freeze()
