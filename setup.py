#!/usr/bin/env python
import os
from distutils.core import setup, Extension
sources = [
    'src/python/core.c',
    'src/libaquahash/io.c',
    'src/libaquahash/internal.c',
    'src/libaquahash/sha3.c']
if os.name == 'nt':
    sources += [
        'src/libaquahash/util_win32.c',
        'src/libaquahash/io_win32.c',
        'src/libaquahash/mmap_win32.c',
    ]
else:
    sources += [
        'src/libaquahash/io_posix.c'
    ]
depends = [
    'src/libaquahash/aquahash.h',
    'src/libaquahash/compiler.h',
    'src/libaquahash/data_sizes.h',
    'src/libaquahash/endian.h',
    'src/libaquahash/aquahash.h',
    'src/libaquahash/io.h',
    'src/libaquahash/fnv.h',
    'src/libaquahash/internal.h',
    'src/libaquahash/sha3.h',
    'src/libaquahash/util.h',
]
pyaquahash = Extension('pyaquahash',
                     sources=sources,
                     depends=depends,
                     extra_compile_args=["-Isrc/", "-std=gnu99", "-Wall"])

setup(
    name='pyaquahash',
    author="Matthew Wampler-Doty",
    author_email="matthew.wampler.doty@gmail.com",
    license='GPL',
    version='0.1.23',
    url='https://github.com/ethereum/aquahash',
    download_url='https://github.com/ethereum/aquahash/tarball/v23',
    description=('Python wrappers for aquahash, the ethereum proof of work'
                 'hashing function'),
    ext_modules=[pyaquahash],
)
