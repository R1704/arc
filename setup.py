from setuptools import setup, find_packages

setup(
    name='arc',
    version='0.1.0',
    author='ron',
    author_email='ron.hommelsheim@gmail.com',
    description='A framework for dealing with various ARC challenges by Chollet.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/R1704/arc',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'numpy>=1.19.0',
        'matplotlib>=3.3.0',
        'requests>=2.25.0',
        'tqdm>=4.50.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7',
)