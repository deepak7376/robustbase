from setuptools import setup, find_packages
import subprocess
import os

# Get the version from git tags
version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in version:
    v, i, s = version.split("-")
    version = v + "+" + i + ".git." + s

assert "-" not in version
assert "." in version

# Write the version to a file
with open("VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % version)

# Read the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# Setup function
setup(
    name='robustbase', 
    version=version, 
    description='A Python Based Library to Calculate Estimators (Sn, Qn, MAD, IQR)', 
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://github.com/deepak7376/robustbase', 
    author='Deepak Yadav', 
    author_email='dky.united@gmail.com', 
    license='MIT', 
    packages=find_packages(),  # Automatically find packages
    include_package_data=True,
    project_urls={
        'Source': 'https://github.com/deepak7376/robustbase',
        'Tracker': 'https://github.com/deepak7376/robustbase/issues',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='robust statistics robustness Sn Qn MAD IQR',
    python_requires='>=3.0',
    install_requires=[
        'certifi>=2019.11.28',
        'docutils>=0.15.2',
        'numpy>=1.18.0',
        'statistics>=1.0.3.5',
    ],
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov>=2.10.0',
            'coverage>=5.0',
            'flake8>=3.8.0',
        ],
    },
)
