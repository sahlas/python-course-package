import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict
import shutil


from tests.consts import THIS_DIR, PROJECT_DIR 

def generate_project(template_values: Dict[str, str]):
    _template_values: Dict[str, str] = deepcopy(template_values)
    cookiecutter_config = {"default_context": _template_values}
    cookiecutter_config_fpath = THIS_DIR / "cookiecutter_test_config.json"
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