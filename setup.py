#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from io import open
import os.path as osp
from setuptools import setup


HERE = osp.abspath(osp.dirname(__file__))
sys.path.insert(0, HERE)
import pibooth_printer_refill_message as plugin

def main():
    setup(
        name=plugin.__name__,
        version=plugin.__version__,
        description=plugin.__doc__,
        long_description=open(osp.join(HERE, "README.md"), encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Natural Language :: English',
            'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
        ],
        author="Dominik Dörr",
        url="https://git.dominikdoerr.de/dominikdoerr/pibooth-printer-refill-message",
        license="GPLv3",
        platforms=['unix', 'linux'],
        keywords=[
            'Raspberry Pi',
            'camera',
            'photobooth'
        ],
        py_modules=["pibooth_printer_refill_message"],
        python_requires=">=3.6",
        install_requires=[
            'pibooth>=2.0.0'
        ],
        zip_safe=False,
        entry_points={'pibooth': ["pibooth_printer_refill_message = pibooth_printer_refill_message"]},
    )

if __name__ == '__main__':
    main()

