
from setuptools import setup, find_packages
  
# reading long description from file 
with open('README.rst') as file: 
    long_description = file.read() 
  
  
# specify requirements of your package here 
REQUIREMENTS = [
'certifi==2019.11.28',
'docutils==0.15.2',
'numpy==1.18.0',
'statistics==1.0.3.5'

] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers', 
    'Topic :: Scientific/Engineering :: Mathematics', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    ] 
  
# calling the setup function  
setup(name='robustbase', 
      version='2.1', 
      description='A Python Based Library to Calculate Estimators (Sn, Qn, MAD, IQR)', 
      long_description=long_description, 
      url='https://github.com/deepak7376/robustbase', 
      author='Deepak Yadav', 
      author_email='dky.united@gmail.com', 
      license='MIT', 
      packages=find_packages(), 
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='Sn Qn MAD IQR',
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3'

      ) 


