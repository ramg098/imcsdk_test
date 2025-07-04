import inspect


def validate_sdk_method(method):
    """Return the file path and starting line number for an SDK method."""
    if not callable(method):
        raise ValueError(f"{method} is not callable")
    source_file = inspect.getsourcefile(method)
    source_lines, start_line = inspect.getsourcelines(method)
    return source_file, start_line

