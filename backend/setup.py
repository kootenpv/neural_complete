from setuptools import find_packages
from setuptools import setup

MAJOR_VERSION = '0'
MINOR_VERSION = '0'
MICRO_VERSION = '0'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

setup(name='neural_complete',
      version=VERSION,
      description="Neural Network for Autocomplete",
      author='Pascal van Kooten',
      url='https://github.com/kootenpv/neural_complete',
      author_email='kootenpv@gmail.com',
      install_requires=[
          'numpy', 'flask', 'keras', 'just'
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Customer Service',
          'Operating System :: Microsoft',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities'
      ],
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      platforms='any')
