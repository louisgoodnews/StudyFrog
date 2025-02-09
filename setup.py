"""
Author: lodego
Date: 2025-02-08
"""

from setuptools import setup, find_packages


def main() -> None:
    """
    Sets up the packages for the StudyFrog application.

    This function is the entry point for the setup process. It is called when
    the user runs the setup.py script. It sets up the packages for the
    application, including the name, version, and packages.

    Returns:
        None
    """

    # Set up the packages
    setup(
        name="StudyFrog",
        version="0.1",
        packages=find_packages(),
    )


if __name__ == "__main__":
    main()
