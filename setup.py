import io
import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

def readme():
    with io.open("README.md", encoding="utf-8") as f:
        return f.read()

class Unsupported(TestCommand):
    def run(self):
        sys.stderr.write("Running 'test' with setup.py is not supported. "
                         "Use 'pytest' or 'tox' to run the tests.\n")
        sys.exit(1)

def _find_git():
    root = os.path.abspath(os.sep)

    parent = "."

    while os.path.abspath(parent) != root:
        if os.path.isdir(os.path.join(parent, ".git")):
            return parent

        parent = os.path.join(parent, "..")

    # TODO solve this clusterfuck
    return os.path.join(os.getenv("HOME"), "github.com/blockchyp/sdk-generator")

setup(
    use_scm_version={"root": _find_git(), "relative_to": __file__},
    long_description=readme(),
    cmdclass={
        "test": Unsupported,
    },
)
