from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filePath: str)->List[str]:
    '''
    this function will return the list of required packages and libraries
    '''
    requirements = []
    with open(filePath) as fileObj:
        requirements = fileObj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'mlproject',
    version = '0.01',
    author = 'sarang',
    author_email = 'sarangkulkarni1997@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
