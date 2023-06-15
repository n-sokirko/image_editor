import os
import pybind11

from setuptools import setup, Extension

module_name = "image_processing"

module = Extension(
    module_name,
    sources=["image_processing.cpp"],
    include_dirs=[pybind11.get_include()],
    extra_compile_args=["-std=c++11"],
)

setup(
    name=module_name,
    ext_modules=[module],
)
