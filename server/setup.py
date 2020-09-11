#!/usr/bin/python
#
# setup.py - standard Python build-and-package program

from setuptools import find_packages, setup


def read_requirements(filename):
    with open(filename) as f:
        return [req for req in (req.partition("#")[0].strip() for req in f) if req]


setup(
    name="flaskProject",
    python_requires='>3.6',
    version="0.1.0",
    description="Test project",
    author="Dmitry Maksymov",
    author_email="maksymov.d.a@gmail.com",
    packages=find_packages("."),
    install_requires=read_requirements('requirements.txt'),
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": [
           "test-api = testAPI.__main__:main"
        ]
    },
    scripts=["testAPI/stories/task_1.py"]
)
