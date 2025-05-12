import sys

from consts import (
    PROJECT_DIR,
    THIS_DIR,
)

PYTHONPATH = str(PROJECT_DIR)


# Add the parent directory to the Python path
sys.path.insert(0, str(PYTHONPATH))
sys.path.insert(0, str(THIS_DIR))
sys.path.insert(0, str(THIS_DIR / "utils"))
sys.path.insert(0, str(THIS_DIR / "fixtures"))
sys.path.insert(0, str(THIS_DIR / "consts"))

pytest_plugins = [
    "tests.fixtures.project_dir",
    # "tests.fixtures.project_dir_with_config",
    # "tests.fixtures.project_dir_with_config_and_hooks",
    # "tests.fixtures.project_dir_with_config_and_hooks_and_pre_commit",
]
