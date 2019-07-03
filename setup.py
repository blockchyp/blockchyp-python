from setuptools import find_packages, setup

def requirements():
    with open('requirements.txt') as requirements:
        return [
            str(line.strip())
            for line in requirements.readlines()
            if line.strip() and not line.startswith(('#', '-'))
        ]

setup(
    name="blockchyp",
    version="0.1.0",
    license="MIT License",
    description=(
        "This is the recommended means for Python developers to access the BlockChyp gateway and "
        "BlockChyp terminals."
    ),
    long_description="",
    author="BlockChyp",
    author_email="support@blockchyp.com",
    url="https://github.com/blockchyp/blockchyp-python",
    keywords="blockchyp",
    # install_requires=requirements(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    packages=find_packages(),
    include_package_data=True,
)