import pytest

@pytest.fixture(scope="session")
def project():
    print("SETUP")
    yield "foo"
    print("TEARDOWN")


def test_linting_passes(project):
    print(project)
    assert False

def test_tests_pass(project):
    ...

def test_install_succeeds(project):
    ...


"""
Setup:
1. generate a project using cookiecutter
2. create a virtual environment and install the project dependencies

Tests:
3. run the tests
4. run the linting

Cleanup/Teardown:
5. remove the generated project
6. remove the virtual environment
# Note: The above code is a placeholder and should be replaced with actual test cases.
"""