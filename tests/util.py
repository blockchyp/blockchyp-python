import os
import shutil
import tempfile


def _tempdir(func):
    try:
        tempdir = tempfile.mkdtemp("blockchyp-test")
        func(tempdir + os.sep)
    finally:
        shutil.rmtree(tempdir)
