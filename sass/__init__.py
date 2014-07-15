import sass._sass as _sass
from sass._sass import CompileError


def compile_string(string, include_paths=b'', image_path=b'',
                   output_style=_sass.SASS_STYLE_NESTED):
    if not isinstance(string, bytes):
        string = string.encode()
    if not isinstance(include_paths, bytes):
        include_paths = include_paths.encode()
    if not isinstance(image_path, bytes):
        image_path = image_path.encode()
    return _sass.compile_string(string, include_paths, image_path, output_style)


def compile_file(path, include_paths=b'', image_path=b'',
                 output_style=_sass.SASS_STYLE_NESTED):
    if not isinstance(path, bytes):
        path = path.encode()
    if not isinstance(include_paths, bytes):
        include_paths = include_paths.encode()
    if not isinstance(image_path, bytes):
        image_path = image_path.encode()
    return _sass.compile_string(path, include_paths, image_path, output_style)

__all__ = ['compile_string', 'compile_file', 'CompileError']
