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

def _find_scm_version():
    root = os.path.abspath(os.sep)

    parent = "."

    while os.path.abspath(parent) != root:
        if os.path.isdir(os.path.join(parent, ".git")):
            return {"root": parent, "relative_to": __file__}

        parent = os.path.join(parent, "..")

    return None

scm_version = _find_scm_version()
version = None
if not scm_version:
    version = "0.1.0"

setup(
    version=version,
    use_scm_version=_find_scm_version(),
    long_description=readme(),
    cmdclass={
        "test": Unsupported,
    },
)
