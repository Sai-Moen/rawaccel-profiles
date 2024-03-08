# profile.py shadows stdlib lol

from dataclasses import dataclass, field
from pathlib import Path
import subprocess

def get_ra_dir() -> Path:
    return Path.cwd().parent

def get_profiles_dir() -> Path:
    d = get_ra_dir() / "profiles"
    if not d.exists():
        d.mkdir()
    return d

@dataclass
class Profile:
    name: Path

    @property
    def text(self) -> str:
        return self.name.stem

    def action(self):
        writer = get_ra_dir() / "writer.exe"
        if writer.exists():
            subprocess.run(f"{writer} {self.name}")

@dataclass
class ProfileManager:
    _profiles: list[Profile] = field(default_factory=list)

    @property
    def profiles(self) -> list[Profile]:
        return self._profiles.copy()

    def update(self):
        self._profiles = self.sorted_profile_list()

    def sorted_profile_list(self) -> list[Profile]:
        d = get_profiles_dir()
        paths = {path for path in d.iterdir() if path.is_file()}
        return [Profile(p) for p in sorted(paths)]

    def create(self, stem: str):
        settings = get_ra_dir() / "settings.json"
        if not settings.exists():
            return

        path = get_profiles_dir() / stem
        path.with_suffix(".json").write_text(settings.read_text())
        self.update()

    def delete(self, stem: str):
        path = get_profiles_dir() / stem
        path.with_suffix(".json").unlink()
        self.update()
