from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    :param file_path:
    :return:
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] #requirement.txt file, requirements given there is new line which needs to be replace to blank
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Naseer Ahmed',
    author_email='nshaiman@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)