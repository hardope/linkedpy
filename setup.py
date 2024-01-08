from setuptools import setup, find_packages

# Load the long description from a separate file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="linkedpy",
    version="0.0.5",
    author="Opeoluwa Adeyeri",
    author_email="adeyeriopeoluwa05@gmail.com",
    url="https://github.com/hardope/MyList",
    description="Python implementation of a default List using linked list",
    long_description=long_description,  # Use the content from README.md or another file
    long_description_content_type="text/markdown",  # Specify the type of content
    packages=['linkedpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
