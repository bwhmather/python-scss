from sass._sass import (
    compile_string as _compile_string,
    compile_file as _compile_file,
    CompileError,
)


def compile_string(*args, **kwargs):
    return _compile_string(*args, **kwargs)


def compile_file(*args, **kwargs):
    return _compile_file(*args, **kwargs)

__all__ = ['compile_string', 'compile_file', 'CompileError']
