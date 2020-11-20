from __future__ import print_function
import sys
from sys import version
from setuptools import setup, find_packages
import pathlib

# here = pathlib.Path(__file__).parent.resolve()
# root = here.parent.resolve()
# long_description = (root / 'README.md').read_text(encoding='utf-8')
long_description = """
This is a package for DataFrame-based graphs on top of Apache Spark. Users can write highly expressive queries by leveraging the DataFrame API, combined with a new API for motif finding. The user also benefits from DataFrame performance optimizations within the Spark SQL engine.
"""

try:
    exec(open("graphframes/version.py").read())
except IOError:
    print(
        "Failed to load PySpark version file for packaging. You must be in graphframes's python dir.",
        file=sys.stderr,
    )
    sys.exit(-1)

VERSION = __version__  # noqa
setup(
    name="graphframes",
    version=VERSION,
    description="Spark DataFrame-based Graphs",
    long_description=long_description,
    author="",
    author_email="",
    url="",
    packages=["graphframes", "graphframes.lib", "graphframes.examples"],
    install_requires=["py4j==0.10.7", "numpy>=1.7"],
    keywords='spark, graphx, dataframe, graphdataframe',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
