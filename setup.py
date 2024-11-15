from setuptools import setup, find_packages

setup(
    name="scope-cli",  # Project name for PyPI
    version="0.2.1",
    description="A CLI tool for visualizing directory sizes and checking port usage.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Deepam Patel",
    author_email="deepam8155@gmail.com",
    url="https://github.com/deepampatel/scope-cli",
    packages=find_packages(),
    install_requires=["psutil"],
    entry_points={
        "console_scripts": [
            "scope=scope.main:main",  # CLI command will be 'scope'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
