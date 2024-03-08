from pathlib import Path
from PIL import Image

INTERNAL = Path("_internal")

def load_data(filename: str):
    return Image.open(INTERNAL / "data" / filename)
