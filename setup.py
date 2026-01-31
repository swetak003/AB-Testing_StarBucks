from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """ 
    This function will return the list of requirements 
    mentioned in the requirements.txt file 
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    return requirements



setup( name='project_STarbucks',
    version='1.0.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Sweta KUmari',
    attrs={'license': 'MIT'},
    description='A/B Testing Project for Starbucks'
)    