import logging
import sys
from pathlib import Path


file_path: Path = Path(__file__)
src_path: Path = Path(file_path.parent.parent, "src")
src_dir = str(src_path)
sys.path.insert(0, src_dir)

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
