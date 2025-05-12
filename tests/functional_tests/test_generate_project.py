


def test_can_generate_project(project_dir):
    """
    Test the generate_project function.

    execute: `cookiecutter <template_path> ...`
    """

    assert project_dir.exists(), f"Project directory {project_dir} does not exist."
