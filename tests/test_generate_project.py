import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict
import shutil


import pytest
from tests.utils.project import generate_project

@pytest.fixture(scope="session")
def project_dir() -> Path: # type: ignore
    template_values = {"repo_name": "test-repo"}
    generate_repo_dir: Path = generate_project(template_values=template_values)
    yield generate_repo_dir # provides the fixture value to the test
    # teardown code
    # remove the generated project
    shutil.rmtree(generate_repo_dir, ignore_errors=False)



def test_can_generate_project(project_dir):
    """
    Test the generate_project function.

    execute: `cookiecutter <template_path> ...`
    """

    assert project_dir.exists(), f"Project directory {project_dir} does not exist."
