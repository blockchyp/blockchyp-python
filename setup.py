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

setup(
    version=os.environ.get("VERSION", "0.1.0"),
    long_description=readme(),
    cmdclass={
        "test": Unsupported,
    },
)
