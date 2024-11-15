from setuptools import setup, find_packages

setup(
    name="scope-cli",  # Updated package name
    version="0.2.0",
    description="A CLI tool for visualizing directory sizes and checking port usage.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Deepam Patel",
    author_email="deepam8155@gmail.com",
    url="https://github.com/deepampatel/scope-cli",  # Updated GitHub URL
    packages=find_packages(),
    install_requires=["psutil"],
    entry_points={
        "console_scripts": [
            "scope-cli=scope.main:main",  # Updated CLI command
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
