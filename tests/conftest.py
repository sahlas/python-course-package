import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent
TESTS_DIR_PARTENT = (THIS_DIR / "../").resolve()
PYTHONPATH = str(TESTS_DIR_PARTENT)
sys.path.insert(0, PYTHONPATH)