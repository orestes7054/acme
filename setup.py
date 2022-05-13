from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="acme-ioet-exercise",
    version= '0.0.2',
    description="App to calculate salary of Acme's Employees",
    license="MIT",
    author="Orestes Olivera Marrero",
    author_email="orestes.om@gmail.com",
    url="https://github.com/orestes7054/acme",
    packages=find_packages(),
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.7",
    project_urls={
        "Homepage": "https://github.com/orestes7054/acme",
        "Source Code": "https://github.com/orestes7054/acme",
    },
)