"""Generate a project using cookiecutter and initialize a git repository."""

from pathlib import Path


def test_can_generate_project(project_dir: Path):
    """
    Test the generate_project function.

    execute: `cookiecutter <template_path> ...`
    """
    assert project_dir.exists()
