
from setuptools import setup, find_packages
  
# reading long description from file 
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

  
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers', 
    'Topic :: Scientific/Engineering :: Mathematics', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    ] 
  
# calling the setup function  
setup(name='robustbase', 
      version='0.2.3', 
      description='A Python Based Library to Calculate Estimators (Sn, Qn, MAD, IQR)', 
      long_description=long_description, 
      long_description_content_type='text/markdown',
      url='https://github.com/deepak7376/robustbase', 
      author='Deepak Yadav', 
      author_email='dky.united@gmail.com', 
      license='MIT', 
      py_modules=["robustbase"],
      package_dir={'':'src'},
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  
      keywords='Sn Qn MAD IQR',
      python_requires='>=3'

      ) 
