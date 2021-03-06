# type: ignore
import os

from setuptools import find_packages, setup

import versioneer

package = "epysurv"


_here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=package,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Epidemiological surveillance in Python.",
    long_description=long_description,
    author="Rüdiger Busche",
    author_email="rbusche@uos.de",
    url="https://github.com/JarnoRFB/epysurv",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    package_data={package: [os.path.join("data", "*.csv")]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
    project_urls={
        "Bug Reports": "https://github.com/JarnoRFB/epysurv/issues",
        "Source": "https://github.com/JarnoRFB/epysurv",
    },
)
