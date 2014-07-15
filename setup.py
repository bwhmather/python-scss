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

from setuptools import setup, Extension, find_packages
from setuptools.command.sdist import sdist as _sdist
from setuptools.command.develop import develop as _develop

cmdclass = {}

libsass_sources = [
    'libsass/ast.cpp',
    'libsass/base64vlq.cpp',
    'libsass/bind.cpp',
    'libsass/constants.cpp',
    'libsass/context.cpp',
    'libsass/contextualize.cpp',
    'libsass/copy_c_str.cpp',
    'libsass/emscripten_wrapper.cpp',
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
    'libsass/trim.cpp',
    'libsass/units.cpp',
]

from setuptools.dist import Distribution
Distribution(dict(setup_requires=['Cython']))

if not os.path.exists('sass.cpp'):
    from Cython.Distutils import build_ext
    sources = libsass_sources + ['sass.pyx']
    cmdclass['build_ext'] = build_ext
else:
    sources = libsass_sources + ['sass.cpp']

ext_modules = [
    Extension(
        'sass._sass', sources,
        libraries=['stdc++'], library_dirs=['./libsass'],
        include_dirs=['.', 'libsass'], language='c++'
    ),
]


class sdist(_sdist):
    def run(self):
        from Cython.Build import cythonize
        print("pre-compiling cython")
        cythonize(['sass.pyx'])

        super(sdist, self).run()

cmdclass['sdist'] = sdist


class develop(_develop):
    def run(self):
        from subprocess import check_call
        print("retrieving libsass submodule")
        if os.path.exists('.git'):
            check_call(['git', 'submodule', 'update', '--init', '--recursive'])
        super(develop, self).run()

cmdclass['develop'] = develop

setup(
    name='sass',
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    version='2.2',
    author='Sergey Kirilov',
    author_email='sergey.kirillov@gmail.com',
    url='https://github.com/pistolero/python-scss',
    install_requires=[],
    test_suite='sass.tests.suite',
    packages=find_packages(),
    license='Apache License 2.0',
    keywords='sass scss libsass',
    description='Python bindings for libsass',
    zip_safe=False,
)
