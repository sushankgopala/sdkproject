from setuptools import setup, find_packages

setup(
    name='sdkproject',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'openpyxl',
    ],
    entry_points={
        'console_scripts': [
            'sdkproject=sdkproject.cli:main',
        ],
    },
    author='Trinet',
    description='CLI to create a RAG project folder structure',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.9',
)
