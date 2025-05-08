## BUILD' MY ENTIRE ML PROJECT AS A PACKAGE
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'



def get_requirements(file_path:str)->List[str]:
    '''
    this will return the list of required libraries
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements    

setup(
    name="mlproject",
    version="0.0.1",
    author="Raghu Vamsi",
    author_email="raghuvamsibolem@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)