from setuptools import setup, find_packages

setup(
    name='py-hn',
    version='0.1.0',
    packages=find_packages(),
    description='An unofficial Hacker News API Client Library in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='mfiro',
    author_email='mfiro@protonmail.com',
    url='https://github.com/mfiro/py-hn',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)