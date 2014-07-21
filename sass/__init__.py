import sass._sass as _sass
from sass._sass import CompileError

OUTPUT_STYLES = {
    'nested': 0,
    'expanded': 1,
    'compact': 2,
    'compressed': 3,
}


def compile_string(string, include_paths=b'', image_path=b'',
                   output_style='nested'):
    if not isinstance(string, bytes):
        string = string.encode('utf-8')
    if not isinstance(include_paths, bytes):
        include_paths = include_paths.encode('utf-8')
    if not isinstance(image_path, bytes):
        image_path = image_path.encode('utf-8')
    output_style = OUTPUT_STYLES[output_style]

    return _sass.compile_string(
        string, include_paths, image_path, output_style
    )


def compile_file(path, include_paths=b'', image_path=b'',
                 output_style='nested'):
    if not isinstance(path, bytes):
        path = path.encode('utf-8')
    if not isinstance(include_paths, bytes):
        include_paths = include_paths.encode('utf-8')
    if not isinstance(image_path, bytes):
        image_path = image_path.encode('utf-8')
    output_style = OUTPUT_STYLES[output_style]

    return _sass.compile_file(
        path, include_paths, image_path, output_style
    )

__all__ = ['compile_string', 'compile_file', 'CompileError']
