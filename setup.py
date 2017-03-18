import os
import setuptools

curr_dir = os.path.dirname(os.path.abspath(__file__))

version = open(os.path.join(curr_dir, 'VERSION'), 'r').read().strip()

description = 'Python repeat command'
github_url = 'https://github.com/itsapinhulk/pyrepeat'
long_description = description + '. See ' + github_url + '.'

setuptools.setup(
    name    = 'pyrepeat',
    version = version,
    description = description,
    long_description  = long_description,
    url = github_url,
    license = 'MIT',
    classifiers = [
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Topic :: Utilities',
    ],
    keywords = 'console utility',
    packages='repeat',
    entry_points = {
      'console_scripts' : [
        'repeat=repeat:_main',
      ],
    },
)
