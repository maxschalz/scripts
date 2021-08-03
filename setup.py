#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

def main():
    """Main function."""

    setup(
        name="scripts",
        version="0.1",
        description="Scripts to generate Python and other scripts",
        author="Max Schalz",
        url="https://github.com/maxschalz/scripts/",
        license="BSD-3-Clause",
        packages=["scripts"],
        classifiers=["License :: OSI Approved :: BSD-3-Clause License",
                     "Programming Language :: Python :: 3"],
        install_requires=None,
        entry_points={"console_scripts": ["initpython = scripts:init_python",
                                          "initlatex = scripts:init_latex",
                                          "initconfig = scripts:cmdline_config"]},
    )

if __name__=="__main__":
    main()
