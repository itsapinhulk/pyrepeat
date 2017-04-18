import os
import setuptools

curr_dir = os.path.dirname(os.path.abspath(__file__))

version = open(os.path.join(curr_dir, 'pyrepeat/VERSION'), 'r').read().strip()

description = 'Repeat command'
github_url = 'https://github.com/itsapinhulk/pyrepeat'
long_description = 'Python script which repeats command until stopped. See ' + github_url + '.'

setuptools.setup(
    name              = 'pyrepeat',
    version           = version,
    description       = description,
    long_description  = long_description,
    url               = github_url,
    license           = 'MIT',

    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Operating System :: POSIX :: Linux',
      'Topic :: System :: Shells',
      'Topic :: Utilities',
    ],
    keywords = 'console utility repeat',
    packages = [
      'pyrepeat',
    ],
    package_data = {
      'pyrepeat': ['VERSION'],
    },
    entry_points = {
      'console_scripts' : [
        'repeat=pyrepeat:main',
      ],
    },
)
