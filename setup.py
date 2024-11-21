from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("-e")]

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Omer',
    author_email='khanomer679@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)