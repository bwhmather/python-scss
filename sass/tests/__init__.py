#   Copyright 2012 Sergey Kirillov
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from __future__ import unicode_literals

import unittest
from os import path

import sass

scss_test_file = str(path.normpath(
    path.join(path.dirname(__file__), 'test.scss'))
)
compiled_result = b'''table.hl {
  margin: 2em 0; }
  table.hl td.ln {
    text-align: right; }

li {
  font-family: serif;
  font-weight: bold;
  font-size: 1.2em; }
'''


class SASSTest(unittest.TestCase):

    def test_compile_string_with_bad_string(self):
        try:
            sass.compile_string(b'bad string')
        except sass.CompileError:
            pass
        else:
            self.fail()

    def test_compile_string(self):
        with file(scss_test_file, 'rb') as scss_file:
            result = sass.compile_string(scss_file.read())
        self.assertEqual(result, compiled_result)

    def test_compile_file(self):
        result = sass.compile_file(scss_test_file)
        self.assertEqual(result, compiled_result)


loader = unittest.TestLoader()
suite = unittest.TestSuite((
    loader.loadTestsFromTestCase(SASSTest),
))
