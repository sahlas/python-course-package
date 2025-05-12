"""Generate a project using cookiecutter and initialize a git repository."""

import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

from tests.consts import PROJECT_DIR


def initialize_git_repo(repo_dir: Path):
    """Initialize a git repository in the given directory."""
    # git init
    subprocess.run(["git", "init"], cwd=repo_dir, check=True)
    # commit the contents to the 'main' branch
    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_dir, check=True)

    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "'feat: Initial commit by pytest'"], cwd=repo_dir, check=True)


def generate_project(template_values: Dict[str, str], test_session_id: str) -> Path:
    """Generate a project directory using cookiecutter."""
    _template_values: Dict[str, str] = deepcopy(template_values)
    cookiecutter_config = {"default_context": _template_values}
    cookiecutter_config_fpath = PROJECT_DIR / f"cookiecutter_test_config_{test_session_id}.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
        "--verbose",
    ]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)

    generated_repo_dir = PROJECT_DIR / "sample" / _template_values["repo_name"]
    return generated_repo_dir
