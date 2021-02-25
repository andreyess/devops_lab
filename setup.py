from setuptools import setup, find_packages

setup(
    name="mypylogger",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshooter.logger:snapshoot",
        ],
    },
    install_requires=[
        "psutil"
    ],
    version="1.0",
    author="Andrei Karpyza",
    author_email="Andrei_Karpyza@epam.com",
    description="This is a package with main purpose - to make system-state snapshots.",
    license="MIT",
)
