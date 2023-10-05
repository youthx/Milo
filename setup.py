import setuptools

long_desc = open("README.md").read()
required = [] # Comma seperated dependent libraries name
with open("./requirements.txt", "r") as f:
    for req in f.readlines():
        req = req.split("=")
        required.append(req)

setuptools.setup(
    name="milo",
    version="1.1.0", # eg:1.0.0
    author="Jack Waechter",
    author_email="jackwaechter0@gmail.com",
    license="MIT",
    description="An organized python project creation tool.",
    long_description="Milo is a python project creation tool, which allows you to easily create & build python projects.",
    long_description_content_type="text/markdown",
    url="<PACKAGE GITHUB URL>",
    packages = ['milo'],
    key_words="environment, venv, creation, init",
    install_requires=required,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)