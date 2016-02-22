"""The PyRhO package setup script"""

from __future__ import print_function       # Added for (eventual) Python 2.x support
from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
#from os import path
import os


# Download and install setuptools if not installed
#from ez_setup import use_setuptools
#use_setuptools()
#python -m ensurepip --upgrade

#from setuptools import setup
#from distutils import setup

here = os.path.abspath(os.path.dirname(__file__))
home = os.path.expanduser("~")
print(home)
prwd = os.path.join(home, 'pyrho') # pyrho working directory

# Get the long description from the relevant file
with open(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

#cwd=os.getcwd()

# Directories
#dDir = cwd+'/data/'
#fDir = cwd+'/figs/'

#def createDir(path):
#    try:
#        os.makedirs(path)
#    except OSError as exception:
#        if exception.errno != errno.EEXIST:
#            raise

#createDir(dDir)
#createDir(fDir)
    
setup(
    name='PyRhO',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.9.1',

    description='A Python module to fit and characterise rhodopsin photocurrents',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/ProjectPyRhO/PyRhO', 

    # Author details
    author='Benjamin D. Evans',
    author_email='ben.d.evans@gmail.com',

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Bio-Informatics',                       ### Consider these topics
        'Topic :: Scientific/Engineering :: Artificial Life',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        #'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.6',
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        
        'Framework :: IPython',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],

    # What does your project relate to?
    keywords='optogenetics rhodopsin opsin brain neuroscience neuron brian jupyter',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),# + ['NEURON'],
    
    #package_dir = {'':'.'},
    #package_dir = {'pyrho': 'pyrho'}, # Relative to this script

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy>=1.8', 'scipy>=0.15', 'matplotlib>=1.3', 'lmfit>=0.9', 'ipython>=4.1', 'brian2'], #'sphinx>=1.3', 
    
    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require = {
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #    'brian' : ['brian2'],
        'GUI'   : ['jupyter>=1.0', 'notebook>=4.1', 'ipywidgets>=4.1', 'traitlets>=4.1', 'seaborn'], #, 'ipython>=4'
        'full'  : ['jupyter>=1.0', 'notebook>=4.1', 'ipywidgets>=4.1', 'traitlets>=4.1', 'seaborn'],
    },
    
    include_package_data=True,
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        '': ['NEURON/*.mod', 'NEURON/*.hoc', 'gui/*.png', 'datasets/*.pkl'], # 'NEURON', 
        #'sample': ['package_data.dat'],
    },
    

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],
    #data_files=[#(prwd, []),
    #            (prwd, [os.path.join(prwd, 'gui/*.png'), ])],
    
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    #},
)
