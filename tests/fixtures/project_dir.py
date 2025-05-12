import json
import shutil
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from typing import Dict
from uuid import uuid4

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Path:  # type: ignore
    test_session_id: str = generate_test_session_id()
    template_values = {"repo_name": f"test-repo-{test_session_id}"}
    generate_repo_dir: Path = generate_project(template_values=template_values, test_session_id=test_session_id)
    try:
        initialize_git_repo(generate_repo_dir)
        subprocess.run(["make", "lint-ci"], cwd=generate_repo_dir, check=False)
        yield generate_repo_dir  # provides the fixture value to the test
    finally:
        # teardown code
        # remove the generated project
        shutil.rmtree(generate_repo_dir, ignore_errors=False)

def generate_test_session_id() -> str:
    """
    Generate a unique test session ID.

    Returns:
        str: A unique test session ID.
    """
    test_session_id = str(uuid4())[:6]
    return test_session_id