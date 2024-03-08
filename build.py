from pathlib import Path
import subprocess

def main():
    root = Path.cwd()
    options = [
        "-F",
        "--distpath", f"{root / "dist"}",
        "--workpath", f"{root / "build"}",
        "--specpath", f"{root / "build"}",
        "--add-data", f"{root / "data"}:res",
    ]
    script = root / "src" / "rawaccel_profiles.py"
    subprocess.run(f"pyinstaller {" ".join(options)} {script}").check_returncode()

if __name__ == "__main__":
    main()
