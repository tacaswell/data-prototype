from os import path
from setuptools import setup, find_packages
import sys


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 9)
if sys.version_info < min_version:
    error = """
data_prototype does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*(sys.version_info[:2] + min_version))
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='data_prototype',
    description="Experimental code for the upcoming Matplotlib data refactor.",
    long_description=readme,
    author="Thomas A Caswell",
    author_email='tacaswell@gmail.com',
    url='https://github.com/tacaswell/data_prototype',
    python_requires='>={}'.format('.'.join(str(n) for n in min_version)),
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            # 'command = some.module:some_function',
        ],
    },
    setup_requires=[
        "setuptools_scm>=6.2",
        "setuptools_scm_git_archive",
        "setuptools>=45",
    ],
    use_scm_version={
        "version_scheme": "release-branch-semver",
        "local_scheme": "node-and-date",
        "write_to": "data_prototype/_version.py",
        "fallback_version": "0.0+UNKNOWN",
    },
    include_package_data=True,
    package_data={
        'data_prototype': [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
        ]
    },
    install_requires=requirements,
    license="BSD (3-clause)",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
