#!/usr/bin/env python
#   Copyright 2012 Sergey Kirillov
#
#   Licensed under the Apache License, Version 2.0 (the 'License');
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an 'AS IS' BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import os.path

from distutils.extension import Extension
from setuptools import setup, Extension


try:
    from Cython.Distutils import build_ext
except ImportError:
    if not os.path.exists('sass.cpp'):
        raise
    print('No Cython installed. Building from pregenerated C source.')
    build_ext = None

here = os.path.dirname(os.path.abspath(__file__))

libsass_sources = [
    'libsass/ast.cpp',
    'libsass/base64vlq.cpp',
    'libsass/bind.cpp',
    'libsass/constants.cpp',
    'libsass/context.cpp',
    'libsass/contextualize.cpp',
    'libsass/copy_c_str.cpp',
    'libsass/error_handling.cpp',
    'libsass/eval.cpp',
    'libsass/expand.cpp',
    'libsass/extend.cpp',
    'libsass/file.cpp',
    'libsass/functions.cpp',
    'libsass/inspect.cpp',
    'libsass/output_compressed.cpp',
    'libsass/output_nested.cpp',
    'libsass/parser.cpp',
    'libsass/prelexer.cpp',
    'libsass/sass.cpp',
    'libsass/sass_interface.cpp',
    'libsass/source_map.cpp',
    'libsass/to_c.cpp',
    'libsass/to_string.cpp',
    'libsass/units.cpp'
]

if build_ext:
    sources = libsass_sources + ['sass.pyx']
    cmdclass = {'build_ext': build_ext}
else:
    sources = libsass_sources + ['sass.cpp']
    cmdclass = {}

ext_modules = [
    Extension('sass', sources, libraries=['stdc++'], library_dirs=['./libsass'],
              include_dirs=['.', 'libsass'], language='c++')]

from setuptools.command.develop import develop
from subprocess import check_call

class update_submodules(develop):
    def run(self):
        print("retrieving libsass submodule")
        if os.path.exists('.git'):
            check_call(['git', 'submodule', 'update', '--init', '--recursive'])
        develop.run(self)

cmdclass["develop"] = update_submodules

setup(
    name='sass',
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    version='2.2',
    author='Sergey Kirilov',
    author_email='sergey.kirillov@gmail.com',
    url='https://github.com/pistolero/python-scss',
    install_requires=[],
    extras_require={
        #    'develop': ['Cython']
    },
    tests_require=['nose'],
    test_suite='test',
    license='Apache License 2.0',
    keywords='sass scss libsass',
    description='Python bindings for libsass',
    long_description=open(os.path.join(here, 'README.rst'), 'rb').read().decode('utf-8')
)
