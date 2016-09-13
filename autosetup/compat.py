import sys

is_py2 = (sys.version_info[0] == 2)
is_py3 = (sys.version_info[0] == 3)

if is_py2:
    from urlparse import urlparse  # noqa
    input_method = raw_input

if is_py3:
    from urllib.parse import urlparse  # noqa
    input_method = input
