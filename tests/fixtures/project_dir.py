"""Generate a project using cookiecutter and initialize a git repository."""

import shutil
import subprocess
from pathlib import Path
from uuid import uuid4

import pytest
from click import echo

# pylint: disable=no-name-in-module
from tests.utils.generate_project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Path:  # type: ignore
    """
    Fixture to create a temporary project directory for testing.

    This fixture generates a unique project directory for each test session.
    """
    test_session_id: str = generate_test_session_id()
    template_values = {
        "repo_name": f"test-repo-{test_session_id}",
        "package_import_name": f"test_package_{test_session_id}",
    }
    generate_repo_dir: Path = generate_project(template_values=template_values, test_session_id=test_session_id)
    try:
        initialize_git_repo(generate_repo_dir)
        subprocess.run(["make", "lint-ci"], cwd=generate_repo_dir, check=False)
        yield generate_repo_dir  # provides the fixture value to the test
    finally:
        # teardown code
        # remove the generated project
        echo(f"Removing the generated project directory: {generate_repo_dir}")
        shutil.rmtree(generate_repo_dir)


def generate_test_session_id() -> str:
    """
    Generate a unique test session ID.

    Returns
    -------
        str: A unique test session ID.

    Example:
        >>> generate_test_session_id()
        'abc123'

    """
    test_session_id = str(uuid4())[:6]
    return test_session_id
