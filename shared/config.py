"""Central paths for the Astronomie project. Change BASE only if the drive letter changes."""
from pathlib import Path

BASE = Path(r"H:\Astronomie")

RAW = BASE / "data" / "raw"
PROCESSED = BASE / "data" / "processed"
PROJECTS = BASE / "projects"


def project_dir(name: str) -> Path:
    """Return the folder of a project and create its standard subfolders."""
    p = PROJECTS / name
    (p / "notebooks").mkdir(parents=True, exist_ok=True)
    (p / "figures").mkdir(parents=True, exist_ok=True)
    return p


if not BASE.exists():
    raise FileNotFoundError(
        f"{BASE} not found. Is the USB drive connected, and is the drive letter still H:?"
    )

RAW.mkdir(parents=True, exist_ok=True)
PROCESSED.mkdir(parents=True, exist_ok=True)
