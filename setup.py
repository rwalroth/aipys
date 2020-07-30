import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aipys",
    version="0.0.1",
    author="Richard Walroth",
    author_email="rwalroth89@gmail.com",
    description="Python tools to help with orca calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rwalroth/aipys",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",
        "numpy",
        "scipy",
        "matplotlib",
    ],
)