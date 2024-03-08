# profile.py shadows stdlib lol

from dataclasses import dataclass
from pathlib import Path

@dataclass
class Profile:
    name: Path

    @property
    def text(self) -> str:
        return self.name.stem

    def action(self):
        pass
