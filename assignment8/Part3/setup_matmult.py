# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:05:00 2024

@author: mtthl

Set up the functions from matmult.pyx


"""

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
        "matmult",
        sources=["matmult.pyx"],
        extra_compile_args=["-std=c99"],  # Specify C99 standard
        include_dirs=[numpy.get_include()],
    )
]

setup(
    ext_modules=cythonize(ext_modules),
)
